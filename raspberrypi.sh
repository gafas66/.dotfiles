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

sudo apt install wireguard wireguard-tools -y

################################################################################
