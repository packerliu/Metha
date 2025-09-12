#!/bin/sh

mkdir -p ./ext-systems
cd ./ext-systems
git config --global advice.detachedHead false
git clone --depth 1 --branch v2020.12.23 "https://github.com/batfish/batfish.git"
cd batfish
sed -i 's/\$(lsb_release -rs)/16.04/g' tools/install_z3.sh
tools/install_z3.sh
#cd /root/ext-systems/batfish
#source tools/batfish_functions.sh
#batfish_build_all
