#!/bin/bash
# sync Accessibility CSS Generator to SVN
wget -N http://people.ds.cam.ac.uk/ssb22/css/css-generate.py
svn commit -m "Update css-generate.py"
