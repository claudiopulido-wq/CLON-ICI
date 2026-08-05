<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: Content-Type");
header("Content-Type: application/json; charset=UTF-8");

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode(["status" => "error", "message" => "Only POST requests are allowed"]);
    exit;
}

// Get POST data
$input = json_decode(file_get_contents("php://input"), true);

if (!$input) {
    $input = $_POST;
}

$email = filter_var($input['email'] ?? '', FILTER_VALIDATE_EMAIL);
$fname = strip_tags($input['fname'] ?? 'there');
$result_id = strip_tags($input['result_id'] ?? 'result-6');
$result_title = strip_tags($input['result_title'] ?? 'Personalized Advisor Recommendation');
$result_why = $input['result_why'] ?? [];

if (!$email) {
    echo json_encode(["status" => "error", "message" => "A valid email address is required"]);
    exit;
}

$why_html = "";
if (is_array($result_why) && count($result_why) > 0) {
    foreach ($result_why as $bullet) {
        // Strip checkmarks if already present, we will render it beautifully
        $clean_bullet = ltrim(strip_tags($bullet), "✓ ");
        $why_html .= '<li style="margin-bottom: 8px; color: #555555; list-style: none;">✓ ' . $clean_bullet . '</li>';
    }
} else {
    $why_html = '<li style="margin-bottom: 8px; color: #555555; list-style: none;">✓ Get personalized guidance based on your goals.</li>';
    $why_html .= '<li style="margin-bottom: 8px; color: #555555; list-style: none;">✓ Find the certification that best fits your experience.</li>';
}

$subject = "Your ICI Evaluation Kit has arrived!";
$from_email = "contact@certifyyourfuture.org";

$headers = "MIME-Version: 1.0" . "\r\n";
$headers .= "Content-Type: text/html; charset=UTF-8" . "\r\n";
$headers .= "From: ICI Certificaciones <" . $from_email . ">" . "\r\n";
$headers .= "Reply-To: " . $from_email . "\r\n";

$message = '
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your ICI Evaluation Kit</title>
</head>
<body style="font-family: \'Outfit\', \'Montserrat\', Helvetica, Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; -webkit-font-smoothing: antialiased;">
    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f4f4f4; padding: 20px 0;">
        <tr>
            <td align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                    <!-- Header with Logo -->
                    <tr>
                        <td align="center" style="padding: 25px 20px; border-bottom: 1px solid #eeeeee;">
                            <img src="https://claudiopulido-wq.github.io/CLON-ICI/assets/ici-logo-color.png" alt="ICI Certificaciones" style="height: 60px; max-height: 60px; display: block; border: 0;">
                        </td>
                    </tr>
                    <!-- Hero Banner Image -->
                    <tr>
                        <td align="center">
                            <img src="https://claudiopulido-wq.github.io/CLON-ICI/assets/para-mail.jpg" alt="Your Official Evaluation Kit is Inside" style="width: 100%; max-width: 600px; display: block; border: 0;">
                        </td>
                    </tr>
                    <!-- Main Body Content -->
                    <tr>
                        <td style="padding: 40px 30px; background-color: #ffffff;">
                            <h2 style="color: #0651a3; font-size: 24px; font-weight: 800; margin-top: 0; margin-bottom: 15px; text-align: center;">Your Evaluation Kit is Ready!</h2>
                            <p style="color: #444444; font-size: 16px; line-height: 1.6; margin-bottom: 25px;">
                                Hi <strong>' . htmlspecialchars($fname) . '</strong>,
                            </p>
                            <p style="color: #444444; font-size: 16px; line-height: 1.6; margin-bottom: 25px;">
                                Thank you for taking our evaluation quiz! Your evaluation kit is on its way. Based on your responses, we have customized a learning pathway tailored to your experience and goals.
                            </p>
                            
                            <!-- Recommendation Box -->
                            <div style="background-color: #f9f9f9; border-left: 4px solid #fdcb00; padding: 20px; border-radius: 4px; margin-bottom: 30px;">
                                <h3 style="color: #0651a3; font-size: 18px; font-weight: 700; margin-top: 0; margin-bottom: 5px;">Recommended Path:</h3>
                                <p style="color: #1a1a1a; font-size: 16px; font-weight: bold; margin-top: 0; margin-bottom: 15px;">' . htmlspecialchars($result_title) . '</p>
                                
                                <p style="font-weight: bold; margin-bottom: 10px; font-size: 14px; color: #333333; text-transform: uppercase; letter-spacing: 0.5px;">Why this fits you:</p>
                                <ul style="margin: 0; padding-left: 0; list-style-type: none; font-size: 15px;">
                                    ' . $why_html . '
                                </ul>
                            </div>
                            
                            <!-- CTA Button -->
                            <table border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-top: 25px;">
                                <tr>
                                    <td align="center">
                                        <a href="https://claudiopulido-wq.github.io/CLON-ICI/" target="_blank" style="background-color: #0651a3; color: #ffffff; text-decoration: none; padding: 15px 30px; font-size: 16px; font-weight: 700; border-radius: 5px; display: inline-block; box-shadow: 0 4px 6px rgba(6,81,163,0.2); transition: background-color 0.3s ease;">Access Your Portal</a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <!-- Footer -->
                    <tr>
                        <td align="center" style="padding: 30px 20px; background-color: #1a1a1a; color: #ffffff;">
                            <p style="margin: 0 0 10px 0; font-size: 14px; font-weight: bold;">Building the Next Generation of Fitness Professionals.</p>
                            <p style="margin: 0 0 20px 0; font-size: 12px; color: #aaaaaa;">&copy; ' . date("Y") . ' ICI Certificaciones. All rights reserved.</p>
                            <table border="0" cellpadding="0" cellspacing="0">
                                <tr>
                                    <td style="padding: 0 10px;">
                                        <a href="https://wa.me/19567393519" target="_blank" style="color: #fdcb00; text-decoration: none; font-size: 12px;">WhatsApp</a>
                                    </td>
                                    <td style="color: #666666;">|</td>
                                    <td style="padding: 0 10px;">
                                        <a href="mailto:contact@certifyyourfuture.org" style="color: #fdcb00; text-decoration: none; font-size: 12px;">Contact Support</a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
';

if (mail($email, $subject, $message, $headers)) {
    echo json_encode(["status" => "success", "message" => "Email sent successfully to $email"]);
} else {
    echo json_encode(["status" => "error", "message" => "Failed to send email. Check PHP mail configuration."]);
}
?>
