################################################################################

echo "# Setting up links to top dotfiles (.alias etc)"

cd ~/
for file in .bash_profile .bashrc .alias .irbrc ;do
    [[ -f $file ]] && mv -f $file $file.org
    ln -s .dotfiles/$file $file
done

# Install latest guthub key
rm -f ./alias_local
gpg -d --pinentry-mode loopback ~/.dotfiles/.alias_local.asc > ~/.alias_local
source ~/.alias_local

# Emacs setup
mkdir ~/.emacs.d
ln -s ~/.dotfiles/init.el ~/.emacs.d/.
ln -s ~/.dotfiles/early-init.el ~/.emacs.d/.
ln -s ~/.dotfiles/lisp ~/.emacs.d/.
echo "" > ~/.emacs.d/custom-vars.el

# Get private ini
cd ~/ && git clone https://gafas66:$token@github.com/gafas66/init

echo "# All files + init set up"

################################################################################
