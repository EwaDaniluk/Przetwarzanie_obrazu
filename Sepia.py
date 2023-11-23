import cv2
import numpy as np

def main():
    im = cv2.imread("obrazek320x240.jpg")
    w = im.shape[1]
    h = im.shape[0]

    im = im.astype(np.uint16)

    for i in range(h):
        for j in range(w):
            b, g, r = im[i, j]
            newb = int((b + g + r) / 3)
            newg = int((b + g + r) / 3)
            newr = int((b + g + r) / 3)
            im[i, j] = (newb, newg, newr)

    while True:
        ws = int(input("Podaj współczynnik wypełnienia barwą (od 20 do 40): "))
        if ws < 20 or ws > 40:
            print("Podany współczynnik nie mieści się w przedziale.")
        else:
            break

    for i in range(h):
        for j in range(w):
            bs, gs, rs = im[i, j]
            newb = bs
            newg = int(gs + ws)
            newr = int(rs + 2*ws)
            im[i, j] = (newb, newg, newr)

    im = im.astype(np.uint8)

    cv2.imwrite("sepia.jpg", im)


if __name__ == '__main__':
    main()
