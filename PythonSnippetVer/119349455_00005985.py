import urllib, os
link = "http://python.org"
print "opening url:", link
site = urllib.urlopen(link)
meta = site.info()
print "Content-Length:", meta.getheaders("Content-Length")[0]

f = open("out.txt", "rb")
print "File on disk:",len(f.read())
f.close()


f = open("out.txt", "wb")
f.write(site.read())
site.close()
f.close()

f = open("out.txt", "rb")
print "File on disk after download:",len(f.read())
f.close()

print "os.stat().st_size returns:", os.stat("out.txt").st_size