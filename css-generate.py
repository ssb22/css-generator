#!/usr/bin/env python
prog="Accessibility CSS Generator, (c) Silas S. Brown 2006-16.  Version 0.9853"

# This program is free software; you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published by 
# the Free Software Foundation; either version 3 of the License, or 
# (at your option) any later version. 
#
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
# GNU General Public License for more details. 

# CHANGES
# -------
# If you want to compare this code to old versions, the old
# versions are being kept in the E-GuideDog SVN repository on
# http://svn.code.sf.net/p/e-guidedog/code/ssb22/css-generator
# as of v0.9782.  Versions prior to that were not kept, but
# you might be able to find some on Internet Archive.
# To check out the repository, you can do:
# svn co http://svn.code.sf.net/p/e-guidedog/code/ssb22/css-generator

# CONFIGURATION
# -------------

# The default configuration can be changed here, or if you
# prefer you can copy and paste all of this to a separate
# file called css_generate_config.py and edit it there
# (which should make it easier to update the code
# independently of your configuration).

# Where to put the output CSS files: default is current directory,
# but you might want to put them in a subdirectory, or set
# an absolute path
outputDir = "."

# Whether to write an HTML menu to standard output as well
# (see my CSS page for example)
outHTML = True
# if putting this on the Web, include in .htaccess:
# AddType text/css css
# SetEnvIf Request_URI "\.css$" requested_css=css
# Header add Content-Disposition "Attachment" env=requested_css

# Which pixel sizes to generate.
# Size 0 means "unchanged" - it will disable the size
# changes, and the layout changes that are meant for large
# sizes.  This is for people who need only colour changes.
pixel_sizes_to_generate = [0,18,20,25,30,35,40,45,50,60,75,100]

# Which pixel size to use with the "chop" and related debug options:
chop_pixel_size = 20

# Which colour schemes to generate.  The format of this is
# [("description","filename-prefix",{...}),...]
# - see the existing ones for examples.
# If you have many of these, you might want to read them
# in from separate configuration files instead of listing
# them here.  In that case, set colour_schemes_to_generate
# to a string containing a wildcard,
# e.g. colour_schemes_to_generate = "my_config_dir/*.conf"
# in which case each file in my_config_dir/*.conf should
# contain one or more entries in the same [(...),...] format
# WARNING: this will be passed to Python's eval() function
# which can execute any command, so don't allow an
# untrusted third party to write these *.conf files.

colour_schemes_to_generate = [
  ("yellow on black","",
   {"text":"yellow","background":"black",
    "headings":"#8080FF","link":"#00FF00",
    "hover":"#0000C0","visited":"#00FFFF",
    "bold":"#FFFF80","italic":"white",
    "coloured":"pink", # used for text inside any FONT COLOR= markup
    "button":"#600040",
    "selectbox":"#600060",
    "reset_button":"#400060",
    "form_disabled":"#404040", # GrayText requires CSS 2.1
    "selection":"#006080", # (if supported by the browser. BEWARE: Some browsers, e.g. Safari 6, will NOT display this exact colour, but a computed medium mid-way between it and the unselected background; you should therefore ensure that other backgrounds (e.g. highlight) are discernable against those 'computed medium' colours as well)
    "highlight":"#300030", # (misc non-selection highlights in site-specific hacks)
    "image_transparency_compromise":"#808000" # non-black and non-white background for transparent images, so at least stand a chance of seeing transparent imgs that were meant for white bkg (or black bkg)
    }),
  
  ("green on black","green",
   {"text":"#00FF00","background":"black",
    "headings":"#40C080","link":"#0040FF",
    "hover":"#400000","visited":"#00FFFF",
    "bold":"#80FF80","italic":"white",
    "button":"#600040",
    "selectbox":"#600060",
    "coloured":"#80C040",
    "reset_button":"#400060",
    "form_disabled":"#404040",
    "selection":"#4000c0",
    "highlight":"#003050",
    "image_transparency_compromise":"#808000"
    }),
  
  ("white on black","WonB",
   {"text":"white","background":"black",
    "headings":"#40C090","link":"#0080FF",
    "hover":"#400000","visited":"#00FFFF",
    "bold":"yellow","italic":"#FFFF80",
    "button":"#600040",
    "selectbox":"#600060",
    "coloured":"#FFFF40",
    "reset_button":"#400060",
    "form_disabled":"#404040",
    "selection":"#4080c0",
    "highlight":"#003050",
    "image_transparency_compromise":"#808080"
    }),
  
  ("soft greys","soft", # c.f. Nightshift etc; thanks to Liviu Andronic for testing
   {"text":"#C0C0C0","background":"#383838",
    "alt-backgrounds":["#333333","#2E2E2E"], # optional
    "headings":"#40C090","link":"#BDB76B",
    "hover":"#453436","visited":"#B6AA7B",
    "bold":"#CD853F","italic":"#EFEFCF",
    "button":"#553030",
    "selectbox":"#603440",                              
    "coloured":"#E0E040",
    "reset_button":"#303055",
    "form_disabled":"#555753",
    "selection":"#5f5f5f",
    "highlight":"#2e3050",
    "focusOutlineStyle":"solid #006080",
    "image_opacity":0.8,
    "image_transparency_compromise":"#2e3436"
  }),

  ("black on linen","BonL", # LyX's background colour is "linen", 240/230/220
   {"text":"black","background":"#faf0e6",
    "headings":"#404040","link":"#0000FF",
    "hover":"#80C0C0","visited":"#008020",
    "bold":"black","italic":"#400000",
    "button":"#608040",
    "selectbox":"#608060",
    "coloured":"#001040",
    "reset_button":"#408060",
    "form_disabled":"#A0A0A0",
    "highlight":"#FFFFE6",
    "image_transparency_compromise":"#faf0e6"
    }),
  
  ("black on white","BonW", # cld call this "black on bright white" (as opposed to "black on linen white") but that causes the list to take up more width
   {"text":"black","background":"white",
    "headings":"#404040","link":"#0000FF",
    "hover":"#80C0C0","visited":"#008020",
    "bold":"black","italic":"#400000",
    "button":"#608040",
    "selectbox":"#608060",
    "coloured":"#001040",
    "reset_button":"#408060",
    "form_disabled":"#A0A0A0",
    "highlight":"#FFFF80",
    "image_transparency_compromise":"white"
    }),
  ]

# Some other options you might want to change:
separate_adjacent_links_at_size_0 = False # sometimes interferes with layouts
separate_adjacent_links_at_other_sizes = True

# Fonts: (cjk_fonts is listed first so it can be used in both serif_fonts and sans_serif_fonts)
cjk_fonts = "Lantinghei SC, AppleGothic"
# AppleGothic must be listed or Korean is broken on Mac OS 10.7
# Lantinghei SC was introduced to OS X in 10.9, which is handy because the previously-good STSong font (which was the system default for Simplified Chinese) broke on 10.9: it renders badly with antialiasing turned off at 20px, e.g. missing the horizontal stroke on U+95E8.  So we set Lantinghei SC for 10.9 but fall back to STSong on 10.8/10.7/etc (I don't think we need to explicitly say STSong, and there are advantages in not doing so, e.g. the TODO below about :lang(ja) is not relevant for pre-10.9 systems)
# TODO: for :lang(ko) and :lang(ja) we had better put AppleGothic and a Japanese font like YuGothic first (before Lantinghei) - see below re U+8D77, U+95E8 etc.  Pity can't read the system preferences for pages that don't set a CJK value of LANG.  This :lang exception needs to be done separately for every element that has a font-family, to avoid corrupting headings etc.
# Other Mac CJK fonts to be aware of: MingLiU prefers full 'Traditional' forms of characters where Trad/Simp has same Unicode value (e.g. U+8D77 'qi3' has an extra vertical stroke making the 'ji' component look more like a 'si'); renders OK on Mac OS 10.9 at 20px without antialias, but might not always be present (the ttf is installed to /Library/Fonts/Microsoft by MS Office and is not present on machines without MS Office).  Arial Unicode MS (present on both 10.7 and 10.9) has some issues with baselines not lining up e.g. in the word 'zhen1li3' U+771F U+7406; it prefers Simplifed Chinese forms (e.g. U+8D77 uses 'ji', and U+95E8 is the Chinese rather than the Japanese simplification).  GB18030 Bitmap (NISC18030) might work at 16px, 32px etc, but scales badly to other sizes.  "Hei" has irregular stroke widths in 10.9 20px no-antialias, but otherwise OK
serif_fonts = "Times New Roman, times, utopia, /* charter, */ "+cjk_fonts+", serif" # TNR is listed first for the benefit of broken Xft systems that need the MS fonts to make them look OK. Shouldn't have any effect on other systems.
sans_serif_fonts = "helvetica, arial, verdana, "+cjk_fonts+", sans-serif" # (TODO: do we want different cjk_fonts here?)

# ---- End of options (but read on for debugging) ----

# DEBUGGING BY BINARY CHOP: If a complex stylesheet exhibits
# a behaviour you weren't expecting (maybe due to a browser
# bug but maybe not) then it might not be obvious how to fix
# it.  This program has a debug mode that helps you do it by
# binary chop.  Run like this:
#    python css-generate.py chop
# which will generate a single debug .css file with half
# the attributes disabled.  Try that debug .css; if the
# problem persisted, then do
#    python css-generate.py chop 1
# or if the problem did not persist, do
#    python css-generate.py chop 0
# and then try again.  Then add another 1 or 0 depending on
# whether or not the problem persisted the next time, e.g.
#    python css-generate.py chop 01
# Hopefully it will narrow down the problem to one thing.
# You will see which one that is from the debug messages
# it prints on standard output (these will appear instead of
# the HTML index of stylesheets that is usually generated).

# For more desperate debugging cases, you can try:
#    python css-generate.py desperate-debug
# which will generate a large number of stylesheets, each
# adding one more rule and not combining.  (Note that some
# rules at the beginning and end of the stylesheet will be
# there unconditionally though.)

# TODO consider forcing "display" to its normal value (not "none")
# if some sites are going to use stock scripts that switch them on and
# off every few seconds inadvertently making the rest of the page dance around

# ---- End of debugging info, code follows ----

try: from css_generate_config import *
except ImportError: pass
if type(colour_schemes_to_generate) in (str,unicode):
  import glob
  colour_schemes_to_generate = reduce(lambda x,y:x+eval(open(y).read()), glob.glob(colour_schemes_to_generate), [])

def do_one_stylesheet(pixelSize,colour,filename,debugStopAfter=0):
  outfile = open(outputDir+os.sep+filename,"w")
  smallestHeadingSize = pixelSize*5.0/6.0
  largestHeadingSize = pixelSize*10.0/6.0

  # In the settings below, beginning with * means it will
  # be omitted from the "pixelSize 0" option (i.e. leave
  # site's size/layout alone and just changing colours)
  defaultStyle={
    "*font-family":serif_fonts,
    "*font-size":"%.1fpx" % pixelSize,
    "color":colour["text"],
    "background":colour["background"], # background-color is handled by aliases
    # We have to specify more or less everything even if
    # it's OK by default, otherwise a web author's
    # stylesheet may override the default and cause a
    # not-so-good author/user stylesheet combination.
    "*font-style":"normal",
    "*font-weight":"normal",
    "*font-variant":"normal",
    "*font-size-adjust":"none",
    "background-image":"none",
    "*letter-spacing":"normal",
    "*line-height":"normal",
    "*width":"auto",
    "*height":"auto",
    "*border-width":"0.05em",
    "*border-radius":"0.05em",
    "*-moz-border-radius":"0.05em",
    "*-webkit-border-radius":"0.05em",
    "*-webkit-font-smoothing":"none", # font smoothing doesn't work so well on large-print low-resolution dark-background displays...
    "*-moz-osx-font-smoothing":"auto","*font-smooth":"never", # -moz-osx-font-smoothing overrides font-smooth on Firefox 25+; "never" would be better, but at least Ffx 29 doesn't support it and falls back to the SITE's spec :-( (greyscale is worse than auto in large print low resolution)
    "*-webkit-text-stroke":"0",
    "*position":"static",
    "*visibility":"visible /* because we're forcing position to static, we must also force visibility to visible otherwise will get large gaps.  Unfortunately some authors use visibility:hidden when they should be using display:none, and CSS does not provide a way of saying '[visibility=hidden] {display:none}' */",
    "*float":"none","*clear":"none",
    "*min-height":"0px",
    "*max-height":"none",
    "*max-width":"none", # see comments below on "max-width"
    "*min-width":"0px",
    "*text-decoration":"none",
    "text-shadow":"none",
    "*text-align":"left /* not full justification */",
    "*margin":"0px",
    "*padding":"0px",
    "*text-indent":"0px",
    "*white-space":"normal /* don't \"nowrap\" */",
    "*cursor":"auto",
    "*overflow":"visible", # the default.  NOT "auto" - it may put the scroll bar of a table off-screen at the bottom.  If (e.g.) "pre" overflows, we want the whole window to be scrollable to see it.
    
    "*filter":"none","*-webkit-filter":"none","*-moz-filter":"none","*-o-filter":"none","*-ms-filter":"none",
    "*opacity":"1",
    "*-moz-opacity":"1",
    
    "-moz-appearance":"none", # DON'T * this, it can lead to white-on-white situations so we need it for colour changes not just size changes

    "*-webkit-hyphens":"manual", # auto hyphenation doesn't always work very well with our fonts (TODO: manual or none?  manual might be needed if devs put breakpoints into very long words)
    "*-moz-hyphens":"manual",
    "*-ms-hyphens":"manual",
    "*hyphens":"manual",
    "*table-layout":"auto",
    "user-select":"text","-moz-user-select":"text","-webkit-user-select":"text", # don't allow making things non-selectable, as selection might help keep track of things (TODO: still have user-select:none for buttons etc?)
    "*flex-basis":"auto", # giant print or small windows can cause long words to overflow 'flex' layouts that specify small pixel widths, so set "auto" instead
    }
  for css3Thing,value in [
      # Get rid of "flip boxes"...
      ("transform","none"),
      ("transform-style","flat"),
      ("backface-visibility","visible"),
      ("transition-property","none")]:
    for browser in ["",'-o-','-ms-','-moz-','-webkit-']:
      defaultStyle['*'+browser+css3Thing] = value

  # have to explicitly set for every type of element,
  # because wildcards don't always work and inheritance can
  # be overridden by author stylesheets resulting in poor
  # combinations.  NB however we don't list ALL elements in
  # mostElements (see code later).
  mostElements="a,blockquote,caption,center,cite,code,col,colgroup,html,iframe,pre,body,div,p,input,select,option,textarea,table,tr,td,th,h1,h2,h3,h4,h5,h6,font,basefont,small,big,span,ul,ol,li,i,em,s,strike,nobr,tt,samp,kbd,b,strong,dl,dt,dd,blink,button,address,dfn,form,marquee,fieldset,legend,listing,abbr,q,menu,dir,multicol,img,plaintext,xmp,label,sup,sub,u,var,acronym,object,embed,canvas,video".split(",")
  html5Elements = "article,aside,bdi,command,details,summary,figure,figcaption,footer,header,hgroup,main,mark,meter,nav,progress,section,time,del,ins,svg,output,thead,tbody".split(",")
  rubyElements = "ruby,rt,rp,rb".split(",") # NOT counted in mostElements
  html5Elements += ['text','text > tspan'] # used within svg, sometimes for nothing more than effect (unfortunately there doesn't seem to be a way of ensuring the containing svg is displayed large enough, but truncation is better than having the text go underneath other elements)
  mostElements += html5Elements
  mostElements += ['location'] # site-specific hack for lib.cam.ac.uk

  # Selector prefixes to exclude certain browsers from trying to implement a rule:
  exclude_ie_below_7 = "html > "
  exclude_ie_below_8 = "html >/**/ body "
  exclude_ie_below_9 = ":not(:empty) " # IE8 (and non-CSS3 browsers) don't support :not
  
  css={} ; printOverride = {}
  webkitScreenOverride = {} ; geckoScreenOverride = {}
  webkitGeckoScreenOverride = {}
  for e in mostElements+rubyElements:
    css[e]=defaultStyle.copy()
    printOverride[e] = {"color":"black","background":"white"}.copy()
    if pixelSize: printOverride[e]["font-size"] = "12pt" # TODO: option?

  # but there are some exceptions:

  for e in rubyElements:
    del css[e]["*text-align"] ; del css[e]["*line-height"]

  for t in ["textarea","html","body","input"]:
    css[t]["*overflow"] = "auto"
  # 'html' is there for IE7.  But Firefox needs it to be 'visible'.  See hack at end.
  # TODO previously excluded 'body' (and deleted 'body' overflow 'visible')
  # as it somehow disables keyboard scrolling in IE7, however do need to
  # set 'body' to "auto' to work around CouchDB's "overflow:none" in both
  # 'html' and 'body' (at least in Firefox); need to find an IE7 to re-test
  # (if broken, consider re-instating the delete and move body:auto to the
  # non-IE7 override hack at end)
  # del css["body"]["*overflow"] # Do not set both "body" and "html" in IE7 - it disables keyboard-only scrolling!
  del css["input"]["*overflow"] # for IE 6 and possibly 8 overprinting too-long input type="text" with a horizontal scrollbar

  for e in ["object","embed","img"]:
    del css[e]["*width"], css[e]["*height"] # object/embed should not be forced to 'auto' as that can sometimes break Flash applications (when the Flash application is actually useful), and if img is 'auto' then that can break on some versions of IE
  css[exclude_ie_below_9+"img"]={"*width":"auto","*height":"auto"} # but we can at least add it back on other browsers (TODO: which versions of IE were affected?) - we DO need to specify this, to cope with sites that do silly things like set image height to something e+7 pixels and expect layering to compensate

  css["textarea"]["*width"]="100%" # not "auto", as that can cause Firefox to sometimes indent the textarea's contents off-screen

  css["frame"]={}
  for e in ["frame","iframe"]: css[e]["*overflow"]="auto" # to override 'scrolling=no' which can go wrong in large print (but this override doesn't always work)

  css["sup"]["*vertical-align"] = "super /* in case authors try to do it with font size instead */"
  css["sub"]["*vertical-align"] = "sub"

  css["marquee"]["*-moz-binding"]="/* make sure firefox doesn't scroll marquee elements */ none"
  css["marquee"]["*display"]="block"

  css["center"]["*text-align"] = "center"
  
  for s in ['s','strike']: css[s]["*text-decoration"]="line-through"
  # TODO: not sure if really want this for the 's' alias of 'strike', since some sites e.g. http://www.elgin.free-online.co.uk/qp_intro.htm (2007-10) use CSS to override its presentation into something other than strikeout
  css['span[style="text-decoration:line-through"],span[style="text-decoration:line-through;"]']={"*text-decoration":"line-through"} # used on some sites

  # Margin exceptions:

  css["body"]["*margin"]="/* keep away from window borders */ 1ex %.1fpx 1ex %.1fpx" % (pixelSize*5/18.0,pixelSize*5/18.0)

  for i in "p,multicol,listing,plaintext,xmp,pre".split(","): css[i]["*margin"]="1em 0"
  
  listStuff="ul,dir,menu,dl,li".split(",") # not ol, leave that as margin 0px - see ol > li below
  for l in listStuff:
    css[l]["*margin"]="0 1em 0 %.1fpx" % (pixelSize*10/18.0)
  listStuff.remove("li")
  for l in listStuff:
    for l2 in listStuff:
      css[l+" "+l2]={"*margin":"0px"}
  css["ol > li"] = {"*list-style-position":"inside","*margin":"0px","*padding-left":"1em","*text-indent":"-1em"} # helps when numbers get very large
  css["blockquote"]["*margin"]="1em 4em"
  css["blockquote[type=cite]"]={"*margin":"1em 0px","*padding":"1em 0px 0px 0px"}
  css["dd"]["*margin"]="0em 2em"
  
  for t in ["th","td"]:
    css[t]["*padding"]="%.1fpx" % (pixelSize/18.0,)
    css[t+'[align^="right"]'] = {"*text-align":"right"}
  
  # Don't say white-space normal on user input elements or pre
  # Galeon 1.25: we also have to exclude "body" and "div" for some reason
  # TODO: is it REALLY a good idea to leave 'div' on this list?
  for e in "pre,input,textarea,body,div".split(","): del css[e]["*white-space"]
  for e in "font,code".split(","): css["pre "+e]={"*white-space":"inherit"} # some mailing lists etc have "font" within "pre", and some sites have "code" within "pre"
  
  # Monospaced elements
  for t in "pre,code,tt,kbd,var".split(","): css[t]["*font-family"]="monospace"
  # and 'samp' let's have sans-serif
  for t in "samp".split(","): css[t]["*font-family"]=sans_serif_fonts
  
  css["spacer"]={"*display":"none"} # no point in keeping the spacers now we've changed the layout so much
  css["a"]["*display"] = "inline" # some sites override it to block, which might have worked OK in their CSS's context but it's not so good in ours

  # max-width (if supported, i.e. not IE6) can reduce left/right scrolling -
  # if one line's linebox needs to expand (e.g. due to a long word), then we
  # don't want to expand the whole block (e.g. the table cell) and all its
  # other line boxes.  BUT: if a max-width'd TD (or even a DIV etc) does
  # have to overflow in a big way (e.g. due to map images), and there is
  # something else to the right (e.g. nested tables with rowspans),
  # overprinting can result, unless also using 'overflow:auto' which can
  # create too many nested or offscreen scrollbars.  No way to say "use this
  # width for internal formatting, then expand to overflows for external
  # bounds" or "use this width if you are a leaf node with mostly text" or
  # whatever.  Only alternative for now is to say "none" and have to
  # horizontally scroll.  (Even "p" is not safe to set - consider a
  # table containing a p containing another table that overflows.)
  # (If set td max-width to "-moz-available" later in the stylesheet, will
  # cause Firefox 3 to do less overprinting than it would have done while
  # Firefox 2 takes the previous one and does a better job incorrectly, but
  # then there are still some instances of overprinting regardless of
  # version etc., especially on mapping sites)
  
  # (Note: On Firefox 2 (not 3), max-width works in a nice way, see Bugzilla
  # bug report at https://bugzilla.mozilla.org/show_bug.cgi?id=452840 - so
  # you may want to uncomment the following if you are particularly on Firefox 2.)
  
  # for e in mostElements: css[e]["*max-width"]=("%.1fpx" % min(1200,pixelSize*470/18))

  # Links stuff - must be before bold/italic colour overrides:
  for linkInside in ",font,big,small,basefont,br,b,i,u,em,strong,abbr,span,div,code,tt,samp,kbd,var,acronym,h1,h2,h3,h4,h5,h6".split(",")+rubyElements:
    for type in [":link",":visited","[onclick]",
                 ".button", # used by some JS applications
                 ]:
      css["a"+type+" "+linkInside]={"color":colour["link"],"text-decoration":"underline","cursor":"pointer"}
      printOverride["a"+type+" "+linkInside]={"color":"#000080"} # printing: links in blue might be useful for sending PDFs to others, but make it a dark blue so still readable if printed in black and white (don't try to ensure page is ALWAYS black and white: that can't be done w/out suppressing images.  User needs to suppress colour at print time.  But ensure legible choice of shading when that happens.)
      css["a"+type+":hover "+linkInside]={"background":colour["hover"]}
      css["a"+type+":active "+linkInside]={"color":"red","text-decoration":"underline","cursor":"pointer"}
      if linkInside in ["b","i","em","u","strong"] and not css[linkInside]["color"]==colour["text"]: css["a"+type+" "+linkInside]["color"]=css[linkInside]["color"]
    css["a:visited "+linkInside]["color"]=colour["visited"]
  # set cursor:pointer for links and ANYTHING inside them (including images etc).  The above cursor:auto should theoretically do the right thing anyway, but it seems that some versions of Firefox need help.
  for linkInside in mostElements+rubyElements:
    for type in [":link",":visited","[onclick]"]:
      key="a"+type+" "+linkInside
      if not css.has_key(key): css[key]={}
      css[key]["cursor"]="pointer"
      if not linkInside in rubyElements: css[key]["*display"]="inline" # some sites have 'div' or do JS things with 'span'...

  # Italic and bold:
  for i in "i,em,cite,address,dfn,u".split(","):
    css[i+" span"]={
      "*font-family":sans_serif_fonts,
      "color":colour["italic"]}
    printOverride[i+" span"]={"color":"black"}
    css[i].update(css[i+" span"])
  for i in "b,strong".split(","):
    css[i+" span"]={
      "*font-weight":"bold",
      "color":colour["bold"]}
    printOverride[i+" span"]={"color":"black"}
    css[i].update(css[i+" span"])
  css["acronym"]["color"]=colour["bold"]
  css["abbr"]["color"]=colour["bold"]
  # Some browsers might start styling abbr by default but not acronym.  Some older browsers might understand acronym title= but not abbr title=, so some sites might try to use acronym= for backward compatibility, but given that this must be for nonessential information anyway (as many simpler browsers don't support either) it probably makes sense to prefer abbr now (if it might be displayed by default on a greater number of modern browsers) unless the webmaster wants to emulate the browser in CSS.
  css["acronym"]["border-bottom"]="1px dotted"
  css["abbr"]["border-bottom"]="1px dotted"

  # Headings stuff (must be after italic/bold):
  indent = 0
  for h in range(6):
    el="h%d" % (h+1)
    css[el]["*font-family"]=sans_serif_fonts
    size = (largestHeadingSize-h*(largestHeadingSize-smallestHeadingSize)/(6-1.0))
    css[el]["*font-size"]="%.1fpx" % size
    css[el]["*font-weight"]="bold"
    # ensure 'h1 strong' etc inherits family (but not necessarily colour):
    for i in ['strong','em','i','b']:
      css[el+" "+i]=css[el].copy()
      css[el+" "+i]["color"]=css[i]["color"]
      printOverride[el+" "+i]={"color":"black"}
    # now for heading colour:
    css[el]["color"]=colour["headings"]
    printOverride[el]={"color":"black"}
    # ensure links in headings inherit size and family:
    css[el+" center"]=css[el].copy() # rather than the default for 'center'
    css[el+" a"]=css[el].copy() # because it's usually A NAME (in the case of HREF, the specificity of a:link should be greater)
    css[el+" abbr"]=css[el].copy() ; del css[el+" abbr"]["*text-decoration"]
    css[el+" span"]=css[el].copy()
    css[el+" a b"]=css[el].copy()
    printOverride[el+" center"]=printOverride[el].copy()
    printOverride[el+" a"]=printOverride[el].copy()
    printOverride[el+" abbr"]=printOverride[el].copy()
    printOverride[el+" span"]=printOverride[el].copy()
    printOverride[el+" a b"]=printOverride[el].copy()
    # and now (AFTER the above) set margins on headings
    if h: indent += size
    css[el]["*margin"]="0px 0px 0px %.1fpx" % indent

  # Images and buttons:
  css["img"]["background"]=colour["image_transparency_compromise"]
  
  # Exception needed for MediaWiki TeX images
  # (they tend to be transparent but with antialiasing that
  # assumes the background will be white)
  css["body.mediawiki img.tex"]={"background":"white"}
  # (note however it might be possible to set the wiki to
  # display maths as real TeX or something instead)
  if not colour["background"]=="white": css["body.mediawiki img.tex"]["border"]="white solid 3px" # to make sure letters near the edge are readable if the rest of the page has a dark background
  
  if "image_opacity" in colour:
    del css["img"]["*opacity"],css["img"]["*-moz-opacity"],css["img"]["*filter"]
    css["img"]["opacity"]=css["img"]["-moz-opacity"]="%g" % colour["image_opacity"]
    css["img"]["filter"]="alpha(opacity=%d)" % int(colour["image_opacity"]*100) # for IE8 and below
    if colour["image_opacity"]<0.9: css["img:hover"] = css["a:hover img"]={"opacity":"0.9","-moz-opacity":"0.9","filter":"alpha(opacity=90)"}
  
  css["button"]["background"]=colour["button"]
  printButtonBackground = "#e0e0e0" # light grey, TODO: option
  printOverride["button"]["background"]=printButtonBackground
  css['div[role="button"]']={"background":colour["button"]} # for Gmail 2012-07 on "standard" view (rather than "basic HTML" view).  "Standard" view might work for people who want the "unchanged" size.
  printOverride['div[role="button"]']={"background":printButtonBackground}
  if "alt-backgrounds" in colour:
    # override specificity of alt-backgrounds div:nth-child
    css['html body div[role="button"]'] = css['div[role="button"]']
    printOverride['html body div[role="button"]'] = {"background":printButtonBackground}
  css["input[type=submit]"]={"background":colour["button"]}
  css["input[type=button]"]={"background":colour["button"]}
  css["input[type=reset]"]={"background":colour["reset_button"]}
  printOverride["input[type=submit]"]={"background":printButtonBackground}
  printOverride["input[type=button]"]={"background":printButtonBackground}
  printOverride["input[type=reset]"]={"background":printButtonBackground}
  for f in ["select","input","textarea","button"]:
    k = "html "+f+'[disabled]' # must include 'html' so more specific than above (TODO: or :not(:empty) if got enough CSS?)
    css[k]={"background":colour["form_disabled"]}
    printOverride[k]={"background":printButtonBackground} # TODO: or something else?
  
  # Separate adjacent links (CSS2+)
  if (pixelSize and separate_adjacent_links_at_other_sizes) or (not pixelSize and separate_adjacent_links_at_size_0):
    for l in [":link",":visited","[onclick]"]:
      css[exclude_ie_below_9+"a"+l+":before"]={"content":'"["',"color":colour["text"],"text-decoration":"none","white-space":"nowrap"}
      css[exclude_ie_below_9+"a"+l+":after"]={"content":'"]"',"color":colour["text"],"text-decoration":"none","white-space":"nowrap"}
      # make sure the hover colour includes :before and :after - this is needed if the :before/:after text is changed by site-specific hacks etc (to cope with empty links)
      css[exclude_ie_below_9+"a"+l+":hover:before"]={"background":colour["hover"]}
      css[exclude_ie_below_9+"a"+l+":hover:after"]={"background":colour["hover"]}
      printOverride[exclude_ie_below_9+"a"+l+":before"]={"color":"black"} # TODO: option to delete the "[" "]" content also?
      printOverride[exclude_ie_below_9+"a"+l+":after"]={"color":"black"}
      
  # Avoid style overrides from :first-letter, :first-line,
  # :before and :after in author's CSS.  However be careful
  # which elements you do this because of browser bugs.
  firstLetterBugs_multiple=[
  "input","select","option","textarea","table","colgroup","col","img", # probably best to avoid these
   "div", # Gecko messes up textarea when enter multiple paragraphs; Safari has text selection visibility problem see below
  ]
  firstLetterBugs_geckoOnly=[
    # none here for now
  ]
  firstLetterBugs_webkitOnly=[
  # The following cause text selection visibility problems in Webkit / Safari 5/6 (cannot be worked around with :first-letter::selection)
  # (+ Chrome 12 bug - OL/LI:first-letter ends up being default size rather than css size; harmless if have default size set similarly anyway)
  "label","address","p","ol","ul","li","pre","code","body","html","h1","h2","h3","h4","h5","h6","form","th","tr","td","dl","dt","dd","b","blockquote","section","header","center","article","span","aside","figure","figcaption","time"
  ]
  firstLetterBugs_other=[
  "a", # causes problems in IE
  ]
  assert not(any(x in firstLetterBugs_geckoOnly or x in firstLetterBugs_webkitOnly or x in firstLetterBugs_other for x in firstLetterBugs_multiple) or any(x in firstLetterBugs_webkitOnly or x in firstLetterBugs_other for x in firstLetterBugs_geckoOnly) or any(x in firstLetterBugs_other for x in firstLetterBugs_webkitOnly)), "Error: firstLetterBugs item in more than one category"
  firstLineBugs=[
  "div", # on firefox 2 causes some google iframes to occlude page content
  "input","select","option","textarea","table","colgroup","col","img",
  "td","th", # causes problems on Firefox 2 if there's a form inside
  "a", # causes problems in IE
  "span", # sometimes causes crashes in Opera 12
  "li", # sometimes causes crashes in Opera 12 (note this might be sacrificing some control, if someone does try a li:first-line override)
  # To be safe, could add other inline-etc tags mentioned in mostElements:
  "label","nobr","tr","ol","ul","abbr","acronym","dfn","em","strong","code","samp","kbd","var","b","i","u","small","s","big","strike","tt","font","cite","q","sub","sup","blink","button","command","dir","embed","object","fieldset","iframe","marquee","basefont","bdi","canvas","time",
  # TODO: other :first-line, :first-letter and :hover overrides can still crash Opera 12 on some sites.  Have suggested in index.html that the user replaces :first with :girst and :hover with :gover when installing one of these CSS files to Opera.
  ]
  inheritDic={"color":"inherit","background":"inherit","*letter-spacing":"inherit","*font-size":"inherit","*font-family":"inherit"}
  # (NB must say inherit, because consider things like p:first-line / A HREF... - the first-line may have higher specificity.
  # If IE7 seems to be getting first lines and first letters wrong, check that Ignore Document Colours is NOT set - "document" can include parts of the CSS.  and try toggling high-contrast mode twice.)
  for e in mostElements:
    if not e in firstLetterBugs_multiple:
      if e in firstLetterBugs_geckoOnly: dictToAddTo = webkitScreenOverride
      elif e in firstLetterBugs_webkitOnly: dictToAddTo = geckoScreenOverride
      elif e in firstLetterBugs_other: dictToAddTo = webkitGeckoScreenOverride
      else: dictToAddTo = css
      dictToAddTo[e+":first-letter"]=inheritDic.copy()
    if not e in firstLineBugs: css[e+":first-line"]=inheritDic.copy()
    for i in map(lambda x:exclude_ie_below_9+e+x,[":before",":after"]):
      css[i]=defaultStyle.copy()
      for mp in ["*margin","*padding"]:
        if not css.get(e,{}).get(mp,"")==css[i][mp]:
          del css[i][mp] # as not sure how browsers would treat a different margin/padding in :before/:after.  But DO keep these settings for the 0px elements, because we DON'T want sites overriding this and causing overprinting.
  # and also do this:
  for i in map(lambda x:exclude_ie_below_9+x,[":before",":after"]): css[i]=defaultStyle.copy() # (especially margin and padding)

  # CSS 2+ markup for viewing XML+CSS pages that don't use HTML.  Not perfect but should be better than nothing.
  xmlKey=":root:not(HTML):not(page), :root:not(HTML):not(page) :not(:empty)"
  # Careful not to use the universal selector, because it can mess up Mozilla's UI.
  # :not(page) is an important addition for recent versions of Firefox whose Preference pages start with 'page' (can be rendered invisible if apply whole of defaultStyle to it).
  css["page:root *"]={"background-color":colour["background"]} # to normalise recent-Firefox preferences pages (without this, some parts do and some don't; result can look too stark).  Tested in Firefox 45.4.
  css[xmlKey]=defaultStyle.copy()
  del css[xmlKey]["*text-decoration"] # because this CSS won't be able to put it back in for links (since it doesn't know which elements ARE links in arbitrary XML)
  # Exception to above for Mozilla scrollbars:
  css[":root:not(HTML):not(page) slider:not(:empty)"]={"background":"#301090"}

  checkbox_scale = int(pixelSize/16)
  if checkbox_scale > 1:
    v = "scale(%d,%d)" % (checkbox_scale,checkbox_scale)
    css["input[type=checkbox]"]={"-ms-transform":v,"-moz-transform":v,"-webkit-transform":v,"-o-transform":"scale(%d)" % checkbox_scale,"margin":"%dpx"%(checkbox_scale*6)}

  if pixelSize:
    # In many versions of firefox, a <P ALIGN=center> with an <IFRAME> inside it will result in the iframe being positioned over the top of the main text if the P's text-align is overridden to "left".  But missing out text-align could allow websites to do full justification.  However it seems OK if we override iframe's display to "block" (this may make some layouts slightly less brief, but iframes usually need a line of their own anyway)
    css["iframe"]["*display"]="block"
    # and if we're doing that, we might as well use the full width:
    css["iframe"]["*width"]="100%"
    # The following may help a little as well: make iframes 50% transparent so at least we can see what's under them if they do overprint (depends on the browser and the site; apparently the IFRAME's height can be treated as close to 0 when it's not) (fixed? keeping this anyway just in case)
    css["iframe"].update({"*filter":"alpha(opacity=50)","*opacity":"0.5","*-moz-opacity":"0.5"})

  # float exceptions for img align=left and align=right (might as well)
  css["img[align=left]"]={"*float":"left"}
  css["img[align=right]"]={"*float":"right"}
    
  # Selection (CSS3)
  if colour.has_key("selection"):
    css["::selection"] = {"background":colour["selection"]}
    css["::-moz-selection"] = {"background":colour["selection"]}

  css['input[type=search]'] = {"-webkit-appearance":"textfield"} # searchbox forces background:white which may conflict with our foreground
  
  css['select']['-webkit-appearance']='listbox' # workaround for Midori Ubuntu bug 1024783
  css['select']['background']=colour['selectbox']
  printOverride['select']['background']=printButtonBackground # TODO: or something else?

  css['input[type=radio]']={'-webkit-appearance':'radio'}
  css['input[type=checkbox]']={'-webkit-appearance':'checkbox'}

  if "alt-backgrounds" in colour:
    css['td:nth-child(odd),div:nth-child(odd)'] = {"background":colour["alt-backgrounds"][0]}
    printOverride['td:nth-child(odd),div:nth-child(odd)'] = {"background":"white"} # TODO: or a very light grey?
    if len(colour["alt-backgrounds"])>1:
      css['td:nth-child(even),div:nth-child(even)'] = {"background":colour["alt-backgrounds"][1]}
      printOverride['td:nth-child(even),div:nth-child(even)'] = {"background":"white"} # TODO: or another very light grey?
    for k in css.keys():
      if css[k].get("background","")==colour["background"] and not k in ["html","body"]: css[k]["background"]="inherit"

  # Make definition lists a bit more legible, including when there is more than one definition for one term
  css['dd+dd']={'*padding-top':'0.5ex','*margin-top':'1ex','*border-top':'thin dotted grey'}
  css['dt'].update({'*padding':'0.5ex 0px 0px 0px','*margin':'1ex 0px 0px 0px','border-top':'thin grey solid'})
  
  css['hr']={"color":"grey","border-style":"inset"} # prevent pages from changing the colour of horizontal rules, especially to black if we have a black background (sometimes used within tables to mimic fraction lines in formulae)
  for aside in ['aside','figure']: css[aside]['border']="thin "+colour["italic"]+" solid" # might help sometimes
  css['body > pre:only-child']={'*white-space':'pre-line','*font-family':serif_fonts} # this might make Gopher pages easier to read in Firefox's "OverbiteFF" (unless ASCII art is in use); NB on some firefox versions it slows down the loading of text/plain URLs and chrome://browser/skin/browser.css etc
  
  for pt in '::-webkit-input-placeholder,:-moz-placeholder,::-moz-placeholder,:ms-input-placeholder,::placeholder'.split(","): css[pt] = {"color":colour["form_disabled"]}

  # Begin site-specific hacks

  def emptyLink(lType,content,css,printOverride,isRealLink=True,omitEmpty=False,isInsideRealLink=False):
   if omitEmpty: eList = [""]
   else: eList = [":empty",":blank",":-moz-only-whitespace"]
   for empty in eList:
    # Fill in the text of an empty link according to
    # context (making up for the fact that we're not
    # displaying whatever CSS-oriented graphical thing
    # the site is showing).  lType is the link in context
    # and 'content' is our guess of what it should say.
    if isRealLink: key = lType+":link"+empty
    else: key = lType+empty
    css[key+":after"]={"color":colour["link"]} # (better make sure the colour is right, as it might be in the middle of a load of other stuff)
    if content:
      if isInsideRealLink: css[key+":after"]["content"]='"'+content+'"'
      else: css[key+":after"]["content"]='"'+content+']"' # overriding "]"
    printOverride[key+":after"]={"color":"#000080"}
    css[key+":before"]={"color":colour["link"]}
    printOverride[key+":before"]={"color":"#000080"}
    if isRealLink:
      key = key.replace(":link",":visited")
      css[key+":after"]={"color":colour["visited"]}
      printOverride[key+":after"]={"color":"#000080"}
      css[key+":before"]={"color":colour["visited"]}
      printOverride[key+":before"]={"color":"#000080"}
    else: # not isRealLink
      if not isInsideRealLink: css[key+":before"]["content"] = '"["'
      css[key]={"text-decoration":"underline","cursor":"pointer","display":"inline","margin":"0px 1ex 0px 1ex","color":colour["link"]}
      css[key+":before"]["cursor"] = css[key+":after"]["cursor"] = "pointer"
      for ll in ["",":before",":after"]: css[exclude_ie_below_9+key+":hover"+ll]={"background":colour["hover"]}
      printOverride[key] = {"color":"#000080"}
  css["div.standardModal-content > div.itemImage:first-child > img"]={"*display":"none"} # 'logo bigger than browser' syndrome

  # Hack for Google search results:
  css["g-img"]={"*display":"inline","*position":"static"}
  css["span.vshid"]={"*display":"inline"} # TODO: rm * ?
  css['img[src^="/images/nav_logo"][alt="Google"]']={"*display":"none"}
  css['div.gb_tc.gb_uc.gb_Vb:empty,div.gb_uc.gb_vc.gb_Wb:empty']={"*display":"none"} # TODO: if gb = Great Britain then we might need to rewrite this to cover other countries.  The div has a :before rule with image content, takes up lots of screen space and is not functional. (2016-10)
  css['table.gssb_c[style~="absolute;"]']={"*position":"absolute"}
  for leaf in ['td','span','a','b']: css['table.gssb_c tr.gssb_i '+leaf]={"background":colour["highlight"]} # TODO: be more specific by saying gssb_c[style~="absolute;"] again ?
  css['div.sbtc div.sbsb_a li.sbsb_d div']={"background":colour["highlight"]} # suggestions cursor 2015-04
  css['a#logo > img[src="/images/nav_logo195.png"]']={"*display":"none"}
  css['div#main div#cnt div#rcnt div.col div#ifb div.rg_meta,div#main div#cnt div#rcnt div.col div#ifb div.rg_bb_i div.rg_bb_i_meta']={"*display":"none"} # image search
  css['div#mngb > div#gb > div.gb_Sb,body#gsr.srp > div#mngb']={"*display":"none"} # other graphical clutter they added 2014-09 and 2014-10
  css['div#gbqfbw > button#gbqfb > span.gbqfi:empty']={'*display':'none'} # 2549-pixel high image on Android shop that messes up scrolling 2016-08
  css['div.kv > cite + div.action-menu.ab_ctl > a[aria-label="Result details"]'] = {'*display':'none'} # it's supposed to just reveal the "Cached" or "Similar" options, but these should be displayed anyway with our CSS so it's a non-functional unlabelled link: save confusion
  # Hack for Wikipedia/MediaWiki diffs (diffchange) and Assembla diffs (was, now) and Sourceforge (vc_, gd, gi, .diff-*) and GitHub (code-deletion, code-addition)
  k = ".diffchange, .was, .now, .vc_diff_change, .vc_diff_remove, .vc_diff_add, .wDiffHtmlDelete, .wDiffHtmlInsert, pre > span.gd, pre > span.gi, .diff-chg, .diff-add, .diff-rem, table.diff-table td.blob-code-deletion span, table.diff-table td.blob-code-addition span"
  css[k] = {"color":colour["italic"]}
  printOverride[k] = {"color":"black"} # TODO: shade of grey?
  css[".wDiffHtmlDelete"]={"*text-decoration":"line-through"}
  css['button[aria-label="Add line comment"] > svg.octicon-plus']={"display":"none"} ; emptyLink('table.diff-table button[aria-label="Add line comment"]','C',css,printOverride,False,True) # GitLab: making those buttons look like "+" just to the left of the diff's "-" and "+" is confusing
  # and media players:
  css["div.mwPlayerContainer div.play-btn span.ui-icon-play:empty:after"]={"content":r'"\21E8 Play"'}
  css["div.mwPlayerContainer div.play-btn span.ui-icon-pause:empty:after"]={"content":'"Pause"'}
  css['body.mediawiki div[title="Play clip"]:empty:after']={"content":'"Play clip"'}
  # Hack for jqMath:
  if pixelSize: css["td.fm-num-frac,td.fm-den-frac"] = {"text-align":"center"}
  # Partial hack for MathJax:  (I wish webmasters would use
  # jqMath, which is easier on user CSS, instead)
  # NB we use div.MathJax_Display here but it's expanded to inline MathJax in printCss
  if pixelSize:
    css["div.MathJax_Display span.mfrac,span.MathJax span.mfrac"]={"display":"inline-table","vertical-align":"middle","padding":"0.5ex"}
    css["div.MathJax_Display span.mfrac > span > span,span.MathJax span.mfrac > span > span"]={"display":"table-row-group","text-align":"center"}
    css["div.MathJax_Display span.mfrac > span > span:first-child,span.MathJax span.mfrac > span > span:first-child"]={"display":"table-cell","border-bottom":"thin solid"}
    css["div.MathJax_Display span.mfrac > span > span + span + span,span.MathJax span.mfrac > span > span + span + span"]={"display":"none"}
    css["div.MathJax_Display span.msqrt > span > span + span,span.MathJax span.msqrt > span > span + span"] = {"display":"none"}
    css["div.MathJax_Display span.msqrt:before,span.MathJax span.msqrt:before"]={"content":r'"\221A("'}
    css["div.MathJax_Display span.msqrt:after,span.MathJax span.msqrt:after"]={"content":'")"'}
    css["div.MathJax_Display span.mtable,span.MathJax span.mtable"]={"display":"inline-table"}
    css["div.MathJax_Display span.mtable span.mtd,span.MathJax span.mtable span.mtd"]={"display":"table-row-group","text-align":"center"}
    for el in [""," span"," img:after"]: css["div.MathJax_Display span.msubsup > span:only-child > span:first-child + span:last-child"+el]={"color":colour["italic"]} # for now, because we don't know if the span:last-child's "vertical-align" should be "sub" or "super" in this context
    css["div.MathJax_Display span.msubsup > span:only-child > span:first-child + span:not(:last-child)"]={"vertical-align":"super"} # TODO: can we do superscript + subscript as an inline-table? (but need a containing element?)
    css["div.MathJax_Display span.msubsup > span:only-child > span:first-child + span + span"]={"vertical-align":"sub"}
  # Following workaround is for MathJax scripts which insist on images when we have fonts (TODO: check for Unicode support?)  It doesn't work in IE9 or below (and possibly some other browsers) because it relies on setting img's content="" to enable the :before/:after; to be safe I'm doing this in only Webkit and Gecko for now.
  for asc in range(0x20,0x7f)+[0xa0,0xd7]+range(0x2200,0x2294): # TODO: others?
    if asc in [ord('"'),ord('\\')]: continue
    k = 'div.MathJax_Display img[src="http://cdn.mathjax.org/mathjax/latest/fonts/HTML-CSS/TeX/png/Main/Regular/476/%04X.png"]' % asc
    webkitGeckoScreenOverride[k]={"width":"0px",'content':'""',"vertical-align":"0px"} # (don't say display=none or that'll hide the :after as well)
    if asc <= 0x7f: c = chr(asc)
    else: c = r'\%04X' % asc
    webkitGeckoScreenOverride[k+":after"]={"content":'"'+c+'"'}
  # Hack for WP/MediaWiki unedited links:
  css["a:link.new, a:link.new i,a:link.new b"]={"color":colour["coloured"] } # (TODO use a different colour?)
  printOverride["a:link.new, a:link.new i,a:link.new b"]={"color":"black" } # TODO: shade of grey?
  # and the navpopup extension: (also adding ul.ui-autocomplete to this, used on some sites)
  css["body.mediawiki > div.navpopup,body.mediawiki .referencetooltip, ul.ui-autocomplete"]={"*position":"absolute","border":"blue solid"}
  css["body.mediawiki > div.ui-dialog"]={"*position":"relative","border":"blue solid"} # some media 'popups'
  # and the map pins (TODO: this is still only approximate! pins tend to be a bit too far to the south-west; not sure why) :
  css['body.mediawiki table tr div[style^="position:absolute"]']={"*position":"absolute","background-color":"transparent"}
  css['body.mediawiki table tr div[style^="position:relative"]']={"*position":"relative","*display":"inline-block"} # inline-block needed because the percentage positioning of the 'absolute' pin div depends on the map div's width being set to that of the map (done on-site by hard-coding, but we would have to special-case it for every possible map width; inline-block is a workaround)
  css['body.mediawiki table tr div[style^="position:absolute"] div[style^="position:absolute"] + div']={"display":"none"} # or the place name would overprint the map too much; it can usually be inferred from the caption
  # and syntax highlighting of code:
  css['body.mediawiki .mw-highlight .k']={"color":colour["italic"]} # keyword
  css['body.mediawiki .mw-highlight .kt']={"color":colour["italic"]} # keyword type
  css['body.mediawiki .mw-highlight .n']={"color":colour["bold"]} # (variable) name
  css['body.mediawiki .mw-highlight .nf']={"color":colour["bold"]} # function name
  css['body.mediawiki .mw-highlight .nt']={"color":colour["italic"]} # tag name(?) (in XML etc)
  css['body.mediawiki .mw-highlight .na']={"color":colour["bold"]} # attribute name
  css['body.mediawiki .mw-highlight .cm,body.mediawiki .mw-highlight .c1,body.mediawiki .mw-highlight .c']={"color":colour["coloured"]} # comment
  css['body.mediawiki .mw-highlight .cp']={"color":colour["headings"]} # preprocessor
  css['body.mediawiki .mw-highlight .s']={"background":colour["highlight"]} # string
  css['body.mediawiki .mw-highlight .se']={"background":colour["highlight"],"color":colour["bold"]} # string escape character
  css['body.mediawiki .mw-highlight .cpf']={"background":colour["highlight"]} # #include parameter (treated like string in some editors)
  css['body.mediawiki .mw-highlight .lineno']={"color":colour["form_disabled"]}
  # TODO: p = punc, o = operator; mi = integer; nv = variable name; nb; others?
  
  # Hack for Vodafone UK's login 2012 (stop their mousein/mouseout events going crazy with our layout)
  css["ul#MUmyAccountOptions"]={"*display":"block"}
  # Hack for some authoring tools that use <FONT COLOR=..> to indicate special emphasis
  css["font[color],span[style=\"color: rgb(128, 0, 0);\"],span[style=\"color:red\"]"]={"color":colour["coloured"]}
  printOverride["font[color],span[style=\"color: rgb(128, 0, 0);\"],span[style=\"color:red\"]"]={"color":"black"} # TODO: shade of grey?
  # and others that use span class="Apple-style-span"
  css["span.Apple-style-span"]={"color":colour["coloured"]}
  printOverride["span.Apple-style-span"]={"color":"black"} # TODO: shade of grey?
  # Hack for pinyinannotator
  if pixelSize:
    css["div.interlinear tt"]={"display":"inline-table","line-height":"1.02","text-align":"center","padding":"0.3em"}
    css["div.interlinear tt i"]={"display":"table-row-group","text-align":"center"}
    css["div.interlinear tt i.line1"]={"display":"table-header-group","text-align":"center","color":colour["headings"]}
    printOverride["div.interlinear tt i.line1"]={"color":"black"}
    css["div#container div#result tt"]={"display":"inline-table","line-height":"1.02","text-align":"center","padding":"0.3em"}
    css["div#container div#result tt > i"]={"display":"table-header-group","text-align":"center"}
    css["div#container div#result tt > b, div#container div#result tt > acronym"]={"display":"table-row-group","text-align":"center"}
  # hack for messages on some sites
  css["tr.new td"]={"border":"thick solid "+colour["coloured"]}
  # hack for (some versions of) phpBB
  css["ul.profile-icons li span"]={"*display":"inline"}
  # hack for embedded Google Maps. 2012-07 Google Maps iframe with certain settings + Safari + CSS = consume all RAM and hang; many sites use GM to embed a "how to find us" map which isn't always the main point of the page, so turn these off until we can fix them properly; in the meantime if you want to see Google Maps you have to turn off this stylesheet (which you'd have to do ANYWAY even without this hack if you want to get any sense out of the maps, unless we can figure out how to give them enough layout exceptions)
  css["body.kui > div#main > div#inner > div#infoarea + div#page > /*div#le-container + div +*/ div#main_map, div.googlemaps > div.mapsbord, div#divMapContainer.MapSingle > div#divMapTools.MapTools, div#divMapContainer.MapSingle > div#divMapTools.MapTools + div#divMap"]={"*display":"none"}
  css["div.rsltDetails > div.jsDivMoreInfo.hideObj"]={"*display":"block"} # not 'reveal address only when mouse-over' (which might be OK in conjunction with a map but...)
  
  # hacks for CAMCors 6, deconstructing some tables etc:
  if pixelSize:
    css['form[action^="/camcors/supervisor/reports"] div.reportBox > table,form[action^="/camcors/supervisor/reports"] div.reportBox > table > tbody,form[action^="/camcors/supervisor/reports"] div.reportBox > table > tbody > tr,form[action^="/camcors/supervisor/reports"] div.reportBox > table > tbody > tr > td']={"display":"block"} # doesn't work well as table
    css['form[action^="/camcors/supervisor/reports"] textarea']={"height":"4em"} # not too high for small windows
    for t in ['table','table > tbody','table > tbody > tr','table > tbody > tr > td']: css['body.camcors-small div.span12 > div > '+t]={"display":"block"} # doesn't work well as table
    css['body.camcors-small div.span12 > div > table'] = {"border":"thin blue solid","margin-bottom":"1ex"} # show difference (important for selection mechanism to make sense)
    css['body.camcors-small input.gwt-TextBox'] = {"width":"2em"} # otherwise they are too wide and affect the whole div
    css['body.camcors-small div.span12 > div > table > tbody > tr > td > div > div > table > tbody > tr > td[align="right"] > div > div.gwt-Label'] = {"display":"none"} # otherwise the "non-supervision hours disabled by college" message can get too wide which affects the whole div
  make_like_link = ["div.GFTJ4-XN2 > a.gwt-Anchor"] # CamCORS
  # (CamCORS hacks end here)
  make_like_link += ["ul.sidebar-navigation > li.sidebar-navigation-item > div.sidebar-navigation-item-header > div.columns:not(:empty)",'a[data-target]'] # ott.cl.cam.ac.uk
  css[','.join(make_like_link)] = css["a:link "] ; css[','.join(x+":hover" for x in make_like_link)] = css["a:link:hover "]
  printOverride[','.join(make_like_link)] = printOverride["a:link "]
  if (pixelSize and separate_adjacent_links_at_other_sizes) or (not pixelSize and separate_adjacent_links_at_size_0):
    for l in [":before",":after"]:
      css[','.join(x+l for x in make_like_link)] = css[exclude_ie_below_9+"a:link"+l]
      printOverride[','.join(x+l for x in make_like_link)] = printOverride[exclude_ie_below_9+"a:link"+l]
  css['img[src="img/otterlogo.jpg"][width="100%"]']={'*display':'none'} # ott.cl.cam.ac.uk

  # hack for MHonarc and similar setups that put full-sized images into clickable links
  # (see comments on max-width above; doesn't seem to be a problem in this instance)
  # if pixelSize: css["a:link img,a:visited img"]={"max-width":"100%","max-height":"100%"}
  # -> DON'T do this - if one dimension is greater than 100% viewport but other is less, result can be bad aspect ratio

  # More autocomplete stuff
  css['body > div.jsAutoCompleteSelector[style~="relative;"]'] = {'*position':'relative','border':'blue solid'}
  
  # hack for sites that use jump.js with nav boxes
  jjc = "body > input#site + div#wrapper "
  jumpjsContent = jjc+"div#content,"+jjc+"div#message"
  jumpjsTooltip = 'div > div.tooltip.dir-ltr[dir="ltr"]' # TODO: ? div[style^="position: absolute"] > div > div.tooltip
  css[jumpjsTooltip+","+jjc+"div#message"]={"border":"thin solid "+colour["italic"]}
  for lr in ['Left','Right']: css["div.nav > div.resultNavControls > ul > li.resultNav"+lr+"Disabled"]={'display':'none'}
  if pixelSize:
      css[jumpjsTooltip]={"position":"absolute","z-index":"9"}
      css[jumpjsTooltip+" p,"+jumpjsTooltip+" div.par"]={"margin":"0px","padding":"0px"}
      css["div.document > div.par > p.sl,div.document > div.par > p.sz"]={"margin":"0px","padding":"0px"}
      css["body > input#site + div#wrapper > div#header, body > input#site + div#wrapper > div#regionHeader"]={
        "height":"40%", # no more or scroll-JS is too far wrong
        "position":"fixed","top":"0px","left":"auto",
        "right":"0px", # right, not left, or overflow problems, + right helps w. tooltips
        "width":"30%", # not fixed+100% or PgDn will go wrong
        "overflow":"auto","border":"blue solid","z-index":"1"}
      css[jumpjsContent]={"margin-right":"31%","z-index":"0"} # to match the 30% (i.e. take 70%, actually 69%)
      css[jjc+"div#secondaryNavContent"]={"*display":"block"} # not None, even if the screen SEEMS to be too small, because we've changed the layout
      css[jjc + "div#secondaryNav"]={"position":"fixed", # or double-scroll JS fails
                 "bottom":"0px","top":"auto",
                 "right":"0px","left":"auto",
                 "width":"30%","height":"60%","border":"blue solid","overflow":"auto","z-index":"2"}
      css["body > div#wrapper div#content div#navScrollPositionFloating"]={
        "display":"block", # don't flash on/off
      }
      css[jjc+"div#content div#navScrollPositionFloating,"+jjc+"div.navPosition > div.scrollPositionDisplay"]={
        "position":"fixed", # don't 'pop up' using display toggle and disrupt the vertical positioning of the entire text due to our position:static override
        "display":"block", # don't flash on/off
        "top":"auto", # because we're using bottom:0px (overriding the popup location)
        "bottom":"0px","right":"0px",
        "width":"30%", # to match the above
        "border":"thin blue solid",
        "overflow":"auto", # just in case
        "z-index":"3", # ditto
      }
      css[jjc+"div.navPosition"]={"display":"block"} # as above, don't flash on/off
      css[jjc+"div#regionHeader div.navPosition > div.scrollPositionDisplay"]={
        "position":"static", # as it's inside regionHeader; no point putting it bottom/right or it won't be visible (clipped by regionHeader)
        "width":"100%", # not 30% because this time it's of regionHeader not of screen
      }

      css["body.HomePage > div#regionMain > div.wrapper > div.wrapperShadow > div#slider > div#slideMain"]={"width":"1px","height":"1px","overflow":"hidden"} # can't get those kind of JS image+caption sliders to work well in large print so might be better off cutting them out (TODO somehow relocate to end of page?) (anyway, do height=width=1 because display:none or height=width=0 seems to get some versions of WebKit in a loop and visibility:hidden doesn't always work)
  # and not just if pixelSize (because these icons aren't necessarily visible with our colour changes) -
  css[exclude_ie_below_9+"li#menuNavigation.iconOnly > a > span.icon:after"]=css[exclude_ie_below_9+"li#menuNavigation.iconOnly > a:empty:after"]={"content":'"Navigation"',"text-transform":"none"}
  css[exclude_ie_below_9+"li#menuSearchHitNext.iconOnly > a > span.icon:after"]=css[exclude_ie_below_9+"li#menuSearchHitNext.iconOnly > a:empty:after"]={"content":'"Next hit"',"text-transform":"none"}
  css[exclude_ie_below_9+"div#wrapper div#primaryNav > ul.menu > li#menuToday > a.todayNav > span.icon:empty:after"]={"content":'"Today"',"text-transform":"none"}
  css[exclude_ie_below_9+"div#wrapper div#primaryNav > ul.menu > li#menuPublications > a > span.icon:empty:after"]={"content":'"Publications"',"text-transform":"none"}
  css[exclude_ie_below_9+"div#wrapper div#primaryNav > ul.menu > li#menuHome > a > span.icon:empty:after"]={"content":'"Home"',"text-transform":"none"}
  css[exclude_ie_below_9+"div#wrapper div#primaryNav > ul.menu > li#menuHome + li > a > span.icon:empty:after"]={"content":'"Bbl"',"text-transform":"none"}
  css[exclude_ie_below_9+"div#header div#menuFrame ul.menu li#menuSynchronizeSwitch a span.icon:after, div#regionHeader menu li#menuSynchronizeSwitch a:after, div#wrapper div#primaryNav > ul.menu > li#menuSynchronizeSwitch > a#linkSynchronizeSwitch > span.icon:empty:after"]={"content":'"Sync"',"text-transform":"none"}
  css[exclude_ie_below_9+"li#menuToolsPreferences.iconOnly > a > span.icon:after"]=css[exclude_ie_below_9+"li#menuToolsPreferences.iconOnly > a:empty:after"]={"content":'"Preferences"',"text-transform":"none"}
  css[exclude_ie_below_9+"div.resultNavControls > ul > li.resultNavLeft > a > span:after, div.jcarousel-container + div#slidePrevButton:empty:after"]={"content":'"<- Prev"',"text-transform":"none"}
  css[exclude_ie_below_9+"div.resultNavControls > ul > li.resultNavRight > a > span:after, div.jcarousel-container + div#slidePrevButton:empty + div#slideNextButton:empty:after"]={"content":'"Next ->"',"text-transform":"none"}
  css[exclude_ie_below_9+"div.resultNavControls > ul > li.resultNavLeft"]={"margin-left":"0px","margin-right":"1ex"}
  css[exclude_ie_below_9+"div.resultNavControls > ul > li.resultNavRight"]={"margin":"0px"}
  css[exclude_ie_below_9+"div.resultNavControls > ul > li.resultNavDoubleLeft > a > span:after"]={'content':'"<<- Backwd"','text-transform':'none'}
  css[exclude_ie_below_9+'div.resultNavControls > ul > li.resultNavDoubleRight > a > span:after']={'content':'"Fwd ->>"','text-transform':'none'}
  css[jumpjsContent.replace(","," .hl,")+" .hl"]={"background":colour['highlight']}
  printOverride[jumpjsContent.replace(","," .hl,")+" .hl"]={"background":'white'} # TODO: shade of grey?
  css[jjc+"span.mk, "+jjc+"span.mk b"]={"background":colour["reset_button"]}
  printOverride[jjc+"span.mk, "+jjc+"span.mk b"]={"background":"white"}
  css[jjc+"div.stdPullQuote"]={"border":css["aside"]["border"]}
  css['div.jsDownloadFileList ul.downloadItemSet > li.itemRow'] = { # confusion re is the Play button above or below the item: delineate them more clearly
    '*padding-top':'1em', # TODO: does this even work?
    'border':'thin blue solid'}
  css['div#content > div#pubListResults > div#pubsViewResults > div.publication'] = {'border':'thin blue solid'}
  css[jjc+"span.pageNum[data-no]"]={'display':'none'}
  css['div#regionMain div.tooltip > ul.tooltipList > li.tooltipListItem > div.header > a > span.source + span.title:before']={'content':r'"\2014"'}
  css['div#materialNav > nav > h1 + ul.directory > li > a > span.title + span.details'] = {'float':'right'}
  # if pixelSize: css[exclude_ie_below_9+"input#site + div#wrapper > div#header > div#menuFrame > ul.menu > li:before"]={"content":"attr(id)","text-transform":"none","display":"inline"}
  css[".menu li a span.label"]={"display":"inline","text-transform":" none"} # not just 'if pixelSize', we need this anyway due to background overrides
  css["body > input#site + div#wrapper div#content figure > img"]={"*max-width":"100%"}
  # some site JS adds modal boxes to the end of the document, try:
  if pixelSize:
    css["body.yesJS > div.ui-dialog.ui-widget.ui-draggable.ui-resizable, body.yesJS > div.fancybox-wrap[style]"]={"position":"absolute","border":"blue solid"}
    css["body.yesJS > div.fancybox-wrap[style] div.fancybox-close:after"]={"content":"\"Close\""}
    # hack for sites that embed YouTube videos (NASA etc) when using the YouTube5 Safari extension on a Mac (TODO: Safari 6 needs sorting out)
    css["div.youtube5top-overlay,div.youtube5bottom-overlay,div.youtube5info,div.youtube5info-button,div.youtube5controls"]={"background":"transparent"}
    css["div#yt-masthead > div.yt-masthead-logo-container, div#yt-masthead-content > form#masthead-search > button.yt-uix-button.yt-uix-button-default"]={"display":"none"}
    css['div.guide-item-container > ul.guide-user-links.yt-box > li[role="menuitem"], div.guide-channels-content > ul#guide-channels > li[role="menuitem"]']={"display":"inline-block"}
  # hack for MusOpen:
  css["a.download-icon span.icon-down:empty:after"]={"content":'"Download"',"color":colour["link"]}
  printOverride["a.download-icon span.icon-down:empty:after"]={"color":"black"}
  css['iframe[title="Like this content on Facebook."],iframe[title="+1"],iframe[title="Twitter Tweet Button"]']={"*display":"none"}
  # Hack for some other sites that put nothing inside software download links:
  emptyLink("div.jsDropdownMenu.downloadDropdown > a.secondaryButton.dropdownHandle > span.buttonIcon.download","Download",css,printOverride,False)
  emptyLink("a.shareButton > span",None,css,printOverride,False,True);emptyLink("div.standardModal-content > div.itemInfoContainer > div.itemFinderLink > a.copyLink[title=\"Copy Link\"] > span","Copy Link",css,printOverride,False);css["div.itemInfoContainer > div.itemFinderLink, div.itemFinderLink > div.shareLinkContainer,input.shareLink[readonly]"]={"*width":"100%"}
  emptyLink("a[title~=download]","Download",css,printOverride)
  # and more for audio players:
  emptyLink("div.audioFormat > a.stream","Stream",css,printOverride)
  emptyLink("a.jsTrackPlay",r"\21E8 Play",css,printOverride) # (sometimes but not always within div.playBtn)
  emptyLink("a.jsTrackPause","Pause",css,printOverride)
  css["div.jsAudioPlayer div.ui-slider > a.ui-slider-handle:link:empty"] = { "*position": "relative", "text-decoration":"none" }
  for jsPlayElem in ['div','a']:
    css["div.jsAudioPlayer > div.jsAudioPlayerInterface > "+jsPlayElem+".jsPlay.controlElem:empty:after"] = { "content": r'"\21E8 Play"', "color":colour["link"]}
    css["div.jsAudioPlayer > div.jsAudioPlayerInterface > "+jsPlayElem+".jsPlay.jsActive.controlElem:empty:after"] = { "content": r'"Playing"', "color":colour["link"]}
  css["div.jsAudioPlayer > div.jsAudioPlayerInterface > div.jsMute.controlElem:empty:after"] = { "content": '"Mute"', "color":colour["link"]}
  printOverride["div.jsAudioPlayer > div.jsAudioPlayerInterface > div.controlElem:empty:after"] = { "color":"black" } # (TODO: but do we want to print those controls at all?)
  css["div.jsAudioPlayer > div.jsAudioPlayerInterface > div.controlElem:empty"] = { "cursor":"pointer" }
  css["div.jsAudioPlayer > div.jsAudioPlayerInterface > div.controlElem"] = { "*display":"inline" }
  css["div.jsAudioPlayer > div.jsAudioPlayerInterface > div.controlElem.ui-slider"] = { "*display":"block" }
  css['div.mejs-playpause-button button[title="Play/Pause"]:empty:after'] = {"content":'"Play/pause"'}
  # and more:
  emptyLink("div.digitalPubFormat > a.fileFormatIcon","Pub format",css,printOverride) # digital publication or whatever
  emptyLink("div.audioFormat > a.fileFormatIcon.audio","Audio format",css,printOverride)
  emptyLink('a[target="itunes_store"]',"iTunes shop",css,printOverride)
  emptyLink('a.appStore[href^="https://itunes.apple.com/"]',"Apple shop",css,printOverride)
  emptyLink('a[href^="https://play.google.com/store/apps/"]',"Android shop",css,printOverride)
  emptyLink('a[href^="http://apps.microsoft.com/"]',"Microsoft shop",css,printOverride)
  emptyLink('div#btnPreviousPage.previousPage',"Previous page",css,printOverride,False)
  emptyLink('div#btnNextPage.nextPage',"Next page",css,printOverride,False)
  emptyLink('div.expanderIcon.collapsed',"+ expand",css,printOverride,False)
  emptyLink('div.expanderIcon.expanded',"- collapse",css,printOverride,False)
  emptyLink('a.navButton.prevNav > div.buttonShell',"Previous",css,printOverride,False)
  emptyLink('a.navButton.nextNav > div.buttonShell',"Next",css,printOverride,False)
  emptyLink('a[title="PREVIOUS"]',"Previous",css,printOverride,True)
  emptyLink('a[title="NEXT"]',"Next",css,printOverride,True)
  # emptyLink('div.toolbar > a.jsZoomIn.zoomIn',"Zoom in",css,printOverride,False);emptyLink('div.toolbar > a.jsZoomOut.zoomOut',"Zoom out",css,printOverride,False) # TODO: somehow let these work? (apparently it's all CSS tricks and we're overriding it)
  emptyLink('div.toolbar > a.jsCloseModal',"Close",css,printOverride,False)
  css["div.galleryCarouselItems"]={"*white-space":"normal"} # not 'nowrap'
  emptyLink('div.tabViews > div.tabControls > a.discoveryTab',"Discovery",css,printOverride,True);emptyLink('div.tabViews > div.tabControls > a.comparisonTab',"Comparison",css,printOverride,True);emptyLink('div.tabViews > div.tabControls > a.xRefTab',"xref",css,printOverride,True) # has href="#" so True; NB these are more likely :blank than :empty, so might not work in all browsers (but don't want to risk removing :empty altogether)
  emptyLink("div.mejs-inner > div.mejs-controls > div.mejs-play > button",r"\21E8 Play",css,printOverride,False)
  emptyLink("div.mejs-inner > div.mejs-controls > div.mejs-pause > button",r"Pause",css,printOverride,False)
  emptyLink(jjc+"div#regionHeader > div#publicationNavigation > div.studyPaneToggle > span.icon","Toggle study pane",css,printOverride,False) # (TODO: on some versions this is effective only if the browser window exceeds a certain width)
  if pixelSize:
    css[jjc+"div#regionMain div#study div.studyPane,div#regionMain > div.wrapper > div.wrapperShadow > div.studyPane"]={"position":"fixed","bottom":"0px","left":"30%","height":"30%","border":"magenta solid","overflow":"auto","z-index":"4"}
    css[jjc+".pub-int ruby"]={"padding":"0 0.35em"}
    css[jjc+"nav div#documentNavigation div.navVerses ul.verses li.verse"]={"display":"inline","margin":"0 0.1ex"}
  emptyLink(jjc+"a.hasAudio > span","Audio",css,printOverride,False)
  emptyLink(jjc+"li.verseOutline a.outToggle > span","Outline",css,printOverride,False) # TODO: why won't this match?
  css["div#screenReaderNavLinkTop > p,div#primaryNav > nav > ul > li"]={"*display":"inline"} # save a bit of vertical space
  css["nav p#showHideMenu > a#showMenu > span.icon:empty:after"]={"content":'"showMenu"'}
  css["nav p#showHideMenu > a#hideMenu > span.icon:empty:after"]={"content":'"hideMenu"'}
  css["nav p#showHideMenu > a#goToMenu > span.icon:empty:after"]={"content":'"goToMenu"'}
  css["a[onclick] > span.iconPrint:empty:after"]={"content":'"Print"'}
  css["a > span.iconHelp:empty:after"]={"content":'"Help"'}
  css["div.jwplayer span.jwcontrols > span.jwcontrolbar span.jwplay > span:first-child:before"]={"content":'"Play/pause button: "'} ; css["div.jwplayer span.jwcontrols > span.jwcontrolbar span.jwplay > span:first-child > button"]={"width":'2em'} # (CSS can't put a text label into that button itself, but we can at least put one before it.  Original is done with background graphics etc.  Incidentally, button:empty doesn't work because it does have some whitespace.)
  css["div.jwplayer span.jwcontrolbar,div.jwplayer span.jwcontrols"]={"display":"inline"} # don't hide controls when mouse is not over video (seeing as they're being repositioned outside it)
  css['div.rp__controls__playback[aria-label="Play"]:empty:before']={"content":'"Play/pause"'} # e.g. ABC Classic FM
  css['div.audio > div.play[rv-on-click]:empty:before']={'content':'"\21E8 Play"'}
  css['div.audio > div.pause[rv-on-click]:empty:before']={'content':'"Pause"'}
  css['body > div.ui-draggable > div.ui-dialog-titlebar']={'cursor':'move'}
  def doHeightWidth(height,width): css['img[width="%d"][height="%d"]' % (width,height)]=css['svg[viewBox="0 0 %d %d"]' % (width,height)]={"*height":"%dpx"%height,"*width":"%dpx"%width}
  doHeightWidth(17,21);doHeightWidth(24,25) # better keep these because it could be an image link to a social network whose natural size is full-screen (and some news sites put these right at the top of all their pages)
  for w in [12,16,17,18,20,24,26,28,30,36,44,48]: doHeightWidth(w,w) # could be navigation icons or similar & there could be very many of them; don't want these to take too much space (e.g. GitHub 'avatars', can be quite simple but still hundreds of pixels big unnecessarily)
  css["div.write-content > textarea#new_comment_field, div.write-content > textarea#issue_body"]={"*height":"10em","*border":"blue solid"} # Github (make comment fields a bit bigger)
  css["div.js-suggester-container > div.write-content > div.suggester-container > div.js-suggester"]={"*position":"absolute"}
  css["div.sidebar-wrapper > ul.nav > li"]={"*display":"inline"} # save a bit of vertical space (GitLab etc)
  css['#calendar td.fc-widget-content.day-available']={'border':'green solid'}

  # For vtiger CRM 6.5.0:
  emptyLink("div#page > div.navbar > div#topMenus > div#nav-inner > div.menuBar > div#headerLinks span.dropdown > a.dropdown-toggle > span.icon-bar:first-child","Preferences etc",css,printOverride,False,isInsideRealLink=True)
  css["div#page > div.navbar > div#topMenus > div#nav-inner > div.menuBar > div.span9 > ul#largeNav"]={"*display":"block"}
  for n in ['listView','relatedList']:
    for t in ["Previous","Next"]:
      emptyLink("button#"+n+t+"PageButton.btn > span",t+" page",css,printOverride,False)
  emptyLink("button.dropdown-toggle.btn > i","Toggle",css,printOverride,False)

  css['div#secondaryNav div#documentNavigation ul.navigationTabs li.tabItem']={'color':colour['link']}
  css['div#secondaryNav div#documentNavigation ul.navigationTabs li.tabItem.active']={'color':colour['visited'],'border':'thin red solid'}
  printOverride['div#secondaryNav div#documentNavigation ul.navigationTabs li.tabItem']=printOverride['div#secondaryNav div#documentNavigation ul.navigationTabs li.tabItem.active']={'color':'#000080'}
  # Hacks for RoundCube-based webmail sites and some forums:
  for t in ["Reset search","Search modifiers","Show preview pane","Enlarge","Click here to give thanks to this post."]: emptyLink('a[title="'+t+'"]',t,css,printOverride) # (OK 'Enlarge' isn't RoundCube but is used on some MediaWiki sites)
  css[exclude_ie_below_9+"li.unread > a > span.unreadcount:before"]={"content":'" ("',"color":colour["coloured"]}
  css[exclude_ie_below_9+"li.unread > a > span.unreadcount:after"]={"content":'")"',"color":colour["coloured"]}
  css[exclude_ie_below_9+"li.unread > a > span.unreadcount"]={"color":colour["coloured"]}
  css["div#mailboxcontainer > div#folderlist-content ul#mailboxlist > li.mailbox"]={"*display":"inline","*border":"none"} # in case you have a lot of folders (seeing as they're displayed on every screen)
  css["div#mailview-bottom > div#mailpreviewframe > iframe#messagecontframe,body.home > div.container > header#globalMasthead + div.clear + header#localMasthead + div.clear + div#frameStore > iframe,body.back > div#content > iframe#ifraResult,body.detailhost > table#detable td#drifdiv > iframe#drif"]={ # 'body.home' etc is for search.lib.cam.ac.uk
      "*height":"25em","*overflow":"visible", # hopefully one of those will work
      "*filter":"none","*opacity":"1","*-moz-opacity":"1"}
  css["body.detailhost > table#detable,body.detailhost > table#detable td#drifdiv"]={"*width":"100%"} # also for search.lib.cam.ac.uk
  css["a#composeoptionstoggle > span.iconlink[title=\"Options\"]:empty:after"]={"content":'"Options"'}
  # Blackwells article feedback:
  emptyLink("a[title=\"Yes\"]","Yes",css,printOverride)
  emptyLink("a[title=\"No\"]","No",css,printOverride)
  # Hacks for eBay:
  css['td#storeHeader']={"*width":"30%"}
  css['td#storeHeader + td.ds-dtd iframe']={"*height":"15em","*filter":"none","*opacity":"1","*-moz-opacity":"1"}
  css['a#gh-la > img#gh-logo']={"*display":"none"} # sorry but it's too big and causes too much horizontal scrolling
  css['div#main + div#spinner > div.spinWrap > p.loader:empty']={'*display':'none'} # Energenie/Sagepay+Paypal 2014-10: please don't spin that line all over the screen and give me a seizure (TODO: would be nice to inspect their scripts to figure out which CSS attributes they were using and consider turning these off globally, but this might require another purchase; the site has timeouts so you can't hang around for too long inspecting how it works)
  # Hacks for LycaMobile online top-up (2014):
  css['iframe[style="height: 1024px;"]']={"*height":"50em","*filter":"none","*opacity":"1","*-moz-opacity":"1"} # (some versions of Firefox can't turn off their misguided scrolling="no" markup AND can't access a context menu to open frame in new tab, so I hope height=50em will be enough; TODO: overflow-y within the iframe like the Twitter-embedded hack below?)
  # Hacks for LinkedIn:
  css['div#post-module > div.post-module-in > form#slideshare-upload-form, div#post-module > div.post-module-in > div#slideshare-upload-callout']={'*display':'none'} # can't get it to work, and a non-working form is just clutter
  css['iframe[src^="https://www.linkedin.com/csp/ads"],iframe[src^="https://ad-emea.doubleclick.net"]']={'*display':'none'} # sorry LinkedIn but they're getting really too cluttered for giant-print navigation
  emptyLink("input.post-link + a.post-link-close","Cancel posting link",css,printOverride) ; emptyLink("a.cancel-file-upload","Cancel file upload",css,printOverride) # I think (not sure how this is supposed to work)
  # Hacks for StackOverflow/etc:
  emptyLink('a[title="delete this comment"]',"Delete this comment",css,printOverride)
  emptyLink('a[title="expand to show all comments on this post"]',"Expand all comments",css,printOverride)
  # Hacks for SOME of Discovery's stuff (although that site is difficult to sort out) :
  if pixelSize:
    css["html.flexbox > body.editorial > div#site-content > div.site-inner > div#content-wrap > div#editorial-main + div#right-rail"]={"display":"none"}
    css["div.slider-body div"]={"display":"block","-webkit-box-orient":"inline-axis","-moz-box-orient":"inline-axis","box-orient":"inline-axis" } # not webkit-box
    css['iframe[title^="Facebook Cross Domain"]']={'display':'none'}
    css['iframe[height="90"][scrolling="no"]']={'display':'none'}
    # + for many sites with large transparent.png images:
    css['img[src*="/transparent.png"]']={'display':'none'}
    # + for sites that embed their news in Twitter format:
    css["body > div.twitter-timeline,body > div.twitter-tweet"]={"overflow-y":"auto","height":"100%"} # in case the overflow:auto override to iframe's scrolling=no isn't working
    # + for BBC radio player:
    css['div.radioplayer-emp-container > div#empv3[style="width: 1px; height: 1px;"]']={"height":"0px","overflow":"hidden"} # so that player controls are higher up (don't say display:none or it won't play in some browsers)
    css['button.twite__share-button,button.twite__share-button + div.twite__panel']={"display":"none"} # BBC 2016: users of social networks already know how to share things; don't need icons that take up whole screen when page is put into large print
    css['form[action^="https://ssl.bbc.co.uk"] > button.p-f-button']={'display':'none'} # doesn't work very well anyway and takes up too much room
  css['body#schedules-day div.programmes-page li#on-now']={"border":"blue solid"}

  # alternative to <wbr/> :
  css['div#regionMain > div.wrapper div#content div#article > article p span.wd.refID, div#regionMain > div.wrapper div#content div#article > article h2 span.wd.refID, div#regionMain > div.wrapper div#content div#article > article h3 span.wd.refID, body > div.ui-dialog div > p > span.wd.refID']={"display":"none"}
  # also use of 'q' adding duplicate quotes:
  css['div#regionMain > div.wrapper div#content div#article > article q.scrp:before, div#regionMain > div.wrapper div#content div#article > article q.scrp:after']={'content':'""'}
  
  # HomeSwapper etc:
  css['iframe[style^="display: none"]']={"*display":"none"}
  
  # sites created at wix.com must have this or their JS will crash on load and not display any content:
  css['div#ReflowTestContainer[style^="width: 1px"]']={"*width":"1px","*height":"1px","*overflow":"hidden"}
  css['div#ReflowTestContainer[style^="width: 1px"] > div#ReflowTestNode']={"*width":"200px"}
  css['div#ReflowTestContainer[style^="width: 1px"] > div#ReflowTestNode > div.ReflowTextInnerNode']={"*width":"10%"}
  # w3schools, since it's often coming up in search results -
  for tht in ["Chrome","Internet Explorer","Firefox","Safari","Opera"]: css['th[title="'+tht+'"]:empty:after']={'*content':'"'+tht+'"'}

  # practicalmandarin and other sites designed by some company: please don't jump around when we're in large print
  css['header.sticky-header']={'*display':'block'}

  # video controls etc
  css['svg[viewBox="0 0 22 22"]']={'*height':'22px','*width':'22px'}
  css['svg[viewBox="0 0 32 32"]']={'*height':'32px','*width':'32px'}
  css['svg[viewBox="0 0 36 36"]']={'*height':'36px','*width':'36px'}
  css['div#streamingAudio.jsAudioPlayer']={"*display":"block"} # please don't change it to display:none in Firefox when it scrolls out of view: doing this causes 'jumpy scrolling'
  
  # Chrome view source (you can activate a CSS bookmarklet on it), and Firefox view source:
  css['body > div.line-gutter-backdrop + table span.html-tag, body#viewsource span.start-tag, body#viewsource span.end-tag']={"color":colour["headings"]}
  css['body > div.line-gutter-backdrop + table span.html-attribute-name, body#viewsource span.attribute-name']={"color":colour["bold"]}
  css['body > div.line-gutter-backdrop + table span.html-attribute-value, body#viewsource a.attribute-value:not([href])']={"color":colour["italic"]}
  css['body > div.line-gutter-backdrop + table span.html-comment, body#viewsource span.comment']={"color":colour["form_disabled"]}
  css['body#viewsource span > span[id^=line]:before']={"*content":'" "',"*display":"block","*font-size":"0","*line-height":"0"} # force line break before line number

  css['h1:before']={"*content":'""'} # overrides large multi-icon image display in Tesco search results 2016-06 (if not logged in with accessibility mode set)
  css['.basketDeliverySurcharge p:before, p.basketInfo:before, body#delivery div#homeDelivery *:after,body#delivery div#homeDelivery *:before']={"*content":'""'} # and this one is needed even on the supposedly "accessible" version (originally developed in conjunction with the RNIB but since drifted)... I want to throw a banana at a Tesco web developer.  Why do I have to spend hours fixing my CSS just to shop?
  css['.header--sticky .primary-nav__item__panel, .header--sticky .utility-nav .utility-nav__list']={"*display":"block"}; css['div[dojotype="dojox.widget.AutoRotator"]'] = {"*display":"none"} # Not that Sainsbury's web developers were any more helpful.  This fixes their broken scrolling 2016-10.
  css['iframe[src^="https://pp.ephapay.net"]']={'*height':'15em'} # Sainsbury's payment card details (they make it non-scrollable)
  
  css['div.xt_fixed_sidebar + div.g_modal.login_modal']={'*position':'absolute','*z-index':'151','border':'blue solid','padding':'1em'} # Tsinghua online course login

  css['div#wrap > div.__iklan + header#masthead + main#content > article[id^="single-post"] > div.container > div.entry-main > aside.entry-sidebar'] = {"display":"none"} # zap an ever-expanding "sidebar" that never lets you get to the article
  
  # Internet Archive:
  css["div#position > div#wbCalendar > div#calUnder.calPosition"]={"display":"none"}
  css["a.year-label.activeHighlight:link"]={"background":colour['highlight']}

  # End site-specific hacks
  css["input[type=text],input[type=password],input[type=search]"]={"border":"1px solid grey"} # TODO what if background is close to grey?
  css['input:-webkit-autofill']={'-webkit-text-fill-color':'blue'} # the background of these things is fixed to bright yellow, so we'd better make sure our webkit-text-fill-color override doesn't apply in this context
  # 'html' overflow should be 'visible' in Firefox, 'auto' in IE7.
  css["html:not(:empty)"]={"*overflow":"visible"}
  # speed up scrolling on Midori (from their FAQ), also avoid colour problems in other browsers on some sites:
  css["*"]={"-webkit-box-shadow":"none","box-shadow":"none"}
  # help Opera 12 and other browsers that don't show keyboard focus -
  css[":focus"]={"outline":colour.get("focusOutlineStyle","thin dotted")}
  
  # Remove '*' as necessary (in css, not needed in printOverride):
  for el in css.keys()[:]:
    for prop,value in css[el].items()[:]:
      if len(prop)>1 and prop[0]=='*':
        del css[el][prop]
        if pixelSize: css[el][prop[1:]] = value
    if css[el] == {}: del css[el]

  # Text for the beginning of the CSS file:
  
  # outfile.write("@import url(chrome://flashblock/content/flashblock.css);\n")
  # That needs to be on first line for old Firefox + flashblock plugin (ignored if not present).
  # However, old IE (including IE6 on Windows Mobile 5/6) rejects the entire stylesheet if it sees it.
  # I think most users who want to block Flash either do different things or can install the line themselves
  # so perhaps now keeping it causes more trouble than it's worth.  Commenting out.

  outfile.write("/* %s generated by %s */\n" % (filename,prog))
  # (useful to have the original filename for when it's renamed userContent.css etc)
  
  outfile.write("""
/* IMPORTANT NOTE.  These stylesheets are NOT intended for
website authors. They are for browser configuration. Using
them on websites that you author might not be a good idea.
- Silas S. Brown */

/* WARNING: This stylesheet has been automatically generated.
You can edit it if you like, but it would probably be easier
to change the program that generates them.
*/""")

  if pixelSize: outfile.write("""

/* Note: CSS can specify that frames be scrollable but it
cannot specify that frames be resizeable.  This can cause
problems on small screens.  To work around it in Firefox,
go to about:config and set layout.frames.force_resizability
to true.
*/

/* Note that this stylesheet uses absolute point sizes in a
number of different places.  This is not good coding, but it
is necessary with some browsers, to avoid problems when
interacting with author-supplied stylesheets. */""")
  outfile.write("""

/* Some versions of IE ignore the first entry so: */
.placebo { line-height: normal; } /* should be harmless even if there is a
.placebo - we want line-height normal
anyway - and should validate */

/* :not(:empty) stops IE5+6 from misinterpreting things it can't understand */

/* Repeat ALT tags after images (problematic; see Mozilla bug 292116)
(2005: commenting this out for now because more trouble than it's worth;
only Mozilla 1.0 does it properly; later versions and Firefox don't)
img[alt]:after { content: attr(alt) !important; color: #FF00FF !important; }
*/\n""")

  ret = printCss(css,outfile,debugStopAfter)

  outfile.write("""@media print {
/*
  Old IE (including IE6 on Windows Mobile 5/6) completely ignores the entire contents of @media, so we need to make screen the default
  and use @media to override for print.
  Making screen the default case and overriding here means original sizes and layouts are NOT preserved for printing
  (which might or might not be wanted).
  W3C's CSS Level 1 specs Section 7.1 showed how to ignore these 'at-rules', so CSS1-only browsers SHOULD be ok.
  PocketIE7 on Windows Mobile 6.1 reads inside the @media for 'color' but not 'background', possibly leading to black on black, so we need a second non-"print" @media block to override it back.
  We also need a second block to override things back for Midori (at least some versions): both color and background.
*/
""")
  # (PocketIE7 also has a habit of displaying the page with a white background while rendering, and applying the CSS's colours only afterwards, even if the CSS is in cache.  PocketIE6 did not do this.  See cssHtmlAttrs option in Web Adjuster for a possible workaround.)
  printCss(printOverride,outfile,debugStopAfter=0)
  # and the above-mentioned second override for IE7, Midori etc :
  outfile.write("} @media tv,handheld,screen,projection {\n")
  for k in printOverride.keys():
    for attr in printOverride[k].keys():
      if attr=='background-color' or printOverride[k][attr] == css.get(k,{}).get(attr,None): del printOverride[k][attr] # don't need to re-iterate an identical attribute (and anyway delete the added background-color alias: we'll re-generate it)
      elif attr=='color': printOverride[k][attr] = css.get(k,{}).get("color",colour["text"])
      elif attr=='background': printOverride[k][attr] = css.get(k,{}).get("background",colour["background"])
      elif attr in ['font-size']: printOverride[k][attr] = css.get(k,{}).get(attr,"")
      else: del printOverride[k][attr] # TODO: shouldn't happen?
    if not printOverride[k]: del printOverride[k]
  printCss(printOverride,outfile,debugStopAfter=0)
  webkitScreenOverride.update(webkitGeckoScreenOverride)
  if webkitScreenOverride:
    outfile.write("} @media screen and (-webkit-min-device-pixel-ratio:0) {\n") # TODO: tv,handheld,projection?
    printCss(webkitScreenOverride,outfile,debugStopAfter=0)
  geckoScreenOverride.update(webkitGeckoScreenOverride)
  if geckoScreenOverride:
    outfile.write("} @media screen and (-moz-images-in-menus:0) {\n") # TODO: tv,handheld,projection?
    printCss(geckoScreenOverride,outfile,debugStopAfter=0)
  outfile.write("}\n")

  return ret

def debug_binary_chop(items,chop_results,problem_start=0,problem_end=-1):
  # returns start,end of problem, and any remaining chop_results after narrowing down to 1 item (so can pass the rest to a sublist)
  if problem_end==-1: problem_end=len(items)
  if problem_end==problem_start+1:
    if chop_results and chop_results[0]=="1": print "Warning: Problem persisted when removed whole item, so removing parts of it is not likely to be useful"
    return problem_start,problem_end,chop_results[1:] # [1:] because important to drop 1 result (expected 'problem didn't persist when removing whole item', then try subdividing and check further results)
  problem_mid = (problem_end-problem_start)/2+problem_start
  if not chop_results: return problem_start,problem_mid,chop_results # try disabling 1st half, if problem persists then recurse on 2nd half, else recurse on 1st half.
  if chop_results[0]=="1": return debug_binary_chop(items,chop_results[1:],problem_mid,problem_end)
  else: return debug_binary_chop(items,chop_results[1:],problem_start,problem_mid)

from textwrap import fill
def printCss(css,outfile,debugStopAfter=0):
  # hack for MathJax (see comments above)
  for k in css.keys()[:]:
    if "div.MathJax_Display" in k: css[k.replace("div.MathJax_Display",".MathJax span.math")]=css[k]
  # For each attrib:val find which elems share it & group them
  rDic={} # maps (attrib,val) to a list of elements that have it
  for elem,attribValDict in css.items():
    # add aliases before starting
    for master,alias in [("background","background-color"),("color","-webkit-text-fill-color")]:
      if attribValDict.has_key(master) and not attribValDict.has_key(alias): attribValDict[alias]=attribValDict[master]
    # end of adding aliases
    for i in attribValDict.items():
      if not rDic.has_key(i): rDic[i]=[]
      rDic[i].append(elem.strip())
  del css # won't use that any more this function
  attrib_val_elemList = rDic.items()
  # Browser debugging by binary chop:
  attrib_val_elemList.sort() # (makes it easier to think about)
  if do_binary_chop:
    global binary_chop_results
    disable_start,disable_end,binary_chop_results = debug_binary_chop(attrib_val_elemList,binary_chop_results)
    if binary_chop_results:
      # chopping up elements within 1 attribute
      attrib_val_elemList[disable_start][1].sort()
      ds2,de2,binary_chop_results = debug_binary_chop(attrib_val_elemList[disable_start][1],binary_chop_results)
      print "Binary chop: From attribute %s=%s, disabling these elements: %s" % (attrib_val_elemList[disable_start][0][0],attrib_val_elemList[disable_start][0][1],", ".join(attrib_val_elemList[disable_start][1][ds2:de2]))
      del attrib_val_elemList[disable_start][1][ds2:de2]
      if binary_chop_results: print "Binary chop: You have supplied too many chop results.  Back off a bit and see the last few debug prints."
    else:
      print "Binary chop: Disabling these attributes: ","; ".join([("%s=%s"%(k,v)) for (k,v),e in attrib_val_elemList[disable_start:disable_end]])
      del attrib_val_elemList[disable_start:disable_end]
  # If any element groups are identical, merge contents, but beware to keep some things separate:
  outDic = {}
  for (k,v),elemList in attrib_val_elemList:
    elemLists = [[x] for x in elemList if '::' in x] # COMPLETELY separate the ::selection markup at all times, to work around browsers ignoring the whole list if they don't like it
    def addIn(l):
      flat=set(reduce(lambda a,b:a+b,elemLists,[]))
      elemLists.append([i for i in l if not i in flat])
    addIn([x for x in elemList if ':blank' in x]) # some Firefox versions need this separated
    addIn([x for x in elemList if ':-moz' in x]) # just in case
    addIn([x for x in elemList if ':-webkit' in x]) # just in case
    addIn([x for x in elemList if ':ms-' in x]) # just in case
    addIn([x for x in elemList if not '*' in x and not '>' in x and not ':empty' in x and not ':not' in x and not '[' in x]) # with IE6, if ANY of the elements in the list use syntax it doesn't recognise ('>', '*' etc), it ignores the whole list, so we need to separate these out
    addIn([x for x in elemList if not ':not' in x]) # for later versions of IE
    addIn(elemList) # everything else
    for eList in elemLists:
      if not eList: continue
      eList.sort()
      elems=tuple(eList)
      if not outDic.has_key(elems): outDic[elems]={}
      outDic[elems][k]=v
  # Now ready for output
  def lenOfShortestElem(elemList): return (min([len(e) for e in elemList if len(e)]),elemList) # (elemList is already alphabetically sorted, so have that as secondary sort)
  for elemList,style in sorted(outDic.items(),lambda x,y:cmp(lenOfShortestElem(x[0]),lenOfShortestElem(y[0]))):
    if debugStopAfter:
      # for pedantic debugging, write each rule separately
      for e in elemList:
        outfile.write(e+" {\n")
        l=style.items() ; l.sort()
        for k,v in l:
          outfile.write("   %s: %s !important;\n" % (k,v))
          debugStopAfter -= 1
          if not debugStopAfter: break
        outfile.write("}\n")
        if not debugStopAfter: return 0
      continue
    # else, if not debugStopAfter:
    outfile.write(fill(", ".join(x.replace(" ","%@%") for x in elemList).replace("-","#@#"),break_long_words=False).replace("#@#","-").replace("%@%"," ")) # (don't let 'fill' break on the hyphens, or on spaces WITHIN each item which might be inside quoted attributes etc, just on spaces BETWEEN items)
    outfile.write(" {\n")
    l=style.items() ; l.sort()
    for k,v in l: outfile.write("   %s: %s !important;\n" % (k,v))
    outfile.write("}\n")
  return debugStopAfter

def main():
  if outHTML: print "<div id=pregen_download><h3>Download pre-generated low-vision stylesheets</h3><noscript>(If you switch on Javascript, there will be an interactive chooser here.&nbsp; Otherwise you can still choose manually from the links below.)</noscript><script><!-- \ndocument.write('Although Javascript is on, for some reason the interactive chooser failed to run on your particular browser. Falling back to the list below.'); //--></script><br><ul>"
  # (HTML5 defaults script type to text/javascript, as do all pre-HTML5 browsers including NN2's 'script language="javascript"' thing, so we might as well save a few bytes)
  for pixelSize in pixel_sizes_to_generate:
    saidPixels = False
    for i in range(len(colour_schemes_to_generate)):
      scheme,suffix,colour = colour_schemes_to_generate[i]
      filename="%d%s.css" % (pixelSize,suffix)
      if pixelSize:
        if saidPixels: pxDesc = "%dpx" % pixelSize # not "" as there's a chance the googlebot will mistake all those duplicate-text links for some kind of attack
        else:
          pxDesc = "%d pixels" % pixelSize
          saidPixels = True
      else: pxDesc = "unchanged"
      toPrn="<li><a href=\"%s\">%s %s</a>" % (filename,pxDesc,scheme)
      if not outHTML: pass
      elif i==len(colour_schemes_to_generate)-1: print toPrn+"</li>"
      else: print toPrn+","
      do_one_stylesheet(pixelSize,colour,filename)
  if not outHTML: return
  print "</ul></div>"
  print """<script><!--
if(document.all||document.getElementById) {
var newDiv=document.createElement('DIV');
var e=document.createElement('H3'); e.appendChild(document.createTextNode('Download or Try Low Vision Stylesheets')); newDiv.appendChild(e);
newDiv.appendChild(document.createTextNode('Select your size and colour: '));
var sizeSelect=document.createElement('SELECT');
var colourSelect=document.createElement('SELECT');
newDiv.appendChild(sizeSelect); newDiv.appendChild(colourSelect);
var defaultSize=35; if(screen && screen.height) defaultSize=screen.height/(window.devicePixelRatio||1)/18.12; // 36pt 15.1in
"""
  pixel_sizes_to_generate.sort()
  for pixelSize in pixel_sizes_to_generate:
    if pixelSize: pxDesc = str(pixelSize)+" pixels"
    else: pxDesc = "unchanged"
    print "e=document.createElement('OPTION'); e.value='"+str(pixelSize)+"'; e.appendChild(document.createTextNode('"+pxDesc+"')); sizeSelect.appendChild(e); if(defaultSize) sizeSelect.selectedIndex="+str(pixel_sizes_to_generate.index(pixelSize))+"; if(defaultSize<"+str(pixelSize)+") defaultSize=0;"
  for scheme,suffix,colour in colour_schemes_to_generate: print "e=document.createElement('OPTION'); e.value='"+suffix+"'; e.appendChild(document.createTextNode('"+scheme+"')); colourSelect.appendChild(e);"
  alternate_server_for_https_requests = os.environ.get('CSS_HTTPS_SERVER',None) # for the bookmarklet, if you want to apply it on https pages (which means the CSS itself must be served from https) and your main website isn't on an HTTPS-capable server but there's a secondary (lower-bandwidth) one you can use just for that use-case
  def tryStylesheetJS(hrefExpr):
    r = "var e=document.createElement('link'); e.id0='ssb22css'; e.rel='stylesheet'; e.href="+hrefExpr+"; if(!document.getElementsByTagName('head')) document.body.appendChild(document.createElement('head')); var h=document.getElementsByTagName('head')[0]; if(h.lastChild && h.lastChild.id0=='ssb22css') h.removeChild(h.lastChild); h.appendChild(e);"
    if alternate_server_for_https_requests:
      r = "var c="+hrefExpr+","+r[4:].replace(hrefExpr,"location.protocol=='https:'?'"+alternate_server_for_https_requests+r"'+c.slice(c.search(/[^/]*\\.css/)).replace('.css',''):c",1)
    return r
  # (do NOT put that in a JS function, the 1st link must be self-contained.  and don't say link.click() it's too browser-specific)
  if alternate_server_for_https_requests: exception = ""
  else: exception = ", except for HTTPS sites in recent browsers which block \"mixed content\" (my site is not yet able to offer an HTTPS option)" # TODO: implement 3rd alternative if primary server becomes HTTPS-capable
  print r"""
newDiv.appendChild(document.createElement('BR'));
newDiv.appendChild(document.createTextNode('Then press '));
var cssLink=document.createElement("A");
var bookmarkletLink=document.createElement("A");
// to reduce confusion, deleted "view or", and set it to 'attachment' in .htaccess
cssLink.appendChild(document.createTextNode("save stylesheet's code"));
bookmarkletLink.appendChild(document.createTextNode("Try stylesheet"));
newDiv.appendChild(bookmarkletLink);
newDiv.appendChild(document.createTextNode(" or "));
newDiv.appendChild(cssLink);
newDiv.appendChild(document.createTextNode("."));
newDiv.appendChild(document.createElement("BR"));
newDiv.appendChild(document.createTextNode("You may be able to drag the 'try stylesheet' link to your browser's Bookmarks toolbar and later press it to re-style any web page"""+exception+r""". It might work better if you set it as a user-supplied stylesheet "));
e=document.createElement("A"); e.href="#inst"; e.appendChild(document.createTextNode("as described below")); newDiv.appendChild(e);
newDiv.appendChild(document.createTextNode("."));
//newDiv.appendChild(document.createTextNode(" (which also means you won't have to press it each time and it will continue to work if this website moves). The 'bookmarklet' approach is best for short-term use (public terminals etc) or testing."));
var base=document.location.href; var i;
for(i=base.length-1; i; i--) if(base.charAt(i)=='/') break;
base=base.substring(0,i)+"/";
function update() {
  cssLink.href=base+sizeSelect.options[sizeSelect.selectedIndex].value+colourSelect.options[colourSelect.selectedIndex].value+".css";
  bookmarkletLink.href="javascript:"""+tryStylesheetJS("""'"+cssLink.href+"'""")+"""function returnvoid(){} returnvoid();";
}
sizeSelect.onchange=update; colourSelect.onchange=update; update();
e=document.getElementById('pregen_download'); e.parentNode.replaceChild(newDiv,e);
if(document.location.href.indexOf("?whatLookLike")>-1) {"""+tryStylesheetJS('cssLink.href')+"""}}
//--></script>""" # "  # (comment for emacs)
  print "(above stylesheets generated by version "+prog.split()[-1]+")"

do_binary_chop = False
binary_chop_results = ""
import sys, os
if "adjuster-config" in sys.argv:
  # print out configuration options for Web Adjuster
  # e.g. large-print-websites.appspot.com
  ps = [] ; cs = [] ; ha = []
  for p in pixel_sizes_to_generate:
    if p==0: ps.append("0=unchanged size")
    else: ps.append(str(p)+"="+str(p)+" pixels")
  for d,f,rest in colour_schemes_to_generate:
    cs.append(f+'='+d)
    ha.append('text="%s" bgcolor="%s" link="%s" vlink="%s" alink="%s"' % (rest['text'],rest['background'],rest['link'],rest['visited'],'red'))
  print "adjuster.options.headAppendCSS="+repr('http://people.ds.cam.ac.uk/ssb22/css/%s%s.css;'+','.join(ps)+';'+','.join(cs))
  print "adjuster.options.cssHtmlAttrs="+repr(';'.join(ha))
elif "desperate-debug" in sys.argv:
  scheme,suffix,colour = colour_schemes_to_generate[0]
  debugStopAfter=1
  while not do_one_stylesheet(chop_pixel_size,colour,"debug%04d.css" % debugStopAfter,debugStopAfter):
    print "Generated debug stylesheet debug%04d.css" % debugStopAfter
    debugStopAfter += 1
elif "chop" in sys.argv:
  do_binary_chop = True
  if not sys.argv[-1] == "chop": binary_chop_results = sys.argv[-1]
  scheme,suffix,colour = colour_schemes_to_generate[0]
  filename="%d%s.css" % (chop_pixel_size,suffix)
  do_one_stylesheet(chop_pixel_size,colour,filename)
  print "Generated debug stylesheet:",filename
else: main()
