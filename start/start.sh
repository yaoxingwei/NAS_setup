#!/bin/sh
#
# run the shell with root permissions.
#

# 1: install git and config
apt install git
git config --global user.name "yaoxw"
git config --global user.email "yaoxingwei@gmail.com"

# 2: generate ssh key and upload to github
ssh-keygen -t rsa -C "yaoxingwei@gmail.com"

# 3: install samba for share to windows
apt install samba

# 4: edit samba config file

