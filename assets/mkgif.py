from PIL import Image, ImageDraw

W, H, S = 24, 32, 4
HAIR = (245, 168, 205)
HAIR_D = (228, 128, 176)
SKIN = (255, 216, 190)
BLUSH = (255, 150, 170)
DRESS = (55, 65, 115)
WHITE = (248, 248, 248)
EYE = (45, 38, 55)
SHOE = (60, 48, 70)


def frame(f):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    lean = (-1 if f == 0 else 1 if f == 2 else 0)
    bob = (1 if f in (1, 3) else 0)

    # twin tails sway with the lean
    d.rectangle([2 + lean, 8 + bob, 5 + lean, 20 + bob], fill=HAIR_D)
    d.rectangle([19 + lean, 8 + bob, 22 + lean, 20 + bob], fill=HAIR_D)
    d.rectangle([2 + lean, 18 + bob, 5 + lean, 22 + bob], fill=HAIR)
    d.rectangle([19 + lean, 18 + bob, 22 + lean, 22 + bob], fill=HAIR)
    # hair back + top
    d.rectangle([5 + lean, 2 + bob, 18 + lean, 12 + bob], fill=HAIR)
    d.rectangle([4 + lean, 4 + bob, 19 + lean, 9 + bob], fill=HAIR)
    # face
    d.rectangle([7 + lean, 6 + bob, 16 + lean, 13 + bob], fill=SKIN)
    # bangs
    d.rectangle([7 + lean, 6 + bob, 16 + lean, 7 + bob], fill=HAIR)
    d.point((8 + lean, 8 + bob), HAIR)
    d.point((15 + lean, 8 + bob), HAIR)
    # happy closed eyes
    d.point((9 + lean, 10 + bob), EYE)
    d.point((10 + lean, 10 + bob), EYE)
    d.point((14 + lean, 10 + bob), EYE)
    d.point((15 + lean, 10 + bob), EYE)
    # smile + blush
    d.point((11 + lean, 13 + bob), EYE)
    d.point((12 + lean, 13 + bob), EYE)
    d.rectangle([8 + lean, 11 + bob, 9 + lean, 11 + bob], fill=BLUSH)
    d.rectangle([15 + lean, 11 + bob, 16 + lean, 11 + bob], fill=BLUSH)

    # dress + collar
    d.rectangle([8 + lean, 14 + bob, 15 + lean, 22 + bob], fill=DRESS)
    d.rectangle([6 + lean, 20 + bob, 17 + lean, 22 + bob], fill=DRESS)
    d.point((10 + lean, 14 + bob), WHITE)
    d.point((13 + lean, 14 + bob), WHITE)
    d.point((11 + lean, 15 + bob), WHITE)
    d.point((12 + lean, 15 + bob), WHITE)
    # arms - up on bounce frames, down on the rest
    if f in (0, 2):
        d.rectangle([5 + lean, 12 + bob, 6 + lean, 15 + bob], fill=SKIN)
        d.rectangle([17 + lean, 12 + bob, 18 + lean, 15 + bob], fill=SKIN)
    else:
        d.rectangle([5 + lean, 15 + bob, 6 + lean, 18 + bob], fill=SKIN)
        d.rectangle([17 + lean, 15 + bob, 18 + lean, 18 + bob], fill=SKIN)
    # legs - one kicks out on the lean frames
    if f == 0:
        d.rectangle([9 + lean, 23 + bob, 10 + lean, 26 + bob], fill=SKIN)
        d.rectangle([9 + lean, 27 + bob, 10 + lean, 29 + bob], fill=SHOE)
        d.rectangle([16 + lean, 23 + bob, 18 + lean, 25 + bob], fill=SKIN)
        d.rectangle([18 + lean, 25 + bob, 20 + lean, 27 + bob], fill=SHOE)
    elif f == 2:
        d.rectangle([14 + lean, 23 + bob, 15 + lean, 26 + bob], fill=SKIN)
        d.rectangle([14 + lean, 27 + bob, 15 + lean, 29 + bob], fill=SHOE)
        d.rectangle([5 + lean, 23 + bob, 7 + lean, 25 + bob], fill=SKIN)
        d.rectangle([3 + lean, 25 + bob, 5 + lean, 27 + bob], fill=SHOE)
    else:
        d.rectangle([9 + lean, 23 + bob, 10 + lean, 27 + bob], fill=SKIN)
        d.rectangle([14 + lean, 23 + bob, 15 + lean, 27 + bob], fill=SKIN)
        d.rectangle([9 + lean, 28 + bob, 10 + lean, 30 + bob], fill=SHOE)
        d.rectangle([14 + lean, 28 + bob, 15 + lean, 30 + bob], fill=SHOE)
    return img.resize((W * S, H * S), Image.NEAREST)


frames = [frame(i) for i in range(4)]
frames[0].save("assets/dance.gif", save_all=True, append_images=frames[1:],
               duration=140, loop=0, transparency=0, disposal=2)
print("saved assets/dance.gif")
