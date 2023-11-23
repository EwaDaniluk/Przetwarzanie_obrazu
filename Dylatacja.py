import cv2
import numpy as np

# Funkcja konwertuje obraz kolorowy na skalę szarości,
# obliczając średnią wartość składowych RGB dla każdego piksela.
def rgb_to_gray(image):
    w = image.shape[1]
    h = image.shape[0]
    gray = np.zeros((h, w), dtype=np.uint8)
    gray = gray.astype(np.int16)  # Konwersja na typ np.int16
    for i in range(h):
        for j in range(w):
            b, g, r = image[i, j]
            gray[i, j] = int(0.299 * r + 0.587 * g + 0.114 * b)
            # zastosowano wartości wag dla składowych RGB, które są zalecane dla przekształcenia na skalę szarości

    return gray

# Funkcja dylatacji
def dylatacja(image, kernel):
    w = image.shape[1]
    h = image.shape[0]
    dilated = np.zeros((h, w), dtype=np.uint8)
    dilated = dilated.astype(np.int16)  # Konwersja na typ np.int16
    k_h, k_w = kernel.shape

    for i in range(k_h // 2, h - k_h // 2):
        for j in range(k_w // 2, w - k_w // 2):
            max_val = 0
            for m in range(-k_h // 2, k_h // 2 + 1):
                for n in range(-k_w // 2, k_w // 2 + 1):
                    val = image[i + m, j + n] + kernel[m + k_h // 2, n + k_w // 2]
                    if val > max_val:
                        max_val = val
            dilated[i, j] = max_val

    return dilated

def main():
    # Wczytanie obrazu
    im = cv2.imread("obrazek360x360.jpg")

    # Konwersja obrazu do skali szarości
    gray = rgb_to_gray(im)

    # Definicja jądra erozji (3x3)
    kernel = np.ones((3, 3), dtype=np.uint8)

    # Dylatacja obrazu
    dilated = dylatacja(gray, kernel)

    # Zapisanie wynikowego obrazu
    cv2.imwrite("dylatacja.jpg", dilated)


if __name__ == '__main__':
    main()
