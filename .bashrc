# .bashrc
################################################################################

# Use dsc009 as main machine over dsc005 - alternative should be dsc001 or so
# NOTE Be very careful with the sequence of || and && here !
if [[ $(uname -n) == "dsc005" ]] && [[ ! -z ${INSIDE_EMACS+x} ]] ;then
#   tmp=$(mktemp)
#   echo <<EOF > $tmp
#Host dsc009
#   SendEnv INSIDE_EMACS"
#EOF
   #   ssh -F $tmp dsc009
   ssh dsc009
fi
    
source $HOME/.alias
source $HOME/.alias_local

export PATH=${HOME}/bin:${HOME}/.local/bin:${PATH}

export CDPATH=
export CDPATH="$CDPATH:/home/EPI/project/EUPILOT/VEC/usr/esk"
export CDPATH="$CDPATH:/home/EPI/project/STXMOD/users"
alias c="echo \$CDPATH | sed 's/:/\n/g'"

git config --global user.email "ekofoed@gmail.com"
git config --global user.name  "ESK"

# NOTE Avoid silly warnings for commands in need of proper terminal
[[ -z ${INSIDE_EMACS+x} ]] || x=$TERM && export TERM=eterm-color
if command -v module 2>&1 > /dev/null
then
    module use /home/kofoed/modulefiles
    module load prj/vec/1
fi
[[ -z ${INSIDE_EMACS+x} ]] || export TERM=$x && unset x

# EAT SHELL INTEGRATION
[ -n "$EAT_SHELL_INTEGRATION_DIR" ] && source "$EAT_SHELL_INTEGRATION_DIR/bash"

#PROMPT_DIRTRIM=1
PROMPT_COMMAND='\
BRANCH="";\
if git branch &> /dev/null; then \
    BRANCH="git:$(git branch 2> /dev/null | grep \* | cut -d " " -f 2)";\
fi;\
PS1="\h\s \[\033[0;32m\]${BRANCH}\[\033[0m\] \w\n$ ";'

# End
################################################################################
