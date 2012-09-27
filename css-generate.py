prog="Accessibility CSS Generator, (c) Silas S. Brown 2006-2012.  Version 0.9788"

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
# http://e-guidedog.svn.sourceforge.net/viewvc/e-guidedog/ssb22/css-generator/
# as of v0.9782.  Versions prior to that were not kept, but
# you might be able to find some on Internet Archive.

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
# sizes.  This is for people who only need new colours.

pixel_sizes_to_generate = [0,18,20,25,30,35,40,45,50,60,75,100]
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
    "selection":"#0080c0", # (for CSS3, ignored by 1 and 2)
    "highlight":"#003050",
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

# TODO why do some sites still have iframes that obscure the text

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
    
    "*-moz-appearance":"none",
    "*-moz-transform":"none",
    "*-webkit-transform":"none",
    }

  # have to explicitly set for every type of element,
  # because wildcards don't always work and inheritance can
  # be overridden by author stylesheets resulting in poor
  # combinations.  NB however we don't list ALL elements in
  # mostElements (see code later).
  mostElements="a,blockquote,caption,center,cite,code,col,colgroup,html,iframe,pre,body,div,p,input,select,option,textarea,table,tr,td,th,h1,h2,h3,h4,h5,h6,font,basefont,small,big,span,ul,ol,li,i,em,s,strike,nobr,tt,kbd,b,strong,dl,dt,dd,blink,button,address,dfn,form,marquee,fieldset,legend,listing,abbr,q,menu,dir,multicol,img,plaintext,xmp,label,sup,sub,u,var,acronym,object,embed,canvas".split(",")
  html5Elements = "article,aside,bdi,command,details,summary,figure,figcaption,footer,header,hgroup,mark,meter,nav,progress,section,time".split(",") # (and ruby/rt/rp/rb)
  mostElements += html5Elements
  
  css={}
  for e in mostElements: css[e]=defaultStyle.copy()

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
  for e in ["frame","iframe"]: css[e]["*overflow"]="auto /* overrides 'scrolling=no' which can go wrong in large print */ "

  css["sup"]["*vertical-align"] = "super /* in case authors try to do it with font size instead */"
  css["sub"]["*vertical-align"] = "sub"

  css["marquee"]["*-moz-binding"]="/* make sure firefox doesn't scroll marquee elements */ none"
  css["marquee"]["*display"]="block"

  css["center"]["*text-align"] = "center"
  
  for s in ['s','strike']: css[s]["*text-decoration"]="line-through"
  # TODO: not sure if really want this for the 's' alias of 'strike', since some sites e.g. http://www.elgin.free-online.co.uk/qp_intro.htm (2007-10) use CSS to override its presentation into something other than strikeout

  # Margin exceptions:

  css["body"]["*margin"]="/* keep away from window borders */ 1ex %.1fpx 1ex %.1fpx" % (pixelSize*5/18.0,pixelSize*5/18.0)

  for i in "p,multicol,listing,plaintext,xmp,pre".split(","): css[i]["*margin"]="1em 0"
  
  listStuff="ul,ol,dir,menu,dl,li".split(",")
  for l in listStuff:
    css[l]["*margin"]="0 1em 0 %.1fpx" % (pixelSize*10/18.0)
  listStuff.remove("li")
  for l in listStuff:
    for l2 in listStuff:
      css[l+" "+l2]={"*margin":"0px"}
  
  css["blockquote"]["*margin"]="1em 4em"
  css["blockquote[type=cite]"]={"*margin":"1em 0px","*padding":"1em 0px 0px 0px"}
  css["dd"]["*margin"]="0em 2em"
  
  for t in ["th","td"]: css[t]["*padding"]="%.1fpx" % (pixelSize/18.0,)
  
  # Don't say white-space normal on user input elements or pre
  # Galeon 1.25: we also have to exclude "body" and "div" for some reason
  # TODO: is it REALLY a good idea to leave 'div' on this list?
  for e in "pre,input,textarea,body,div".split(","): del css[e]["*white-space"]
  for e in "font,code".split(","): css["pre "+e]={"*white-space":"inherit"} # some mailing lists etc have "font" within "pre", and some sites have "code" within "pre"
  
  # Monospaced elements
  for t in "pre,code,tt,kbd,var".split(","): css[t]["*font-family"]="monospace"
  
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
    # and now (AFTER the above) set margins on headings
    css[el]["*margin"]="0px 0px 0px %.1fpx" % indent

  # Links stuff:
  for linkInside in ",font,big,small,basefont,br,b,i,u,em,strong,abbr,span,div,code,tt,kbd,var,acronym,h1,h2,h3,h4,h5,h6".split(","):
    for type in [":link",":visited","[onclick]"]:
      css["a"+type+" "+linkInside]={"color":colour["link"],"text-decoration":"underline","cursor":"pointer"}
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
    css[i]["*font-family"]="helvetica, arial, verdana"
    css[i]["color"]=colour["italic"]
  for i in "b,strong".split(","):
    css[i]["*font-weight"]="bold"
    css[i]["color"]=colour["bold"]
  css["acronym"]["color"]=colour["bold"]

  # Images and buttons:
  css["img"]["background"]=colour["image_transparency_compromise"]
  
  # Exception needed for MediaWiki TeX images
  # (they tend to be transparent but with antialiasing that
  # assumes the background will be white)
  css["body.mediawiki img.tex"]={"background":"white"}
  # (note however it might be possible to set the wiki to
  # display maths as real TeX or something instead)
  
  if "image_opacity" in colour:
    del css["img"]["*opacity"],css["img"]["*-moz-opacity"],css["img"]["*filter"]
    css["img"]["opacity"]=css["img"]["-moz-opacity"]="%g" % colour["image_opacity"]
    css["img"]["filter"]="alpha(opacity=%d)" % int(colour["image_opacity"]*100) # for IE8 and below
    if colour["image_opacity"]<0.9: css["img:hover"] = css["a:hover img"]={"opacity":"0.9","-moz-opacity":"0.9","filter":"alpha(opacity=90)"}
  
  css["button"]["background"]=colour["button"]
  css['div[role="button"]']={"background":colour["button"]} # for Gmail 2012-07 on "standard" view (rather than "basic HTML" view).  "Standard" view might work for people who want the "unchanged" size.
  if "alt-backgrounds" in colour: css['html body div[role="button"]'] = css['div[role="button"]'] # override specificity of alt-backgrounds div:nth-child
  css["input[type=submit]"]={"background":colour["button"]}
  css["input[type=button]"]={"background":colour["button"]}
  css["input[type=reset]"]={"background":colour["reset_button"]}
  for dType in ['[disabled="disabled"]','.disabled']:
    for f in ["select","input","textarea","button"]:
      css[f+dType]={"background":colour["form_disabled"]}
  
  # Separate adjacent links (CSS2+)
  if (pixelSize and separate_adjacent_links_at_other_sizes) or (not pixelSize and separate_adjacent_links_at_size_0):
    for l in [":link",":visited","[onclick]"]:
      css[":not(:empty) a"+l+":before"]={"content":'"["',"color":colour["text"],"text-decoration":"none","white-space":"nowrap"}
      css[":not(:empty) a"+l+":after"]={"content":'"]"',"color":colour["text"],"text-decoration":"none","white-space":"nowrap"}

  # Avoid style overrides from :first-letter, :first-line,
  # :before and :after in author's CSS.  However be careful
  # which elements you do this because of browser bugs.
  firstLetterBugs=[
   "div", # Gecko messes up textarea when enter multiple paragraphs
  "input","select","option","textarea","table","colgroup","col","img", # probably best to avoid these
  "a", # causes problems in IE
  # the following cause text selection visibility problems in Webkit / Safari 5/6 (cannot be worked around with :first-letter::selection)
  # (+ Chrome 12 bug - OL/LI:first-letter ends up being default size rather than css size; harmless if have default size set similarly anyway)
  # TODO: allow them in Gecko via a Gecko-specific rule?  especially (e.g.) "p"
  "label","address","p","ul","li","pre","code","body","html","h1","h2","h3","h4","h5","h6","form","th","tr","td","dl","dt","dd","b","blockquote","section"
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
    for i in map(lambda x:":not(:empty) "+e+x,[":before",":after"]):
      css[i]=defaultStyle.copy()
      del css[i]["*margin"]
      del css[i]["*padding"]
  
  # CSS 2+ markup for viewing XML+CSS pages that don't use HTML.  Not perfect but should be better than nothing.
  xmlKey=":root:not(HTML), :root:not(HTML) :not(:empty)"
  # Careful not to use the universal selector, because it can mess up Mozilla's UI
  css[xmlKey]=defaultStyle.copy()
  del css[xmlKey]["*text-decoration"] # because this CSS won't be able to put it back in for links (since it doesn't know which elements ARE links in arbitrary XML)
  # Exception to above for Mozilla scrollbars:
  css[":root:not(HTML) slider:not(:empty)"]={"background":"#301090"}

  if pixelSize:
    # In many versions of firefox, a <P ALIGN=center> with an <IFRAME> inside it will result in the iframe being positioned over the top of the main text if the P's text-align is overridden to "left".  But missing out text-align could allow websites to do full justification.  However it seems OK if we override iframe's display to "block" (this may make some layouts slightly less brief, but iframes usually need a line of their own anyway)
    css["iframe"]["*display"]="block"
    # and if we're doing that, we might as well use the full width:
    css["iframe"]["*width"]="100%"
    # The following may help a little as well: make iframes 50% transparent so at least we can see what's under them if they do overprint
    # (the overprinting does still happen on some sites; apparently the IFRAME's height is treated as close to 0 when it's not)
    css["iframe"].update({"*filter":"alpha(opacity=50)","*opacity":"0.5","*-moz-opacity":"0.5"})

  # Selection (CSS3)
  if colour.has_key("selection"):
    css["::selection"] = {"background":colour["selection"]}
    css["::-moz-selection"] = {"background":colour["selection"]}

  css['input[type=search]'] = {"-webkit-appearance":"textfield"} # searchbox forces background:white which may conflict with our foreground
  
  css['select']['-webkit-appearance']='listbox' # workaround for Midori Ubuntu bug 1024783
  css['select']['background']=colour['selectbox']

  # Remove '*' as necessary:
  for el in css.keys()[:]:
    for prop,value in css[el].items()[:]:
      if prop[0]=='*':
        del css[el][prop]
        if pixelSize: css[el][prop[1:]] = value
    if css[el] == {}: del css[el]

  if "alt-backgrounds" in colour:
    css['td:nth-child(odd),div:nth-child(odd)'] = {"background":colour["alt-backgrounds"][0]}
    if len(colour["alt-backgrounds"])>1:
      css['td:nth-child(even),div:nth-child(even)'] = {"background":colour["alt-backgrounds"][1]}
    for k in css.keys():
      if css[k].get("background","")==colour["background"] and not k in ["html","body"]: css[k]["background"]="inherit"
  
  # Text for the beginning of the CSS file:
  
  outfile.write("@import url(chrome://flashblock/content/flashblock.css);\n") # Needs to be on first line for Firefox + flashblock plugin (ignored if not present)

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

@media print { * { color: black !important; } } /* in browsers that do not support @media, this will be overridden by the items below */

@media screen,projection,tv {

/* :not(:empty) stops IE5+6 from misinterpreting things it can't understand */

/* Repeat ALT tags after images (problematic; see Mozilla bug 292116)
(2005: commenting this out for now because more trouble than it's worth;
only Mozilla 1.0 does it properly; later versions and Firefox don't)
img[alt]:after { content: attr(alt) !important; color: #FF00FF !important; }
*/\n""")

  ret = printCss(css,outfile,debugStopAfter)
  # Begin site-specific hacks - at end of CSS
  # Hack for Wikipedia/MediaWiki diffs (diffchange) and Assembla diffs (was, now) and Sourceforge (vc_)
  outfile.write(".diffchange, .was, .now, .vc_diff_change, .vc_diff_remove, .vc_diff_add, .wDiffHtmlDelete, .wDiffHtmlInsert { color: "+colour["italic"]+" !important;}\n")
  outfile.write(".wDiffHtmlDelete { text-decoration: line-through !important; }\n")
  # Hack for WP/MediaWiki unedited links:
  outfile.write("a.new { color: "+colour["coloured"]+" !important; }\n") # (TODO use a different colour?)
  # and the navpopup extension: (also adding ul.ui-autocomplete to this, used on some sites)
  outfile.write("body.mediawiki > div.navpopup,body.mediawiki .referencetooltip, ul.ui-autocomplete{position:absolute!important;border:blue solid !important;}")
  # Hack for Vodafone UK's login 2012 (stop their mousein/mouseout events going crazy with our layout)
  if pixelSize: outfile.write("ul#MUmyAccountOptions { display: block !important; }")
  # Hack for some authoring tools that use <FONT COLOR=..> to indicate special emphasis
  outfile.write("font[color] { color: "+colour["coloured"]+" !important;}\n")
  # and others that use span class="Apple-style-span"
  outfile.write("span.Apple-style-span { color: "+colour["coloured"]+" !important;}\n")
  # Hack for pinyinannotator
  if pixelSize: outfile.write("""
div.interlinear tt { display: inline-table !important; line-height: 1.02 !important; text-align: center !important; padding: 0.3em !important; }
div.interlinear tt i { display: table-row-group !important; text-align: center !important; }
div.interlinear tt i.line1 { display: table-header-group !important; text-align: center !important; color: """+colour["headings"]+""" !important; }
div#container div#result tt { display: inline-table !important; line-height: 1.02 !important; text-align: center !important; padding: 0.3em !important; }
div#container div#result tt > i { display: table-header-group !important; text-align: center !important; }
div#container div#result tt > b, div#container div#result tt > acronym { display: table-row-group !important; text-align: center !important; }
""")
  # hack for messages on some sites
  outfile.write("tr.new td { border: thick solid "+colour["coloured"]+" !important;}\n")
  # hack for (some versions of) phpBB
  outfile.write("ul.profile-icons li span {display:inline !important;}")
  # hack for embedded Google Maps. 2012-07 Google Maps iframe with certain settings + Safari + CSS = consume all RAM and hang; many sites use GM to embed a "how to find us" map which isn't always the main point of the page, so turn these off until we can fix them properly; in the meantime if you want to see Google Maps you have to turn off this stylesheet (which you'd have to do ANYWAY even without this hack if you want to get any sense out of the maps, unless we can figure out how to give them enough layout exceptions)
  if pixelSize: outfile.write("body.kui > div#main > div#inner > div#infoarea + div#page > /*div#le-container + div +*/ div#main_map { display: none !important; }")
  
  # hack for MHonarc and similar setups that put full-sized images into clickable links
  # (see comments on max-width above; doesn't seem to be a problem in this instance)
  # if pixelSize: outfile.write("a:link img,a:visited img { max-width:100% !important;max-height:100% !important;}")
  # -> DON'T do this - if one dimension is greater than 100% viewport but other is less, result can be bad aspect ratio
  
  # hack for sites that use jump.js with nav boxes
  jjc = "body > input#rsconf + div#wrapper > div#header + div#container > div#spacer + "
  # wrapper might or might not be .dropShadow50
  jjSN = jjc + "div#secondaryNav"
  jumpjsContent = jjc+"div#content," +jjSN+" + div#content"
  jumpjsTooltip = "div.tooltip.dropShadow20"
  outfile.write(jumpjsTooltip+" {border:thin solid "+colour["italic"]+"!important;}")
  if pixelSize: outfile.write(jumpjsTooltip+""" {position:absolute !important;z-index:9!important;}
"""+jumpjsTooltip+""" p,"""+jumpjsTooltip+""" div.par { margin: 0px !important; padding: 0px !important; }
div.document > div.par > p.sl,div.document > div.par > p.sz { margin: 0px !important; padding: 0px !important; }
body > input#rsconf + div#wrapper > div#header { height:40%!important/*no more or scroll-JS is too far wrong*/;position:fixed !important;top:0px!important;right/*not left or overflow problems, + right helps w. tooltips*/:0px!important;width:30%!important/*not fixed+100% or PgDn will go wrong*/;overflow:auto!important;border:blue solid!important;z-index:1!important;}
"""+jumpjsContent+"""{margin-right:30%!important;z-index:0!important;}
""" + jjSN + """{ position:fixed !important;/*or double-scroll JS fails*/bottom:0px;right/*not left,see below*/:0px;width:30%!important;height:60%!important;border:blue solid!important;overflow:auto!important;z-index:2!important;}""")
  # and not just if pixelSize (because these icons aren't necessarily visible with our colour changes) -
  outfile.write(""":not(:empty) li#menuNavigation.iconOnly > a > span.icon:after { content: "Navigation"; text-transform: none; }
:not(:empty) li#menuSearchHitNext.iconOnly > a > span.icon:after { content: "Next hit"; text-transform: none !important; }
:not(:empty) li#menuToolsPreferences.iconOnly > a > span.icon:after { content: "Preferences"; text-transform: none; }
:not(:empty) div.resultNavControls > ul > li.resultNavLeft > a > span:after { content: "<- Prev"; text-transform: none; }
:not(:empty) div.resultNavControls > ul > li.resultNavRight > a > span:after { content: "Next ->"; text-transform: none; }
:not(:empty) div.resultNavControls > ul > li.resultNavDoubleLeft > a > span:after { content: "<<- Backwd"; text-transform: none; }
:not(:empty) div.resultNavControls > ul > li.resultNavDoubleRight > a > span:after { content: "Fwd ->>"; text-transform: none; }
""")
  outfile.write(jumpjsContent.replace(","," span.hl,")+""" span.hl{background: """+colour['highlight']+""" !important;}
div.result > div.document span.mk,div.result > div.document span.mk b, div.par p.sb span.mk, div.par p.ss span.mk b { background: """+colour["reset_button"]+""" !important; }
""")
  # if pixelSize: outfile.write(":not(:empty) input#rsconf + div#wrapper > div#header > div#menuFrame > ul.menu > li:before { content: attr(id); text-transform: none; display: inline !important; }\n")
  outfile.write(".menu li a span.label { display:inline !important; text-transform: none !important;}\n") # not just 'if pixelSize', we need this anyway due to background overrides
  # some site JS adds modal boxes to the end of the document, try:
  outfile.write("body.yesJS > div.fancybox-wrap[style] { position: absolute !important; border: blue solid !important; } body.yesJS > div.fancybox-wrap[style] div.fancybox-close:after { content: \"Close\"; }\n")
  # hack for sites that embed YouTube videos (NASA etc) when using the YouTube5 Safari extension on a Mac
  outfile.write("div.youtube5top-overlay,div.youtube5bottom-overlay,div.youtube5info,div.youtube5info-button,div.youtube5controls { background-color:transparent!important;background:transparent!important;}\n")
  # End site-specific hacks
  outfile.write("input[type=text],input[type=password],input[type=search] { border: 1px solid grey !important; }") # TODO what if background is close to grey?
  # 'html' overflow should be 'visible' in Firefox, 'auto' in IE7.
  if pixelSize: outfile.write("html:not(:empty) { overflow: visible !important; }\n")
  # speed up scrolling on Midori (from their FAQ) -
  outfile.write("* {-webkit-box-shadow: none !important;}\n")
  # help Opera 12 and other browsers that don't show keyboard focus -
  outfile.write(":focus { outline: "+colour.get("focusOutlineStyle","thin dotted")+"; }\n")

  outfile.write("} /* end of @media block */\n")
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
  # For each attrib:val find which elems share it & group them
  rDic={} # maps (attrib,val) to a list of elements that have it
  for elem,attribValDict in css.items():
    # add aliases before starting
    if attribValDict.has_key("background") and not attribValDict.has_key("background-color"): attribValDict["background-color"]=attribValDict["background"]
    # end of adding aliases
    for i in attribValDict.items():
      if not rDic.has_key(i): rDic[i]=[]
      rDic[i].append(elem)
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
    elemList_ie = filter(lambda x:not '*' in x and not '>' in x and not ':not' in x and not '[' in x, elemList)
    elemList_rest = filter(lambda x:x not in elemList_ie, elemList)
    for eList in [elemList_ie, elemList_rest]:
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
    outfile.write(fill(", ".join(elemList).replace("-","#@#"),break_long_words=False).replace("#@#","-")) # (don't let 'fill' break on the hyphens)
    outfile.write(" {\n")
    l=style.items() ; l.sort()
    for k,v in l: outfile.write("   %s: %s !important;\n" % (k,v))
    outfile.write("}\n")
  return debugStopAfter

def main():
  print "<DIV id=pregen_download><H3>Download pre-generated low-vision stylesheets</H3><NOSCRIPT>(If you switch on Javascript, there will be an interactive chooser here.&nbsp; Otherwise you can still choose manually from the links below.)</NOSCRIPT><SCRIPT LANGUAGE=Javascript><!-- \ndocument.write('Although Javascript is on, for some reason the interactive chooser failed to run on your particular browser. Falling back to the list below.'); //--></SCRIPT><BR><UL>"
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
  print """<SCRIPT language=Javascript><!--
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
if "desperate-debug" in sys.argv:
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
