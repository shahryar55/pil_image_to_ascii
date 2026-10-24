from PIL import Image

im = Image.open("image.jpg")
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


        

