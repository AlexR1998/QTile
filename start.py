import os
from random import randint

imgs=os.listdir("/home/alex/Images/wallpapers")
si=imgs[randint(0,len(imgs)-1)]
cmd=[
        "setxkbmap latam",
        "feh --bg-fill /home/alex/Images/wallpapers/"+si,
        "picom --experimental-backends &",
    ]

for x in cmd:
    os.system(x)
