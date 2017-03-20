#coding=utf-8

from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def getstr(r,g,b,alpha=256):
    if alpha==0:
        return ' '
    lens=len(ascii_char)
    gray=int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit=257.0/lens
    char=ascii_char[int(gray/unit)]

    return char

if __name__ == '__main__':
    picture_name=raw_input('please input picture name---->')
    size=raw_input('please input size you want like 30x30 or enter to default---->')
    a=size.split('x')
    width=int(a[0]) if size else 40
    height=int(a[1]) if size else 40
    im=Image.open(picture_name)
    im=im.resize((width,height),Image.NEAREST)

    txt=''

    for i in range(width):
        for j in range(height):
            txt+=getstr(*im.getpixel((j,i)))
        txt+='\n'

    print txt

    with open('output.txt','w') as e:
        e.write(txt)
        e.close()
