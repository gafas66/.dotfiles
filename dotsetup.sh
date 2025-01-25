################################################################################

echo "Setting up links to top dotfiles (.alias etc)"

ln -s ~/.dotfiles/.alias ~/.
mv -f ~/.bashrc ~/.bashrc_original ;ln -s ~/.dotfiles/.bashrc ~/.
ln -s ~/.dotfiles/.irbrc ~/.
gpg -d ~/.dotfiles/.alias_local.asc > ~/.alias_local

mkdir ~/.emacs.d
ln -s ~/.dotfiles/init.el ~/.emacs.d/.
ln -s ~/.dotfiles/lisp ~/.emacs.d/.
touch ~/.emcacs.d/custom-vars.el

echo "NB! ~/init needs to be cloned as org files are there"
