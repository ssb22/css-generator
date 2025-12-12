
from https://ssb22.user.srcf.net/css/flipbox.html
(also [mirrored on GitLab Pages](https://ssb22.gitlab.io/css/flipbox.html) just in case)

# Why animated flip boxes are not always good
When I was asked by the proprietor of a small Mandarin language school in London to review their website in 2015, I found the Web design company they’d used had included a few troublesome features such as “flip boxes” and video-backgrounds.  The site stopped using these by 2019.

(They had in fact asked me to link to them as a favour just to get it into the search engines for the first time, and I said the only legitimate way to do that from my university-provided web space was an honest review.  I didn’t live near enough to try the school, so my review had to be about the web design.)

“Flip boxes” were apparently written as part of “Avada Theme” by a company called “Theme Fusion” but copied by many others.  If you search the Web for them, you can find the following text at several sites:

"Animated flip boxes are simply awesome.  We’ve never met anyone who doesn’t love these bad boys."

and to my astonishment, no obvious counterpoint has been published.  So as a public service, I am hereby pointing out some obvious reasons why animated flip boxes on websites can be bad design.

1. **Flip boxes can hide information.** I’m not convinced the Practical Mandarin school really wanted visitors to fail to see each course’s HSK level until they moved the mouse over the course name.  How is the visitor to know they’re ‘supposed’ to do that?  Is the visitor required to move the mouse everywhere just to see what happens?  This borders on what Vincent Flanders called “mystery meat navigation”, except that at least the flip boxes do contain some information on the ‘front’ (but they give no obvious clue that more information can be found ‘behind’).
2. **Flip boxes don’t work without a mouse.** At least some web designers have the sense to change tack when the site detects a mobile device is in use, but is that detection mechanism guaranteed to *always* find out if the user lacks a mouse?  What if the user is on a *tablet* and it’s a type that wasn’t listed in the detection logic?  (Even if you don’t care about devices that few people use, are you sure you’ll be able to keep that detection logic up-to-date with the “next big thing” when it comes out?)
3. **Flip boxes don’t allow their ‘front side’ to be copied.** Suppose the visitor is browsing a site that is not written in their own language, and wants to use dictionary software on some of the words.  They won’t be able to use their mouse to copy and paste the information on the front of the ‘flip box’ if that box flips over as soon as they get anywhere near it.  There are ways of working around this, but it’s likely to be frustrating.
4. **Flip boxes can interact badly with user stylesheets.** The information is generally visible in a text-mode browser such as Lynx, but if you use a graphical browser with a user-supplied stylesheet that doesn’t override all of the relevant transform and transform-style CSS rules, you’ll likely end up with very ‘messy’ interaction.  My own stylesheets for low vision in this repository have of course been updated to override all transform rules when changing the layout.

I hope that web designers can think more carefully about how they use these things in future.  I feel partly responsible, because I was involved in the W3C WAI panel, and perhaps I should have foreseen this and said something when the W3C were writing up the CSS 3 specifications that made flip boxes possible.  But I failed to spot it at that time.  Sorry, world.
