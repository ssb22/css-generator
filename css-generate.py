prog="Accessibility CSS Generator, (c) Silas S. Brown 2006-2014.  Version 0.9833"

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
# versions are being kept on SourceForge's E-GuideDog SVN repository
# http://sourceforge.net/p/e-guidedog/code/HEAD/tree/ssb22/css-generator/
# as of v0.9782.  Versions prior to that were not kept, but
# you might be able to find some on Internet Archive.
# To check out the repository, you can do:
# svn co http://svn.code.sf.net/p/e-guidedog/code/ssb22/css-generator

# INSTRUCTIONS
# ------------

# When you run this code, it writes the generated .css files
# to the current directory, and an HTML menu of them to
# standard output (see my CSS page for example).
# If putting this on the Web, include in .htaccess:
# AddType text/css css
# SetEnvIf Request_URI "\.css$" requested_css=css
# Header add Content-Disposition "Attachment" env=requested_css

# You can change pixel_sizes_to_generate and
# colour_schemes_to_generate below - the format of the
# latter is [("description","filename-prefix",{...}),...]
# see the existing ones for example.
# There are also a few advanced options you can change if
# you want, after the sizes and colour schemes.

# Size 0 means "unchanged" - it will disable the size
# changes, and the layout changes that are meant for large
# sizes.  This is for people who need only colour changes.

pixel_sizes_to_generate = [20,25,30,35,40,45,50,60,75,100,18,0] # (1st one listed has special status in debugging - see 'binary chop' below)
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
    "selection":"#006080", # (if supported by the browser)
    "highlight":"#003050", # (misc non-selection highlights in site-specific hacks)
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

# OPTIONS
separate_adjacent_links_at_size_0 = False # sometimes interferes with layouts
separate_adjacent_links_at_other_sizes = True

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

def do_one_stylesheet(pixelSize,colour,filename,debugStopAfter=0):
  outfile = open(filename,"w")
  smallestHeadingSize = pixelSize*5.0/6.0
  largestHeadingSize = pixelSize*10.0/6.0

  # In the settings below, beginning with * means it will
  # be omitted from the "pixelSize 0" option (i.e. leave
  # site's size/layout alone and just changing colours)
  defaultStyle={
    "*font-family":"Times New Roman, times, utopia, /* charter, */ AppleGothic, serif",
    # TNR is listed first for the benefit of broken Xft systems that need the MS fonts to make them look OK. Shouldn't have any effect on other systems.
    # AppleGothic must be listed or Korean is broken on Mac OS (at least 10.7); doesn't seem to affect other scripts, and doesn't seem to be a problem to not mention it in headings etc.  (Safari 5.x works with AppleGothic listed last; in 6.0 it must be listed before serif)
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
    "*-webkit-font-smoothing":"none",
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
    
    "*filter":"none",
    "*opacity":"1",
    "*-moz-opacity":"1",
    
    "-moz-appearance":"none", # DON'T * this, it can lead to white-on-white situations so we need it for colour changes not just size changes
    "*-moz-transform":"none",
    "*-webkit-transform":"none",

    "*-webkit-hyphens":"manual", # auto hyphenation doesn't always work very well with our fonts (TODO: manual or none?  manual might be needed if devs put breakpoints into very long words)
    "*-moz-hyphens":"manual",
    "*-ms-hyphens":"manual",
    "hyphens":"manual",
    }

  # have to explicitly set for every type of element,
  # because wildcards don't always work and inheritance can
  # be overridden by author stylesheets resulting in poor
  # combinations.  NB however we don't list ALL elements in
  # mostElements (see code later).
  mostElements="a,blockquote,caption,center,cite,code,col,colgroup,html,iframe,pre,body,div,p,input,select,option,textarea,table,tr,td,th,h1,h2,h3,h4,h5,h6,font,basefont,small,big,span,ul,ol,li,i,em,s,strike,nobr,tt,samp,kbd,b,strong,dl,dt,dd,blink,button,address,dfn,form,marquee,fieldset,legend,listing,abbr,q,menu,dir,multicol,img,plaintext,xmp,label,sup,sub,u,var,acronym,object,embed,canvas,video".split(",")
  html5Elements = "article,aside,bdi,command,details,summary,figure,figcaption,footer,header,hgroup,main,mark,meter,nav,progress,section,time,del,ins,svg".split(",") # (and ruby/rt/rp/rb)
  mostElements += html5Elements

  # Selector prefixes to exclude certain browsers from trying to implement a rule:
  exclude_ie_below_7 = "html > "
  exclude_ie_below_8 = "html >/**/ body "
  exclude_ie_below_9 = ":not(:empty) " # IE8 (and non-CSS3 browsers) don't support :not
  
  css={} ; printOverride = {}
  webkitScreenOverride = {} ; geckoScreenOverride = {}
  webkitGeckoScreenOverride = {}
  for e in mostElements:
    css[e]=defaultStyle.copy()
    printOverride[e] = {"color":"black","background":"white"}.copy()
    if pixelSize: printOverride[e]["font-size"] = "12pt" # TODO: option?

  # but there are some exceptions:

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

  for e in ["object","embed","img"]:
    del css[e]["*width"], css[e]["*height"] # object/embed should not be forced to 'auto' as that can sometimes break Flash applications (when the Flash application is actually useful), and if img is 'auto' then that can break on some versions of IE

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
  for t in "samp".split(","): css[t]["*font-family"]="helvetica, arial, verdana"
  
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

  # Headings stuff:
  indent = 0
  for h in range(6):
    el="h%d" % (h+1)
    css[el]["color"]=colour["headings"]
    printOverride[el]={"color":"black"}
    css[el]["*font-weight"]="bold"
    css[el]["*font-family"]="helvetica, arial, verdana"
    size = (largestHeadingSize-h*(largestHeadingSize-smallestHeadingSize)/(6-1.0))
    indent += size
    css[el]["*font-size"]="%.1fpx" % size
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
    css[el]["*margin"]="0px 0px 0px %.1fpx" % indent

  # Links stuff:
  for linkInside in ",font,big,small,basefont,br,b,i,u,em,strong,abbr,span,div,code,tt,samp,kbd,var,acronym,h1,h2,h3,h4,h5,h6".split(","):
    for type in [":link",":visited","[onclick]"]:
      css["a"+type+" "+linkInside]={"color":colour["link"],"text-decoration":"underline","cursor":"pointer"}
      printOverride["a"+type+" "+linkInside]={"color":"#101010"} # (dark grey, TODO: option?)
      css["a"+type+":hover "+linkInside]={"background":colour["hover"]}
      css["a"+type+":active "+linkInside]={"color":"red","text-decoration":"underline","cursor":"pointer"}
      if linkInside in ["b","i","em","u","strong"] and not css[linkInside]["color"]==colour["text"]: css["a"+type+" "+linkInside]["color"]=css[linkInside]["color"]
    css["a:visited "+linkInside]["color"]=colour["visited"]
  # set cursor:pointer for links and ANYTHING inside them (including images etc).  The above cursor:auto should theoretically do the right thing anyway, but it seems that some versions of Firefox need help.
  for linkInside in mostElements:
    for type in [":link",":visited","[onclick]"]:
      key="a"+type+" "+linkInside
      if not css.has_key(key): css[key]={}
      css[key]["cursor"]="pointer"
      css[key]["*display"]="inline" # some sites have 'div' or do JS things with 'span'...

  # Italic and bold:
  for i in "i,em,cite,address,dfn,u".split(","):
    css[i+" span"]={
      "*font-family":"helvetica, arial, verdana",
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
  firstLetterBugs=[
   "div", # Gecko messes up textarea when enter multiple paragraphs
  "input","select","option","textarea","table","colgroup","col","img", # probably best to avoid these
  "a", # causes problems in IE
  # The following cause text selection visibility problems in Webkit / Safari 5/6 (cannot be worked around with :first-letter::selection)
  # (+ Chrome 12 bug - OL/LI:first-letter ends up being default size rather than css size; harmless if have default size set similarly anyway)
  # TODO: allow them in Gecko via a Gecko-specific rule?  especially (e.g.) "p"
  "label","address","p","ol","ul","li","pre","code","body","html","h1","h2","h3","h4","h5","h6","form","th","tr","td","dl","dt","dd","b","blockquote","section","header","center","article","span","aside"
  ]
  # TODO: old version had th:first-letter but not tr,td & no documentation of why; similar with first-line
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
    if not e in firstLetterBugs: css[e+":first-letter"]=inheritDic.copy()
    if not e in firstLineBugs: css[e+":first-line"]=inheritDic.copy()
    for i in map(lambda x:exclude_ie_below_9+e+x,[":before",":after"]):
      css[i]=defaultStyle.copy()
      for mp in ["*margin","*padding"]:
        if not css.get(e,{}).get(mp,"")==css[i][mp]:
          del css[i][mp] # as not sure how browsers would treat a different margin/padding in :before/:after.  But DO keep these settings for the 0px elements, because we DON'T want sites overriding this and causing overprinting.
  # and also do this:
  for i in map(lambda x:exclude_ie_below_9+x,[":before",":after"]): css[i]=defaultStyle.copy() # (especially margin and padding)

  # CSS 2+ markup for viewing XML+CSS pages that don't use HTML.  Not perfect but should be better than nothing.
  xmlKey=":root:not(HTML), :root:not(HTML) :not(:empty)"
  # Careful not to use the universal selector, because it can mess up Mozilla's UI
  css[xmlKey]=defaultStyle.copy()
  del css[xmlKey]["*text-decoration"] # because this CSS won't be able to put it back in for links (since it doesn't know which elements ARE links in arbitrary XML)
  # Exception to above for Mozilla scrollbars:
  css[":root:not(HTML) slider:not(:empty)"]={"background":"#301090"}

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
  css['dt'].update({'*padding':'0.5ex 0px 0px 0px','*margin':'1ex 0px 0px 0px','border-top':'thin solid grey'})

  # Begin site-specific hacks

  # Hack for Google search results:
  css["span.vshid"]={"*display":"inline"} # TODO: rm * ?
  css['table.gssb_c[style~="absolute;"]']={"*position":"absolute"}
  for leaf in ['td','span','a','b']: css['table.gssb_c tr.gssb_i '+leaf]={"background":colour["highlight"]} # TODO: be more specific by saying gssb_c[style~="absolute;"] again ?
  css['div#main div#cnt div#rcnt div.col div#ifb div.rg_meta,div#main div#cnt div#rcnt div.col div#ifb div.rg_bb_i div.rg_bb_i_meta']={"*display":"none"} # image search
  
  # Hack for Wikipedia/MediaWiki diffs (diffchange) and Assembla diffs (was, now) and Sourceforge (vc_, gd, gi, .diff-*)
  k = ".diffchange, .was, .now, .vc_diff_change, .vc_diff_remove, .vc_diff_add, .wDiffHtmlDelete, .wDiffHtmlInsert, pre > span.gd, pre > span.gi, .diff-chg, .diff-add, .diff-rem"
  css[k] = {"color":colour["italic"]}
  printOverride[k] = {"color":"black"} # TODO: shade of grey?
  css[".wDiffHtmlDelete"]={"*text-decoration":"line-through"}
  # and media players:
  css["div.mwPlayerContainer div.play-btn span.ui-icon-play:empty:after"]={"content":'"\21E8 Play"'}
  css["div.mwPlayerContainer div.play-btn span.ui-icon-pause:empty:after"]={"content":'"Pause"'}
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
  
  # hack for CAMCors
  if pixelSize:
    css['form[action^="/camcors/supervisor/reports"] div.reportBox > table,form[action^="/camcors/supervisor/reports"] div.reportBox > table > tbody,form[action^="/camcors/supervisor/reports"] div.reportBox > table > tbody > tr,form[action^="/camcors/supervisor/reports"] div.reportBox > table > tbody > tr > td']={"display":"block"}
    css['form[action^="/camcors/supervisor/reports"] textarea']={"height":"4em"}
  
  # hack for MHonarc and similar setups that put full-sized images into clickable links
  # (see comments on max-width above; doesn't seem to be a problem in this instance)
  # if pixelSize: css["a:link img,a:visited img"]={"max-width":"100%","max-height":"100%"}
  # -> DON'T do this - if one dimension is greater than 100% viewport but other is less, result can be bad aspect ratio

  # More autocomplete stuff
  css['body > div.jsAutoCompleteSelector[style~="relative;"]'] = {'*position':'relative','border':'blue solid'}
  
  # hack for sites that use jump.js with nav boxes
  jjc = "body > input#site + div#band + div#wrapper > div#header + div#container > "
  # wrapper might or might not be .dropShadow50
  jjSN = jjc + "div#secondaryNav,"+jjc+"div#message + div#secondaryNav"
  jumpjsContent = jjc+"div#content," +jjc + "div#secondaryNav + div#content,"+jjc+"div#message + div#secondaryNav + div#content,"+jjc+"div#message"
  jumpjsTooltip = 'div > div.tooltip.dropShadowTooltip[dir="ltr"]'
  css[jumpjsTooltip+","+jjc+"div#message"]={"border":"thin solid "+colour["italic"]}
  for lr in ['Left','Right']: css["div.nav > div.resultNavControls > ul > li.resultNav"+lr+"Disabled"]={'display':'none'}
  if pixelSize:
      css[jumpjsTooltip]={"position":"absolute","z-index":"9"}
      css[jumpjsTooltip+" p,"+jumpjsTooltip+" div.par"]={"margin":"0px","padding":"0px"}
      css["div.document > div.par > p.sl,div.document > div.par > p.sz"]={"margin":"0px","padding":"0px"}
      css["body > input#site + div#band + div#wrapper > div#header"]={
        "height":"40%", # no more or scroll-JS is too far wrong
        "position":"fixed","top":"0px","left":"auto",
        "right":"0px", # right, not left, or overflow problems, + right helps w. tooltips
        "width":"30%", # not fixed+100% or PgDn will go wrong
        "overflow":"auto","border":"blue solid","z-index":"1"}
      css[jumpjsContent]={"margin-right":"31%","z-index":"0"}
      css[jjSN]={"position":"fixed", # or double-scroll JS fails
                 "bottom":"0px","left":"auto",
                 "right":"0px", # not left,see above
                 "width":"30%","height":"60%","bottom":"0%","top":"auto","border":"blue solid","overflow":"auto","z-index":"2"}
      css["body.HomePage > div#regionMain > div.wrapper > div.wrapperShadow > div#slider > div#slideMain"]={"width":"1px","height":"1px","overflow":"hidden"} # can't get those kind of JS image+caption sliders to work well in large print so might be better off cutting them out (TODO somehow relocate to end of page?) (anyway, do height=width=1 because display:none or height=width=0 seems to get some versions of WebKit in a loop and visibility:hidden doesn't always work)
  # and not just if pixelSize (because these icons aren't necessarily visible with our colour changes) -
  css[exclude_ie_below_9+"li#menuNavigation.iconOnly > a > span.icon:after"]={"content":'"Navigation"',"text-transform":"none"}
  css[exclude_ie_below_9+"li#menuSearchHitNext.iconOnly > a > span.icon:after"]={"content":'"Next hit"',"text-transform":"none"}
  css[exclude_ie_below_9+"div#header div#menuFrame ul.menu li#menuSynchronizeSwitch a span.icon:before"]={"content":'"Sync"',"text-transform":"none"}
  css[exclude_ie_below_9+"li#menuToolsPreferences.iconOnly > a > span.icon:after"]={"content":'"Preferences"',"text-transform":"none"}
  css[exclude_ie_below_9+"div.resultNavControls > ul > li.resultNavLeft > a > span:after, div.jcarousel-container + div#slidePrevButton:empty:after"]={"content":'"<- Prev"',"text-transform":"none"}
  css[exclude_ie_below_9+"div.resultNavControls > ul > li.resultNavRight > a > span:after, div.jcarousel-container + div#slidePrevButton:empty + div#slideNextButton:empty:after"]={"content":'"Next ->"',"text-transform":"none"}
  css[exclude_ie_below_9+"div.resultNavControls > ul > li.resultNavDoubleLeft > a > span:after"]={'content':'"<<- Backwd"','text-transform':'none'}
  css[exclude_ie_below_9+'div.resultNavControls > ul > li.resultNavDoubleRight > a > span:after']={'content':'"Fwd ->>"','text-transform':'none'}
  css[jumpjsContent.replace(","," span.hl,")+" span.hl"]={"background":colour['highlight']}
  printOverride[jumpjsContent.replace(","," span.hl,")+" span.hl"]={"background":'white'} # TODO: shade of grey?
  css["div.result > div.document span.mk,div.result > div.document span.mk b, div.par p.sb span.mk, div.par p.ss span.mk b"]={"background":colour["reset_button"]}
  printOverride["div.result > div.document span.mk,div.result > div.document span.mk b, div.par p.sb span.mk, div.par p.ss span.mk b"]={"background":"white"}
  # if pixelSize: css[exclude_ie_below_9+"input#site + div#band + div#wrapper > div#header > div#menuFrame > ul.menu > li:before"]={"content":"attr(id)","text-transform":"none","display":"inline"}
  css[".menu li a span.label"]={"display":"inline","text-transform":" none"} # not just 'if pixelSize', we need this anyway due to background overrides
  # some site JS adds modal boxes to the end of the document, try:
  if pixelSize:
    css["body.yesJS > div.ui-dialog.ui-widget.ui-draggable.ui-resizable, body.yesJS > div.fancybox-wrap[style]"]={"position":"absolute","border":"blue solid"}
    css["body.yesJS > div.fancybox-wrap[style] div.fancybox-close:after"]={"content":"\"Close\""}
    # hack for sites that embed YouTube videos (NASA etc) when using the YouTube5 Safari extension on a Mac (TODO: Safari 6 needs sorting out)
    css["div.youtube5top-overlay,div.youtube5bottom-overlay,div.youtube5info,div.youtube5info-button,div.youtube5controls"]={"background-color":"transparent","background":"transparent"}
  # hack for MusOpen:
  css["a.download-icon span.icon-down:empty:after"]={"content":'"Download"',"color":colour["link"]}
  printOverride["a.download-icon span.icon-down:empty:after"]={"color":"black"}
  css['iframe[title="Like this content on Facebook."],iframe[title="+1"],iframe[title="Twitter Tweet Button"]']={"*display":"none"}
  # Hack for some other sites that put nothing inside software download links:
  def emptyLink(lType,content,css,printOverride):
    # Fill in the text of an empty link according to
    # context (making up for the fact that we're not
    # displaying whatever CSS-oriented graphical thing
    # the site is showing).  lType is the link in context
    # and 'content' is our guess of what it should say.
    key = lType+":link:empty"
    css[key+":after"]={
      "content":'"'+content+']"', # overriding "]"
      "color":colour["link"]} # (better make sure the colour is right, as it might be in the middle of a load of other stuff)
    printOverride[key+":after"]={"color":"black"}
    css[key+":before"]={"color":colour["link"]}
    printOverride[key+":before"]={"color":"black"}
    key = key.replace(":link",":visited")
    css[key+":after"]={"color":colour["visited"]}
    printOverride[key+":after"]={"color":"black"}
    css[key+":before"]={"color":colour["visited"]}
    printOverride[key+":before"]={"color":"black"}
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
  emptyLink('a[href^="https://play.google.com/store/apps/"]',"Android shop",css,printOverride)
  emptyLink('a[href^="http://apps.microsoft.com/"]',"Microsoft shop",css,printOverride)
  css["nav p#showHideMenu > a#showMenu > span.icon:empty:after"]={"content":'"showMenu"'}
  css["nav p#showHideMenu > a#hideMenu > span.icon:empty:after"]={"content":'"hideMenu"'}
  css["nav p#showHideMenu > a#goToMenu > span.icon:empty:after"]={"content":'"goToMenu"'}
  css["a[onclick] > span.iconPrint:empty:after"]={"content":'"Print"'}
  css["a > span.iconHelp:empty:after"]={"content":'"Help"'}
  # Hacks for LinkedIn:
  css['div#post-module > div.post-module-in > form#slideshare-upload-form, div#post-module > div.post-module-in > div#slideshare-upload-callout']={'*display':'none'} # can't get it to work, and a non-working form is just clutter
  css['iframe[src^="https://www.linkedin.com/csp/ads"],iframe[src^="https://ad-emea.doubleclick.net"]']={'*display':'none'} # sorry LinkedIn but they're getting really too cluttered for giant-print navigation
  emptyLink("input.post-link + a.post-link-close","Cancel posting link",css,printOverride) ; emptyLink("a.cancel-file-upload","Cancel file upload",css,printOverride) # I think (not sure how this is supposed to work)
  # Hacks for SOME of Discovery's stuff (although that site is difficult to sort out) :
  if pixelSize:
    css["html.flexbox > body.editorial > div#site-content > div.site-inner > div#content-wrap > div#editorial-main + div#right-rail"]={"display":"none"}
    css["div.slider-body div"]={"display":"block","-webkit-box-orient":"inline-axis","-moz-box-orient":"inline-axis","box-orient":"inline-axis" } # not webkit-box
    css['iframe[title^="Facebook Cross Domain"]']={'display':'none'}
    css['iframe[height="90"][scrolling="no"]']={'display':'none'}
    # + for many sites with large transparent.png images:
    css['img[src*="/transparent.png"]']={'display':'none'}
    # + for sites that embed their news in Twitter format:
    css["body > div.twitter-timeline"]={"overflow-y":"auto","height":"100%"} # in case the overflow:auto override to iframe's scrolling=no isn't working
  
  # sites created at wix.com must have this or their JS will crash on load and not display any content:
  css['div#ReflowTestContainer[style^="width: 1px"]']={"*width":"1px","*height":"1px","*overflow":"hidden"}
  css['div#ReflowTestContainer[style^="width: 1px"] > div#ReflowTestNode']={"*width":"200px"}
  css['div#ReflowTestContainer[style^="width: 1px"] > div#ReflowTestNode > div.ReflowTextInnerNode']={"*width":"10%"}

  # End site-specific hacks
  css["input[type=text],input[type=password],input[type=search]"]={"border":"1px solid grey"} # TODO what if background is close to grey?
  # 'html' overflow should be 'visible' in Firefox, 'auto' in IE7.
  css["html:not(:empty)"]={"*overflow":"visible"}
  # speed up scrolling on Midori (from their FAQ) -
  css["*"]={"-webkit-box-shadow":"none"}
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
*/
""")
  # (PocketIE7 also has a habit of displaying the page with a white background while rendering, and applying the CSS's colours only afterwards, even if the CSS is in cache.  PocketIE6 did not do this.  See cssHtmlAttrs option in Web Adjuster for a possible workaround.)
  printCss(printOverride,outfile,debugStopAfter=0,eolComment=" /* @media */")
  # and the above-mentioned second override for IE7 :
  outfile.write("} @media tv,handheld,screen,projection {\n")
  for k in printOverride.keys():
    if 'color' in printOverride[k]:
      printOverride[k]={"color":css.get(k,{}).get("color",colour["text"])}
    else: del printOverride[k]
  printCss(printOverride,outfile,debugStopAfter=0,eolComment=" /* @media */")
  webkitScreenOverride.update(webkitGeckoScreenOverride)
  if webkitScreenOverride:
    outfile.write("} @media screen and (-webkit-min-device-pixel-ratio:0) {\n") # TODO: tv,handheld,projection?
    printCss(webkitScreenOverride,outfile,debugStopAfter=0,eolComment=" /* @media */")
  geckoScreenOverride.update(webkitGeckoScreenOverride)
  if geckoScreenOverride:
    outfile.write("} @media screen and (-moz-images-in-menus:0) {\n") # TODO: tv,handheld,projection?
    printCss(geckoScreenOverride,outfile,debugStopAfter=0,eolComment=" /* @media */")
  outfile.write("} /* end of @media */\n")

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
def printCss(css,outfile,debugStopAfter=0,eolComment=""):
  # hack for MathJax (see comments above)
  for k in css.keys()[:]:
    if "div.MathJax_Display" in k: css[k.replace("div.MathJax_Display",".MathJax span.math")]=css[k]
  # For each attrib:val find which elems share it & group them
  rDic={} # maps (attrib,val) to a list of elements that have it
  for elem,attribValDict in css.items():
    # add aliases before starting
    if attribValDict.has_key("background") and not attribValDict.has_key("background-color"): attribValDict["background-color"]=attribValDict["background"]
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
  # If any elem grps are identical, merge contents
  outDic = {}
  for (k,v),elemList in attrib_val_elemList:
    # With IE6, if ANY of the elements in the list use syntax it doesn't recognise ('>', '*' etc), it ignores the whole list.  So we need to separate it out.
    # Also we need to COMPLETELY separate the ::selection markup at all times.
    elemList_sep = [x for x in elemList if '::' in x]
    elemList_ie = [x for x in elemList if not x in elemList_sep and not '*' in x and not '>' in x and not ':not' in x and not '[' in x]
    elemList_rest = [x for x in elemList if x not in elemList_ie and x not in elemList_sep]
    for eList in [[x] for x in elemList_sep]+[elemList_ie, elemList_rest]:
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
        outfile.write(e+" {"+eolComment+"\n")
        l=style.items() ; l.sort()
        for k,v in l:
          outfile.write("   %s: %s !important;%s\n" % (k,v,eolComment))
          debugStopAfter -= 1
          if not debugStopAfter: break
        outfile.write("}"+eolComment+"\n")
        if not debugStopAfter: return 0
      continue
    # else, if not debugStopAfter:
    outfile.write(fill(", ".join(x.replace(" ","%@%") for x in elemList).replace("-","#@#"),break_long_words=False).replace("#@#","-").replace("%@%"," ").replace("\n",eolComment+"\n")) # (don't let 'fill' break on the hyphens, or on spaces WITHIN each item which might be inside quoted attributes etc, just on spaces BETWEEN items)
    outfile.write(" {"+eolComment+"\n")
    l=style.items() ; l.sort()
    for k,v in l: outfile.write("   %s: %s !important;%s\n" % (k,v,eolComment))
    outfile.write("}"+eolComment+"\n")
  return debugStopAfter

def main():
  print "<div id=pregen_download><h3>Download pre-generated low-vision stylesheets</h3><noscript>(If you switch on Javascript, there will be an interactive chooser here.&nbsp; Otherwise you can still choose manually from the links below.)</noscript><script><!-- \ndocument.write('Although Javascript is on, for some reason the interactive chooser failed to run on your particular browser. Falling back to the list below.'); //--></script><br><ul>"
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
      toPrn="<LI><A HREF=\"%s\">%s %s</A>" % (filename,pxDesc,scheme)
      if i==len(colour_schemes_to_generate)-1: print toPrn+"</LI>"
      else: print toPrn+","
      do_one_stylesheet(pixelSize,colour,filename)
  print "</UL></DIV>"
  print """<SCRIPT><!--
if(document.all||document.getElementById) {
var newDiv=document.createElement('DIV');
var e=document.createElement('H3'); e.appendChild(document.createTextNode('Download or Try Low Vision Stylesheets')); newDiv.appendChild(e);
newDiv.appendChild(document.createTextNode('Select your size and colour: '));
var sizeSelect=document.createElement('SELECT');
var colourSelect=document.createElement('SELECT');
newDiv.appendChild(sizeSelect); newDiv.appendChild(colourSelect);
var defaultSize=35; if(screen && screen.height) defaultSize=screen.height/18.12; // 36pt 15.1in
"""
  pixel_sizes_to_generate.sort()
  for pixelSize in pixel_sizes_to_generate:
    if pixelSize: pxDesc = str(pixelSize)+" pixels"
    else: pxDesc = "unchanged"
    print "e=document.createElement('OPTION'); e.value='"+str(pixelSize)+"'; e.appendChild(document.createTextNode('"+pxDesc+"')); sizeSelect.appendChild(e); if(defaultSize) sizeSelect.selectedIndex="+str(pixel_sizes_to_generate.index(pixelSize))+"; if(defaultSize<"+str(pixelSize)+") defaultSize=0;"
  for scheme,suffix,colour in colour_schemes_to_generate: print "e=document.createElement('OPTION'); e.value='"+suffix+"'; e.appendChild(document.createTextNode('"+scheme+"')); colourSelect.appendChild(e);"
  def tryStylesheetJS(hrefExpr): return "var e=document.createElement('link'); e.id0='ssb22css'; e.rel='stylesheet'; e.href="+hrefExpr+"; if(!document.getElementsByTagName('head')) document.body.appendChild(document.createElement('head')); var h=document.getElementsByTagName('head')[0]; if(h.lastChild && h.lastChild.id0=='ssb22css') h.removeChild(h.lastChild); h.appendChild(e);"
  # (do NOT put that in a JS function, the 1st link must be self-contained.  and don't say link.click() it's too browser-specific)
  print """
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
newDiv.appendChild(document.createTextNode("You may be able to drag the 'try stylesheet' link to your browser's Bookmarks toolbar and later press it to re-style any web page. But it might work better if you set it as a user-supplied stylesheet "));
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
//--></SCRIPT>""" # "  # (comment for emacs)
  print "(above stylesheets generated by version "+prog.split()[-1]+")"

do_binary_chop = False
binary_chop_results = ""
import sys
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
  while not do_one_stylesheet(pixel_sizes_to_generate[0],colour,"debug%04d.css" % debugStopAfter,debugStopAfter):
    print "Generated debug stylesheet debug%04d.css" % debugStopAfter
    debugStopAfter += 1
elif "chop" in sys.argv:
  do_binary_chop = True
  if not sys.argv[-1] == "chop": binary_chop_results = sys.argv[-1]
  scheme,suffix,colour = colour_schemes_to_generate[0]
  filename="%d%s.css" % (pixel_sizes_to_generate[0],suffix)
  do_one_stylesheet(pixel_sizes_to_generate[0],colour,filename)
  print "Generated debug stylesheet:",filename
else: main()
