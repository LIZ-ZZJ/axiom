width=int(1280)
height=int(720)

screenwidth=float(input())

railwidth=2.5

space=round(railwidth/screenwidth*width)
halfs=space/2
notex=space*0.8
notey=notex*0.25
holdhitspace=18.75/200*notex

print('@define space {}'.format(space))
print('@define halfs {:.1f}'.format(halfs))
print('@define notex {:.1f}'.format(notex))
print('@define notey {:.1f}'.format(notey))
print('@define holdhitspace {:.1f}'.format(holdhitspace))
