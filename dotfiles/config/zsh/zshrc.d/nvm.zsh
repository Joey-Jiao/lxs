export NVM_DIR="$HOME/.local/nvm"

if [[ -d "$NVM_DIR" ]]; then
    [[ -s "$NVM_DIR/nvm.sh" ]] && source "$NVM_DIR/nvm.sh"
    [[ -s "$NVM_DIR/bash_completion" ]] && source "$NVM_DIR/bash_completion"
fi
