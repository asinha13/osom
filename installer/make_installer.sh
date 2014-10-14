#!/bin/sh

set -e

NAME="osom-installer"

mydir=$(pwd)
installdir=$mydir"/"$NAME
installpkg=$NAME".tar.gz"
echo $installdir
rm -rf $installdir
mkdir $installdir

cd ..

filename="./installer/products"
tmpfiles=""

while read line
do
    cd $line
    echo "Now in directory $line"
    rm -rf dist/
    rm -rf MANIFEST
    python setup.py sdist
    for tarfile in dist/*.tar.gz; do
        cp $tarfile $installdir
        echo "copying $tarfile"
    done
    cd -
    echo
done < "$filename"

cd $mydir

cp install.sh $installdir
chmod a+x $installdir"/install.sh"
tar czf $installpkg $NAME

echo "The installer package is available at "$installpkg