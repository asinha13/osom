#!/bin/sh

set -e

if [ "$(id -u)" != "0" ]; then
    echo "Please run as root!"
    exit 1
fi

apt-get install -y nginx

install_pkg () {
    f=$1
    tar zxf $f
    for d in */ ; do
        cd $d
        python setup.py install
        cd ..
        rm -rf $d
    done
}

for filename in ./*.tar.gz; do
    echo untar file $filename
    install_pkg $filename
done