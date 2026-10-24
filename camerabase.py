from PIL import Image
import cv2
im = cv2.videocapture(0)
res = im.resize((50,50))
px = res.load()

ww, hh = res.size
for h in range(hh):
    print('')
    h+1
    for w in range(ww):
        w+1
        r, g, b = px[w, h]
        print(f'\033[38;2;{r};{g};{b}m@\033[0m', end='')


        

