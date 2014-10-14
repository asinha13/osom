#!/bin/sh

set -e

NAME="osom-installer"

./make_installer.sh
cd $NAME
sudo ./install.sh
cd -