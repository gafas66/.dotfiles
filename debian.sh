################################################################################
# This is base install for debian VM

# Not always default
apt -y install git gitk ruby leiningen emacs

# Needed for installing guest additions on vbox
apt -y install build-essential dkms linux-headers-$(uname -r)

# then open graphic file browser to click on guest-add cdrom to mount it

# cd to mounted cd
#cd ..
sh ./VBoxLinuxAdditions.run

# edit settings.org to refresh packages

emacs # to download all packages

################################################################################
