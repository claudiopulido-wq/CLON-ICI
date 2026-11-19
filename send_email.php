<?php
// Aviso interno de un nuevo prospecto del quiz «Ask an Advisor».
// Solo envía a un destinatario fijo de ICI (nunca a la dirección que llega por POST),
// solo acepta POST desde el propio sitio y limita los envíos por IP y por día.

header("Content-Type: application/json; charset=UTF-8");

const TO_EMAIL      = 'contact@certifyyourfuture.org';
const FROM_EMAIL    = 'contact@certifyyourfuture.org';
const ALLOWED_HOSTS = ['certifyyourfuture.org', 'www.certifyyourfuture.org'];
const MAX_PER_IP    = 5;    // envíos por IP por hora
const MAX_PER_DAY   = 100;  // envíos totales por día

function respond($code, $status, $message) {
    http_response_code($code);
    echo json_encode(["status" => $status, "message" => $message]);
    exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Allow: POST');
    respond(405, "error", "Only POST requests are allowed");
}

// Mismo origen: si el navegador manda Origin o Referer, debe ser el propio sitio.
$src = $_SERVER['HTTP_ORIGIN'] ?? ($_SERVER['HTTP_REFERER'] ?? '');
$srcHost = strtolower((string) parse_url($src, PHP_URL_HOST));
if ($srcHost === '' || !in_array($srcHost, ALLOWED_HOSTS, true)) {
    respond(403, "error", "Forbidden");
}

// Límite de envíos (archivos en el directorio temporal del servidor).
function rate_ok($key, $limit, $window) {
    $file = rtrim(sys_get_temp_dir(), '/\\') . '/ici_rl_' . hash('sha256', $key);
    $now = time();
    $fh = @fopen($file, 'c+');
    if (!$fh) return true; // si no se puede escribir, no bloquear el formulario
    flock($fh, LOCK_EX);
    $hits = array_filter(array_map('intval', explode(',', stream_get_contents($fh))), function ($t) use ($now, $window) {
        return $t > $now - $window;
    });
    $ok = count($hits) < $limit;
    if ($ok) $hits[] = $now;
    ftruncate($fh, 0); rewind($fh); fwrite($fh, implode(',', $hits));
    flock($fh, LOCK_UN); fclose($fh);
    return $ok;
}
$ip = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
if (!rate_ok('ip:' . $ip, MAX_PER_IP, 3600) || !rate_ok('day', MAX_PER_DAY, 86400)) {
    respond(429, "error", "Too many requests. Please try again later.");
}

$input = json_decode(file_get_contents("php://input"), true);
if (!is_array($input)) $input = $_POST;

function clean($v, $max) {
    $v = trim(strip_tags((string) $v));
    $v = preg_replace('/[\r\n\t]+/', ' ', $v);
    return mb_substr($v, 0, $max);
}

$email = filter_var(clean($input['email'] ?? '', 254), FILTER_VALIDATE_EMAIL);
if (!$email) {
    respond(400, "error", "A valid email address is required");
}
$fname        = clean($input['fname'] ?? '', 80);
$result_id    = clean($input['result_id'] ?? '', 40);
$result_title = clean($input['result_title'] ?? '', 150);
$why = [];
if (is_array($input['result_why'] ?? null)) {
    foreach (array_slice($input['result_why'], 0, 10) as $b) $why[] = clean($b, 200);
}

$subject = "Nuevo prospecto del quiz: " . ($result_title !== '' ? $result_title : 'sin resultado');
$body  = "Nuevo prospecto desde el quiz «Ask an Advisor» de certifyyourfuture.org\n\n";
$body .= "Nombre: " . ($fname !== '' ? $fname : '(sin nombre)') . "\n";
$body .= "Correo: " . $email . "\n";
$body .= "Resultado: " . $result_title . " (" . $result_id . ")\n";
if ($why) $body .= "Motivos mostrados:\n- " . implode("\n- ", $why) . "\n";
$body .= "\nFecha (UTC): " . gmdate('Y-m-d H:i:s') . "\nIP: " . $ip . "\n";

$headers  = "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
$headers .= "From: ICI <" . FROM_EMAIL . ">\r\n";
$headers .= "Reply-To: " . $email . "\r\n";

if (mail(TO_EMAIL, '=?UTF-8?B?' . base64_encode($subject) . '?=', $body, $headers)) {
    respond(200, "success", "Thanks! We received your answers.");
}
respond(500, "error", "We could not process your request right now.");
