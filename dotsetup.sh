################################################################################

echo "# Setting up links to top dotfiles (.alias etc)"

ln -s ~/.dotfiles/.alias ~/.
mv -f ~/.bashrc ~/.bashrc_original ;ln -s ~/.dotfiles/.bashrc ~/.
ln -s ~/.dotfiles/.irbrc ~/.
gpg -d ~/.dotfiles/.alias_local.asc > ~/.alias_local

mkdir ~/.emacs.d
ln -s ~/.dotfiles/init.el ~/.emacs.d/.
ln -s ~/.dotfiles/early-init.el ~/.emacs.d/.
ln -s ~/.dotfiles/lisp ~/.emacs.d/.
echo "" > ~/.emacs.d/custom-vars.el

source ~/.alias_local
cd ~/ && git clone https://gafas66:$token@github.com/gafas66/init

echo "# All files + init set up"

################################################################################
