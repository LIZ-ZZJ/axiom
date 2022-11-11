import os
from PIL import Image, ImageFont, ImageDraw

fpath = "C:\\Windows\\Fonts\\CascadiaCode.ttf"
fsize = 250
font = ImageFont.truetype(fpath, fsize)

f=open('input.txt', 'r')
text = f.read().split('\n')

ims=[]
boxs=[fsize*3,fsize*3,0,0]

for word in text:
    length = len(word)
    img = Image.new("RGBA", ((fsize * length*3),
                    (fsize*3)), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((fsize * length,fsize), word, font=font, fill="#ffffff")
    bbox=img.getbbox()
    boxs[0]=min(boxs[0],bbox[0])
    boxs[1]=min(boxs[1],bbox[1])
    boxs[2]=max(boxs[2],bbox[2])
    boxs[3]=max(boxs[3],bbox[3])
    ims.append(img)

for i in range(12):
    ims[i].crop((boxs[0]-12,boxs[1]-12,boxs[2]+12,boxs[3]+12)).save('axiom-texture-'+str(i)+'.png')
