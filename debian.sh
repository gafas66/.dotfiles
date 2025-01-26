################################################################################
# This is base install for debian VM

# Not always default
apt -y install git gitk emacs

# Needed for installing guest additions on vbox
apt -y install build-essential dkms linux-headers-$(uname -r)

# then open graphic file browser to click on guest-add cdrom to mount it

# cd to mounted cd
#cd ..
sh ./VBoxLinuxAdditions.run

# edit settings.org to refresh packages

emacs # to download all packages

# JDK-8 which seems to work for robocode

wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | sudo apt-key add -

add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/

apt update && sudo apt-get install adoptopenjdk-8-hotspot

# Note these install java & stuff so above is minimal

apt -y install leiningen ruby

################################################################################
