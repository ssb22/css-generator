
from https://ssb22.user.srcf.net/css/gopher.html
(also [mirrored on GitLab Pages](https://ssb22.gitlab.io/css/gopher.html) just in case)

# Gopher protocol considered inferior
As a partially-sighted computer scientist, I’m sometimes asked for an opinion on little-known technologies that might seem to make things easier for blind or partially-sighted people.  Gopher was an early-1990s alternative to the then-emerging World Wide Web, and some enthusiasts think it must be better because it is text-based.  Although Gopher can deliver graphics and other files, it’s usually used for plain-text files and separate lists of links.  But there are problems:

1. Gopher is less likely to properly display non-English languages that are not written in ASCII;
2. Gopher pages seem more likely to use “ASCII art”, which confuses screen readers and cannot even be skipped like HTML images can;
3. Gopher pages are typically not designed to be reflowed to less than 70 columns for giant-print and small-device situations, nor to be displayed in a proportional font (the size-changing versions of my low-vision stylesheets tell Firefox’s “OverbiteFF” Gopher plug-in to use a proportional font, which helps on many Gopher pages but does break some).

After I wrote the above, some Gopher enthusiasts developed a new protocol called Gemini which largely addresses these things.  Gemini is UTF-8 compatible and wraps text to the window width.  It can also set language tags to help speech synthesisers select the correct pronunciation, although all languages used on the page are listed in the protocol header rather than in the markup, so the synthesiser still has to work out where the use of each language begins and ends (unless they start using Unicode 3.1’s deprecated `U+E0001` ‘language tag’ for this).  Gemini’s ‘preformatted’ regions can still contain ASCII art, but clients like Ariane/Seren can collapse these regions by default.

Enthusiasts of the *original* Gopher protocol sometimes point to its being more ‘lightweight’ than Gemini and the Web’s HTTP, because Gopher is “headerless” whereas Gemini carries uncompressed TLS overhead and HTTP adds headers to each transaction.  The rest of this page discusses Gopher’s claim of being lightweight.

## HTTP headers actually save traffic
It may be surprising that adding more headers can save traffic, but it can.  Consider, HTTP/1.0 and HTTP/1.1 has:

* protocol-level compression—useful for all but the smallest responses, unless the file is already compressed, or unless sufficient compression is being performed on the underlying stream of packets
* partial downloads and continuation (called “byte serving” or “range requests” in HTTP 1.1)—so if a connection fails during a large download then it doesn’t have to be started again from the beginning
* keep-alive and pipelining—useful when many small requests will be made in a short time (although browser support for pipelining was patchy before HTTP2 over TLS, but keep-alive still helped)
* expiry and caching information—so browsers often won’t need to re-fetch something a second time.  My old Web Access Gateway’s image server for CJK characters absolutely depended on this for its apparent speed: if I’d used HTTP/0.9 or Gopher to serve those images, the user experience would have been slower despite there being fewer bytes per response.

So the actual traffic-saving advantage of headerless protocols exists only for a *one-off* access to a *single* and *very small* file.

## Headerless responses do not require Gopher
If you do need one-off access to a single very small file and would genuinely benefit from a headerless response, this can also be obtained using:

1. the original “HTTP/0.9”, which pre-dates Gopher and costs just 4 extra bytes—less if Gopher’s oft-omitted terminating full-stop line is counted against it
  * HTTP/0.9 continued to be supported by most HTTP servers in subsequent years, so if you ran a standard HTTP server (and hadn’t set it to rely on a “virtual hosts” configuration or insist on HTTPS) then you could obtain headerless responses from it, without having to either run an additional server or restrict your choice of HTTP server to one that can also handle Gopher requests.
  * However in 2014 HTTP/0.9 was officially made optional (RFC 7230 Appendix A) although many servers continued to support it.
  * In mid-2016 support began to be removed from mainstream browsers (which would in any case not have used HTTP/0.9 unless the server *forced* it: requesting it from the client side requires manual control of the transfer)—but as mainstream browsers no longer support the Gopher protocol either, it’s rare to be using a system that has a Gopher-capable browser but no `telnet` or `nc` to issue an HTTP/0.9 request (and you can write scripts to avoid having to type the full command each time).  For the record, in 1998 my Access Gateway *assumed* an HTTP/1 header would be sent; it would have failed if some server had sent it an HTTP/0.9 response, but I didn’t notice because I never encountered an HTTP/0.9-only server even back in 1998.
2. Dedicated TCP ports that return small responses, like `daytime` (port 13) and `qotd` (port 17), often run from `inetd` or similar.  These can require no request at all, which means:
  * they require *fewer* keystrokes than Gopher servers if you’re typing into `telnet` or `nc`
  * they can still be made into Gopher links (compare `lynx gopher://localhost:13` with `nc localhost 13` or `telnet localhost 13` if your machine runs the `daytime` service), and they can even be made into HTTP links if the browser still displays HTTP/0.9-style responses
  * they would however be discovered by anyone who runs a port probe, whereas a link that is not known to the public would require packet sniffing to see, so you probably don’t want to use the “dedicated open port” approach to implement something like “poor-man’s port knocking” for an SSH server—but if *that’s* your application then you’ll find the overhead of the SSH negotiations dwarfs that of an HTTP request.

If you’re typing into a Telnet client by hand on a mobile phone that charges you for every byte, then it’s likely that each keystroke will end up in a separate TCP packet (not to mention the echo), in which case you’d probably be better off either using an off-the-shelf HTTP browser to send the request all at once, or else using a custom port that doesn’t require a request at all (if you don’t mind the information also being available to anyone who runs a port probe, and you don’t need to make *too* many different types of information available in this way).

## Example custom inetd entries for small responses
* A “what is my IP address?” service on port 2
  (the Python script has to be written without
  spaces if you want to inline it into
  `/etc/inetd.conf`):
  `2 stream tcp nowait nobody /usr/bin/python2 python2 -c i=__import__;a=i('sys');b=i('socket');s=b.fromfd(a.stdin.fileno(),b.AF_INET,b.SOCK_STREAM);s.sendall(s.getpeername()[0]+'\n')`

* Report uptime and system load on port 3:
  `3 stream tcp nowait nobody /usr/bin/uptime uptime`

* Serve a small text file on port 4:
  `4 stream tcp nowait nobody /bin/cat cat /weather.txt`

## Conclusion
I won’t go into silly nationalistic squabbles about the Web being invented by a Brit working in Europe whereas Gopher was American—if anyone feels tempted to use Gopher’s general inability to display non-English languages as an anti-American joke, please remember that quite a few Americans were involved in designing Unicode and other multilingual standards, so they’re not all ignorant.  There are also potential political points about Gopher having had stricter licensing in its early years, but America isn’t the only place with plenty of lawyers and they did eventually GPL it.  But it does seem that the Gopher protocol would fall on technical points alone, and that its enthusiasts would be better off promoting low-bandwidth and “text-friendly” websites, or perhaps using Gemini if they want the thrill of building something simpler than the Web (after all some people still like amateur radio even though we now have advanced mobile phone networks).

## Copyright and Trademarks
All material © Silas S. Brown unless otherwise stated.
CJK was a registered trademark of The Research Libraries Group, Inc. and subsequently OCLC, but I believe the trademark has expired.
Firefox is a registered trademark of The Mozilla Foundation.
Gemini is a trademark of Google LLC when used in the context of LLMs.
Python is a trademark of the Python Software Foundation.
Unicode is a registered trademark of Unicode, Inc. in the United States and other countries.
Any other trademarks I mentioned without realising are trademarks of their respective holders.
