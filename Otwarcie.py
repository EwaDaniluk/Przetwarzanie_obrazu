import cv2
import numpy as np
from Erozja import rgb_to_gray, erozja
from Dylatacja import dylatacja


def otwarcie(image, kernel):
    eroded = erozja(image, kernel)
    opened = dylatacja(eroded, kernel)
    return opened


def main():
    # Wczytanie obrazu
    im = cv2.imread("obrazek360x360.jpg")

    # Konwersja obrazu do skali szarości
    gray = rgb_to_gray(im)

    # Definicja jądra erozji/dylatacji (3x3)
    kernel = np.ones((3, 3), dtype=np.uint8)

    # Otwarcie obrazu
    opened = otwarcie(gray, kernel)

    # Zapisanie wynikowego obrazu
    cv2.imwrite("otwarcie.jpg", opened)


if __name__ == '__main__':
    main()
