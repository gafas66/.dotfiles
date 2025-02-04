################################################################################
# This is base install for debian VM

# Not always default
apt -y install git gitk emacs zip unzip tree htop ruby ripgrep

sudo bash < <(curl -s https://raw.githubusercontent.com/clojure-lsp/clojure-lsp/master/install)

curl -sLO https://raw.githubusercontent.com/babashka/babashka/master/install
chmod +x install
./install

 # Needed for installing guest additions on vbox
apt -y install build-essential dkms linux-headers-$(uname -r)

# then open graphic file browser to click on guest-add cdrom to mount it

# cd to mounted cd
#cd ..
sh ./VBoxLinuxAdditions.run

# edit settings.org to refresh packages

emacs # to download all packages

# JDK-8 which seems to work for robocode

echo "deb http://deb.debian.org/debian/ unstable main" > /etc/apt/sources.list.d/debian-unstable.list

# Note these install java & stuff so above is minimal

################################################################################
