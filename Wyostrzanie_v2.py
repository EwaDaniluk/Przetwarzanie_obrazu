# Maskowanie nieostrości

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

# Funkcja przeprowadza filtracje dolnoprzepustową (wygładzania) na obrazie oryginalnym.
# Następnie odejmujemy obraz wygładzony od obrazu oryginalnego, aby otrzymać maskę.
# W końcu dodaje tę maskę do obrazu oryginalnego, aby otrzymać wyostrzony obraz.
def sharpen_image(image, kernel_size, sigma):
    # Konwersja obrazu do skali szarości
    gray = rgb_to_gray(image)

    # Wygładzanie obrazu
    blurred = np.zeros_like(gray, dtype=np.float32)

    # Rozmiar maski
    mask_size = kernel_size * kernel_size

    # Obliczanie wygładzenia dla każdego piksela
    for i in range(1, gray.shape[0] - 1):
        for j in range(1, gray.shape[1] - 1):
            sum = 0
            for m in range(-1, 2):
                for n in range(-1, 2):
                    sum += gray[i + m, j + n]
            blurred[i, j] = sum / mask_size

    # Obliczanie maski
    mask = gray - blurred

    # Dodawanie maski do obrazu oryginalnego
    sharpened = gray + mask

    return sharpened


def main():
    # Wczytanie obrazu
    image = cv2.imread("obrazek360x360.jpg")

    # Wyostrzanie obrazu
    sharpened = sharpen_image(image, kernel_size=3, sigma=1.0)
    # Większy 'karnel_size' oznacza większy rozmiar maski, a większe 'sigma' powoduje większe rozmycie

    # Zapisanie wynikowego obrazu
    cv2.imwrite("wyostrzony_v2.jpg", sharpened)


if __name__ == '__main__':
    main()
