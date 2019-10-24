#!/bin/bash
git pull --no-edit
wget -N http://ssb22.user.srcf.net/css/css-generate.py
git commit -am update && git push
