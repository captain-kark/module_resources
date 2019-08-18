#!/usr/bin/env bash

source ./scripts/_util.sh

function checkInstall {
    command -v $1 2>&1 > /dev/null
    if [ $? -gt 0 ]; then
        redx "$1 installed"
        printf "\nCheck that ${MAGENTA_TEXT}${1}${CLEAR_TEXT} has been added to your \$PATH, and try again.\n"
        exit 1
    fi

    checkmark "$1 installed"
}

checkInstall git
checkInstall python3.7
checkInstall pip
checkInstall virtualenv
checkInstall pyenv
