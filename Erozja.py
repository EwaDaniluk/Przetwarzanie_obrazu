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

# Funkcja erozji
def erozja(image, kernel):
    w = image.shape[1]
    h = image.shape[0]
    eroded = np.zeros((h, w), dtype=np.uint8)
    eroded = eroded.astype(np.int16)  # Konwersja na typ np.int16
    k_h, k_w = kernel.shape

    for i in range(k_h // 2, h - k_h // 2):
        for j in range(k_w // 2, w - k_w // 2):
            min_val = 255
            for m in range(-k_h // 2, k_h // 2 + 1):
                for n in range(-k_w // 2, k_w // 2 + 1):
                    val = image[i + m, j + n] - kernel[m + k_h // 2, n + k_w // 2]
                    if val < min_val:
                        min_val = val
            eroded[i, j] = min_val

    return eroded

def main():
    # Wczytanie obrazu
    im = cv2.imread("obrazek360x360.jpg")

    # Konwersja obrazu do skali szarości
    gray = rgb_to_gray(im)

    # Definicja jądra erozji (3x3)
    kernel = np.ones((3, 3), dtype=np.uint8)

    # Erozja obrazu
    eroded = erozja(gray, kernel)

    # Zapisanie wynikowego obrazu
    cv2.imwrite("erozja.jpg", eroded)


if __name__ == '__main__':
    main()
