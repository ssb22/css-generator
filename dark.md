
from https://ssb22.user.srcf.net/css/dark.html
(also [mirrored on GitLab Pages](https://ssb22.gitlab.io/css/dark.html) just in case)

# Advantages of dark backgrounds on computer displays
* Eye fatigue from video glare is reduced
* Flicker problems (if they exist) are reduced by dark backgrounds
* Some medical conditions (e.g. photophobia) are less aggravated by dark backgrounds
* Colours, when used to convey information like syntax highlighting, might be easier to notice against a dark background
* Less blue light could mean less disruption to the body’s sleep cycle if using the display in the evening
* On some displays, dark colours save electricity
  * and since darker displays are more suitable for use in dimly-lit rooms, the lighting can take less electricity too
* Defective pixels that are permanently dark can cause less confusion if the background is dark
  * and if, after an accident, the display still works but a digitiser (“touch”) or other layer in front of it is cracked, then this might be less noticeable against a dark background, hence allowing more time between repairs or replacements
* If the display is surrounded by a dark border, then bright text can touch its very edge without causing confusion, unlike dark text which may need a margin (dark lines running along a black edge won’t stand out), therefore light text on a dark background can make better use of space during full-screen presentations etc 

## When dark backgrounds are *not* good
* When the display is reflective (not backlit)
* When the display is backlit but there is a lot of ambient light on it that would disturb a dark background (for example using a laptop or projector in a well-lit room)
* When the fonts are too small or thin (which is hopefully not the case when large or giant print is in use)
* On some mobile displays in some lighting conditions, scratches from accidental drops etc are more visible against dark backgrounds.  (But in other cases the reverse is true.) 

Unfortunately people are sometimes forced to use light backgrounds for software-only reasons, since not all software has been properly constructed to work in a dark background (and some “high-end” websites do not function well when [accessibility CSS files](README.md) are applied); hopefully more developers can be made aware of the need to construct things in a “customisation-friendly” way.

## References
Due to the shortage of rigorous scientific studies on the subject, the above is mostly based on my own experience and that of other people I’ve met (with various sight conditions)—I’ve been focusing on technical ways to *enable* dark backgrounds rather than on the proof that we need them.  But I have collected a few citations if this helps:

* F. L. Van Nes (1986).  Space, colour and typography on visual display terminals.  Behaviour & Information Technology, 5:2, 99-118.
  * From the CRT era, says “on displays with a 50 or 60 Hz refresh rate, as employed in videotex systems, high-luminance backgrounds show annoying flicker effects, especially when large areas are involved.”  (Section 4.1.1, page 105)
* F. L. Van Nes (1984).  Limits of visual perception in the technology of visual display terminals.  Behaviour & Information Technology, 3:4, 371-377.
  * Again from the CRT era, mentions the problem of ambient light disturbing a dark background (Section 2.1), cites an earlier study on refresh rates (The influence of field repetition frequency on the visibility of flicker on displays, Van der Zee and Van der Meulen, 1982), some discussion of contrast, and cites a couple of early studies on colour-coded text (Section 5)
* N. E. Tanton (1979).  UK Teletext—Evolution and Potential.  IEEE Transactions on Consumer Electronics, CE-25:3, 246-250.
  * Regarding the display of text on televisions of the 1970s, mentions “In the first experiments, all text was displayed as white...on a black background” with other background options added later.  Unfortunately does not explain the reasoning behind this decision.
* E. A. Moulton, L. Becerra and D. Borsook (2009).  An fMRI case report of photophobia: Activation of the trigeminal nociceptive pathway.  Pain 145:3, 358-363.
  * To inflict pain on their photophobic subject, the researchers used presentation software to change from a dark-background slide to a white-background slide.
* M. Johns (1995).  Design for slides.  Journal of Audiovisual Media in Medicine 18:3.
  * I do not have full-text access to this one, but it mentions white-background slides causing viewer fatigue in some circumstances.
