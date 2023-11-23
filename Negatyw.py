import cv2

def main():
    im = cv2.imread("obrazek320x240.jpg")
    w = im.shape[1]
    h = im.shape[0]
    LUT = []

    for i in range(256):
        LUT.append(255-i)

    for i in range(h):
        for j in range(w):
            b, g, r = im[i, j]
            im[i, j] = LUT[b], LUT[g], LUT[r]

    cv2.imwrite("negatyw.jpg", im)


if __name__ == '__main__':
    main()
