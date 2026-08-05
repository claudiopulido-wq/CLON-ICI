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
                                        <a href="https://claudiopulido-wq.github.io/CLON-ICI/" target="_blank" style="background-color: #0651a3; color: #ffffff; text-decoration: none; padding: 15px 30px; font-size: 16px; font-weight: 700; border-radius: 5px; display: inline-block; box-shadow: 0 4px 6px rgba(6,81,163,0.2); transition: background-color 0.3s ease;">Download Your Evaluation Kit</a>
                                    </td>
                                </tr>
                            </table>

                            <!-- Section: Inside Your Evaluation Kit -->
                            <div style="margin-top: 40px; border-top: 1px solid #eeeeee; padding-top: 30px;">
                                <h3 style="color: #e26a37; font-size: 20px; font-weight: 700; margin-top: 0; margin-bottom: 15px; text-align: center; font-family: 'Montserrat', sans-serif;">Inside Your Evaluation Kit</h3>
                                <p style="color: #444444; font-size: 15px; line-height: 1.6; margin-bottom: 20px;">
                                    We've packed this guide with everything you need to make an informed decision about your future:
                                </p>
                                <ul style="margin: 0 0 20px 0; padding-left: 20px; font-size: 15px; color: #444444; line-height: 1.6;">
                                    <li style="margin-bottom: 10px;"><strong>The Fitness Blueprint:</strong> An 11-step roadmap from enrollment to landing your first client.</li>
                                    <li style="margin-bottom: 10px;"><strong>Certification Overviews:</strong> Deep dives into Personal Trainer, Elite Trainer, and Coach programs.</li>
                                    <li style="margin-bottom: 10px;"><strong>Career Opportunities:</strong> Guidance on launching your career in gyms, studios, or online.</li>
                                    <li style="margin-bottom: 10px;"><strong>Study Tool Previews:</strong> A look at our dynamic learning modules, study materials, and success support.</li>
                                </ul>
                            </div>

                            <!-- Section: Your 3-Step Start -->
                            <div style="margin-top: 35px; border-top: 1px solid #eeeeee; padding-top: 30px; margin-bottom: 10px;">
                                <h3 style="color: #e26a37; font-size: 20px; font-weight: 700; margin-top: 0; margin-bottom: 20px; text-align: center; font-family: 'Montserrat', sans-serif;">Your 3-Step Start</h3>
                                
                                <!-- Step 1 -->
                                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f9f9f9; border-radius: 6px; margin-bottom: 15px; border: 1px solid #eeeeee;">
                                    <tr>
                                        <td style="padding: 20px;">
                                            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                                <tr>
                                                    <td valign="top" width="40">
                                                        <span style="background-color: #fdcb00; color: #1a1a1a; width: 28px; height: 28px; line-height: 28px; border-radius: 50%; display: inline-block; text-align: center; font-weight: bold; font-size: 14px;">1</span>
                                                    </td>
                                                    <td valign="top">
                                                        <h4 style="margin: 0 0 5px 0; color: #1a1a1a; font-size: 16px; font-weight: 700;">Review the Kit</h4>
                                                        <p style="margin: 0; color: #555555; font-size: 14px; line-height: 1.5;">Find the program that fits your goals—whether you want to work in a gym or start an online business.</p>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>

                                <!-- Step 2 -->
                                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f9f9f9; border-radius: 6px; margin-bottom: 15px; border: 1px solid #eeeeee;">
                                    <tr>
                                        <td style="padding: 20px;">
                                            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                                <tr>
                                                    <td valign="top" width="40">
                                                        <span style="background-color: #fdcb00; color: #1a1a1a; width: 28px; height: 28px; line-height: 28px; border-radius: 50%; display: inline-block; text-align: center; font-weight: bold; font-size: 14px;">2</span>
                                                    </td>
                                                    <td valign="top">
                                                        <h4 style="margin: 0 0 5px 0; color: #1a1a1a; font-size: 16px; font-weight: 700;">Talk to an Advisor</h4>
                                                        <p style="margin: 0; color: #555555; font-size: 14px; line-height: 1.5;">Have questions about certifications or flexible payment options? Our team is ready to help.</p>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>

                                <!-- Step 3 -->
                                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f9f9f9; border-radius: 6px; margin-bottom: 25px; border: 1px solid #eeeeee;">
                                    <tr>
                                        <td style="padding: 20px;">
                                            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                                <tr>
                                                    <td valign="top" width="40">
                                                        <span style="background-color: #fdcb00; color: #1a1a1a; width: 28px; height: 28px; line-height: 28px; border-radius: 50%; display: inline-block; text-align: center; font-weight: bold; font-size: 14px;">3</span>
                                                    </td>
                                                    <td valign="top">
                                                        <h4 style="margin: 0 0 5px 0; color: #1a1a1a; font-size: 16px; font-weight: 700;">Claim Your Discount</h4>
                                                        <p style="margin: 0; color: #555555; font-size: 14px; line-height: 1.5;">Use the exclusive code <strong>EVALKIT50</strong> to take $50 off your enrollment today!</p>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>

                                <!-- Start Your Career Now Button -->
                                <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                    <tr>
                                        <td align="center">
                                            <a href="https://claudiopulido-wq.github.io/CLON-ICI/" target="_blank" style="background-color: #fdcb00; color: #1a1a1a; text-decoration: none; padding: 15px 30px; font-size: 16px; font-weight: 700; border-radius: 5px; display: inline-block; box-shadow: 0 4px 6px rgba(253,203,0,0.2); transition: background-color 0.3s ease;">Start Your Career Now</a>
                                        </td>
                                    </tr>
                                </table>
                            </div>
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
