import os
import tinify
import re
tinify.key = "0l5xWNcBWV6gNQxWdXmYXpZspMxhWgVB"
pat=re.compile(r'.*\.png')
for root, dirs, files in os.walk('./',topdown=False):
    for name in files:
        filen=os.path.join(root,name)
        if(pat.match(filen)):
            print(filen)
            source = tinify.from_file(filen)
            source.to_file(filen)
