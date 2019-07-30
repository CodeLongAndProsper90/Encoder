#!/bin/bash


o=$(sed '6q;d' /etc/os-*) 
arr=($(echo $o | tr "=" "\n"))
IFS='='
os=${arr[1]}
IFS=' '


if [ os = "debian" ]; then

sudo apt-get install git python3

else

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
echo 'Move to the directory `encode`, then run the command \"alias encode="python3 ~/encode.py && encode\". After that, you can just ues encode to run it until the next reboot.'
sleep 5s
