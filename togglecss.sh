#!/bin/bash

# Toggle user stylesheet and restart Firefox
# Silas S. Brown 2011, public domain, no warranty

# Where to find history:
# on GitHub at https://github.com/ssb22/css-generator
# and on GitLab at https://gitlab.com/ssb22/css-generator
# and on BitBucket https://bitbucket.org/ssb22/css-generator
# and at https://gitlab.developers.cam.ac.uk/ssb22/css-generator

if ! cd "$HOME/.mozilla/firefox"; then
  echo "Could not find Firefox profiles directory"
  exit 1
fi
export Done=0
for D in *.default; do
  cd "$D/chrome"
  if test -e userContent.css; then
    mv userContent.css userContent.css-disabled
    export Done=1
  elif test -e userContent.css-disabled; then
    mv userContent.css-disabled userContent.css
    export Done=1
  fi
  cd ../..
done
if test $Done == 1; then
  if pidof firefox firefox-bin >/dev/null 2>/dev/null; then
    kill $(pidof firefox firefox-bin) 2>/dev/null
    firefox &
    echo "Stylesheets toggled, Firefox restarted"
  else
    echo "Stylesheets toggled, no current Firefox to restart"
  fi
else
  echo "Could not find any stylesheets to toggle"
  exit 1
fi
