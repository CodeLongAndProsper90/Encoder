#!/bin/bash


o=$(sed '6q;d' /etc/os-*) 
arr=($(echo $o | tr "=" "\n"))
IFS='='
os=${arr[1]}
IFS=' '


if [ os = "debian" ]; then

sudo apt-get install git python3

else if [ os = "fedora" ]; then

yum install git python3

fi

echo 'Git & Python 3 are installed'

sudo pip3 install colorama
sleep 1
echo 'colorama is installed'
sudo pip3 install random
sleep 1
echo 'random is installed'
sleep 2
echo 'Downloading files'
git clone https://github.com/CodeLongAndProsper90/encode.git
sleep 3
echo 'Download complete'
sleep 0.5s
cd encode

