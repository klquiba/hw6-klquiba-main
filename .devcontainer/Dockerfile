############################################################################
##        Base image

ARG VARIANT="3.11-bullseye"
FROM mcr.microsoft.com/devcontainers/python:0-${VARIANT}

# [Optional] Uncomment this section to install additional OS packages.
#   gawk: For convenience (mkzip.sh), even though not needed by students
#   vim: Default editor (for commit messages from git commandline)
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends gawk vim-nox \
#     && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# [Add-on; Optional] Uncomment this section to install latest fzf release
# COPY .devcontainer/install-fzf.sh /tmp/install-fzf.sh
# RUN /bin/bash /tmp/install-fzf.sh && rm -f /tmp/install-fzf.sh


############################################################################
##        VSCode user -- additional setup

ARG USERNAME="vscode"
USER ${USERNAME}:${USERNAME}

ARG VENV_PATH="/home/${USERNAME}/venv"

# Create virtualenv and install required packages (via pip)
COPY --chown=${USERNAME}:${USERNAME} requirements.txt requirements-dev.txt /tmp/pip-tmp/
RUN python -m venv /home/vscode/venv \
    && ${VENV_PATH}/bin/pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt -r /tmp/pip-tmp/requirements-dev.txt \
    && rm -rf /tmp/pip-tmp

# [Add-on] Install zsh-autosuggestions plugin
RUN git clone https://github.com/zsh-users/zsh-autosuggestions /home/${USERNAME}/.oh-my-zsh/custom/plugins/zsh-autosuggestions

# [Add-on] Tweak zsh configuration
# RUN sed -i -E 's/^ZSH_THEME=.*$/ZSH_THEME="agnoster"/g' /home/${USERNAME}/.zshrc
RUN sed -i -E 's/^plugins=.*$/plugins=(git zsh-autosuggestions)/g' /home/${USERNAME}/.zshrc \
    && sed -i -E 's/^# (zstyle '"'"':omz:update'"'"' mode disabled.*)$/\1/g' /home/${USERNAME}/.zshrc
