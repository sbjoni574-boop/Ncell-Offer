# sms_forwarder.py
import serial
import requests
import time

TELEGRAM_URL = "https://api.telegram.org/bot<BOT_TOKEN>/sendMessage"
CHAT_ID = "<YOUR_CHAT_ID>"
SERIAL_PORT = "/dev/ttyUSB0"  # SIM modem

def send_to_telegram(msg):
    requests.post(TELEGRAM_URL, data={"chat_id": CHAT_ID, "text": "📱 SMS CAPTURED:\n" + msg})

ser = serial.Serial(SERIAL_PORT, 115200, timeout=1)
ser.write(b'AT+CMGF=1\r')  # Text mode
time.sleep(1)
ser.write(b'AT+CNMI=2,2,0,0,0\r')  # SMS push to serial
time.sleep(1)

print("[+] Listening for SMS...")

while True:
    try:
        line = ser.readline().decode('utf-8', errors='ignore')
        if "+CMT" in line:
            number = line.split('"')[1]
            timestamp = line.split('"')[3]
            message = ser.readline().decode('utf-8', errors='ignore')
            full_sms = f"From: {number}\nTime: {timestamp}\nMessage: {message}"
            send_to_telegram(full_sms)
            print(full_sms)
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(1)
