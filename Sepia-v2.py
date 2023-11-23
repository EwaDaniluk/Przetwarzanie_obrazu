import cv2
import numpy as np

def main():
    im = cv2.imread("obrazek320x240.jpg")
    w = im.shape[1]
    h = im.shape[0]

    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_gray = cv2.cvtColor(im_gray, cv2.COLOR_GRAY2RGB)

    while True:
        W = int(input("Podaj współczynnik wypełnienia barwą (od 20 do 40): "))
        if W < 20 or W > 40:
            print("Podany współczynnik nie mieści się w przedziale.")
        else:
            break

    for i in range(h):
        for j in range(w):
            b, g, r = im_gray[i, j]
            newg = int(g + W)
            newr = int(r + 2 * W)
            newg = np.clip(newg, 0, 255) # ograniczenie wartości do 0-255
            newr = np.clip(newr, 0, 255) # ograniczenie wartości do 0-255
            im_gray[i, j] = (b, newg, newr)

    cv2.imwrite("sepia-v2.jpg", im_gray)


if __name__ == '__main__':
    main()
