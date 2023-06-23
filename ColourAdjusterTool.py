from PIL import Image
import argparse
from pathlib import Path

def getsection(image, num):
    width, height = image.size
    shift = (height/4) * num
    return image.crop((0, shift, width, height/4 + shift))

def setsection(image, paste, num):
    height = image.size[1]
    shift = int((height/4) * num)
    image.paste(paste, (0, shift))
    return image

def setcolour(image, colour):
    rgb = image.split()
    for i in range(3):
        rgb[i].paste(rgb[i].point(lambda x: colour[i]))
    return Image.merge(image.mode, rgb)

def processimg(image, colour):
    base = getsection(image, 0)
    hover = getsection(image, 2)

    base = setcolour(base, colour)
    hover = setcolour(hover, colour)

    image = setsection(image, base, 0)
    image = setsection(image, hover, 2)
    return image

def findimgs(root):
    images = []
    for path in root.iterdir():
        if path.is_file():
            images.append(path)
        else:
            images.extend(findimgs(path))
    return images

def processall(imagepaths, colour, savedir):
    for impath in imagepaths:
        image = Image.open(str(impath))
        image = processimg(image, colour)
        savepath = savedir.joinpath(impath.relative_to(impath.parts[0]))
        savepath.parent.mkdir(parents=True, exist_ok=True)
        image.save(str(savepath))


def main():
    parser = argparse.ArgumentParser(description="Colour Adjuster Tool (CAT)")

    parser.add_argument("folder", help="Top level target folder containing all icons to be modified")
    parser.add_argument("colour", help="New icon colour, in hex")

    args = parser.parse_args()

    colour = [0, 0, 0]
    hexcol = args.colour
    if hexcol[0] == "#":
        hexcol = hexcol[1:]
    colour[0] = int(hexcol[0:2], 16)
    colour[1] = int(hexcol[2:4], 16)
    colour[2] = int(hexcol[4:6], 16)

    root = Path(args.folder)
    savedir = Path(str(root) + "_" + hexcol)
    
    images = findimgs(root)
    processall(images, colour, savedir)
    
if __name__ == "__main__":
    main()