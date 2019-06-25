#!/bin/bash
git pull --no-edit
wget -N http://people.ds.cam.ac.uk/ssb22/css/css-generate.py
git commit -am update && git push
