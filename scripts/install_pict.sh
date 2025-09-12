#!/bin/sh

mkdir -p ./ext-systems
cd ./ext-systems

git config --global advice.detachedHead false
git clone --depth 1 --branch release "https://github.com/microsoft/pict.git"
cd pict
make
