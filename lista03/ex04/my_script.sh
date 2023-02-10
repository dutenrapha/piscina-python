#!/bin/bash

python3 -m venv django_venv

mydir=$(cd $(dirname "$0") && pwd)
venv_dir="${mydir}/django_venv/"


tmp_file=$(mktemp)
cat <<EOF >"$tmp_file"
# original bash behavior
if [ -f /etc/bash.bashrc ]; then
    source /etc/bash.bashrc
fi
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi

# activating venv
source "${venv_dir}/bin/activate"

# remove deactivate function:
# we don't want to call it by mistake
# and forget we have an additional shell running
unset -f deactivate

# exit venv shell
venv_deactivate() {
    printf "Exitting virtual env shell.\n" >&2
    exit 0
}
trap "venv_deactivate" SIGUSR1

VIRTUAL_ENV_SHELL_PID=$$
export VIRTUAL_ENV_SHELL_PID

# remove ourself, don't let temporary files laying around
rm -f "${tmp_file}"
pip install -r requirement.txt
EOF

exec "/bin/bash" --rcfile "$tmp_file" -i || {
    printf "Failed to execute virtual environment shell\n" >&2
    exit 1
}

#ref
# https://stackoverflow.com/questions/13122137/how-to-source-virtualenv-activate-in-a-bash-script