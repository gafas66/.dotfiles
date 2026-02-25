################################################################################
# This is base install for Raspberry Pi OS

sudo apt update
sudo apt upgrade -y

# Not always default

sudo apt -y install git gitk emacs zip unzip tree htop btop ruby ripgrep curl x11-utils
sudo bash < <(curl -s https://raw.githubusercontent.com/clojure-lsp/clojure-lsp/master/install)

# BABASHKA
curl -sLO https://raw.githubusercontent.com/babashka/babashka/master/install
chmod +x install
sudo ./install
rm install

 # Needed for installing guest additions on vbox & wireguard on RPI-OS
sudo apt -y install build-essential dkms linux-headers-$(uname -r)

# Install piVpn for wireguard server and wireguard
sudo curl -L https://install.pivpn.io | bash

sudo apt install wireguard wireguard-tools resolvconf -y

# Enable user remote login even after reboot
loginctl enable-linger

# Install Samba file sharing
sudo apt install samba samba-common-bin smbclient cifs-utils -y

# NOTE RPI cannot drive many external HDD
# Install other (most likely) file systems ExFat
#sudo apt install exfat-fuse -y
# Install NTFS (was not on OS 23-feb-26

################################################################################
