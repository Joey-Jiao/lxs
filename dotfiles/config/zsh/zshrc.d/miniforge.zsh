export MINIFORGE_HOME="${MINIFORGE_HOME:-$HOME/.local/miniforge}"
export MAMBA_ROOT_PREFIX="$MINIFORGE_HOME"

if [[ -d "$MINIFORGE_HOME" ]]; then
    __conda_setup="$("$MINIFORGE_HOME/bin/conda" 'shell.zsh' 'hook' 2>/dev/null)"
    if [[ $? -eq 0 ]]; then
        eval "$__conda_setup"
    elif [[ -f "$MINIFORGE_HOME/etc/profile.d/conda.sh" ]]; then
        source "$MINIFORGE_HOME/etc/profile.d/conda.sh"
    fi

    if [[ -f "$MINIFORGE_HOME/etc/profile.d/mamba.sh" ]]; then
        source "$MINIFORGE_HOME/etc/profile.d/mamba.sh"
    fi
fi

unset __conda_setup
