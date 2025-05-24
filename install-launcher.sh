#!/bin/bash

# === Distro detection ===
if [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO=$ID
else
    echo "Unsupported system: /etc/os-release not found."
    exit 1
fi

echo "[*] Detected distro: $DISTRO"

# === Install dependencies ===
case "$DISTRO" in
    debian|ubuntu)
        sudo apt update
        sudo apt install -y python3 python3-tk curl
        ;;
    fedora)
        sudo dnf install -y python3 python3-tkinter curl
        ;;
    arch)
        sudo pacman -Sy --noconfirm python python-tk curl
        ;;
    *)
        echo "Unsupported distro: $DISTRO"
        exit 1
        ;;
esac

# === Create scripts folder ===
mkdir -p ~/scripts

# === Download the launcher script ===
curl -L https://raw.githubusercontent.com/neuralcurtis/conflaunch/main/launch.py -o ~/scripts/launch.py
chmod +x ~/scripts/launch.py

# === Create .desktop launcher ===
mkdir -p ~/.local/share/applications
cat > ~/.local/share/applications/conflaunch.desktop <<EOF
[Desktop Entry]
Name=Config Launcher
Exec=python3 /home/$USER/scripts/launch.py
Type=Application
Terminal=false
Categories=Utility;
EOF

echo "[✓] Installed Config Launcher."
echo "→ You can now search for 'Config Launcher' in your app menu."

