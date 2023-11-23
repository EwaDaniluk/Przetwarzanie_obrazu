# Operator Laplace'a

import cv2
import numpy as np

# Funkcja konwertuje obraz kolorowy na skalę szarości,
# obliczając średnią wartość składowych RGB dla każdego piksela.
def rgb_to_gray(image):
    w = image.shape[1]
    h = image.shape[0]
    gray = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            b, g, r = image[i, j]
            gray[i, j] = int(0.299 * r + 0.587 * g + 0.114 * b)
            # zastosowano wartości wag dla składowych RGB, które są zalecane dla przekształcenia na skalę szarości

    return gray

# Funkcja oblicza operator Laplace'a na obrazie szarości,
# korzystając z odpowiednich wzorów dla gradientu poziomego i pionowego.
# W tej implementacji rozmiar maski jest ustalony na 3x3.
def laplacian_operator(image):
    w = image.shape[1]
    h = image.shape[0]
    laplace = np.zeros((h, w), dtype=np.int16)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            gx = image[i, j - 1] - 2 * image[i, j] + image[i, j + 1]
            gy = image[i - 1, j] - 2 * image[i, j] + image[i + 1, j]
            laplace[i, j] = gx + gy

    return laplace

# Funkcja wykonuje skalowanie i absolutną wartość wyniku operacji Laplace'a.
def convert_scale_abs(image):
    w = image.shape[1]
    h = image.shape[0]
    sharpened = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            sharpened[i, j] = np.abs(image[i, j])

    return sharpened


def main():
    # Wczytanie obrazu
    im = cv2.imread("obrazek360x360.jpg")

    # Konwersja obrazu do skali szarości
    gray = rgb_to_gray(im)

    # Wyostrzenie obrazu przy użyciu operatora Laplace'a
    laplace = laplacian_operator(gray)
    sharpened = convert_scale_abs(gray - laplace)

    # Zapisanie wynikowego obrazu
    cv2.imwrite("wyostrzony_v1.jpg", sharpened)


if __name__ == '__main__':
    main()
