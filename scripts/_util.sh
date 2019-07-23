#!/usr/bin/env bash

GREEN_TEXT="\033[1;32m"
RED_TEXT="\033[1;31m"
YELLOW_TEXT="\033[33m"
MAGENTA_TEXT="\033[35m"
BLUE_TEXT="\033[36m"
CLEAR_TEXT="\033[0m"

function checkmark { printf "${GREEN_TEXT} ✔ ${CLEAR_TEXT} $1\n"; }
function redx { printf "${RED_TEXT} ✘ ${CLEAR_TEXT} $1\n"; }
