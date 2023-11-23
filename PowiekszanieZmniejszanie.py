# import cv2
# import numpy as np
#
#
# def main():
#     im = cv2.imread("obrazek320x240.jpg")
#     x1 = im.shape[1]
#     while True:
#         x2 = int(input("Podaj szerokość obrazu wyjściowego: "))
#         if x2 < 0 :
#             print("Podana szerokość jest mniejsza od 0")
#         else:
#             break
#     y1 = im.shape[0]
#     while True:
#         y2 = int(input("Podaj wysokość obrazu wyjściowego"))
#         if y2 < 0 :
#             print("Podana wysokość jest mniejsza od 0")
#         else:
#             break
#     Rx = float(x1/x2)
#     Ry = float(y1/y2)
#     wymiar = (x2, y2)
#     if x1 > x2 or y1 > y2:            #zmniejszamy
#         zmniejszony = cv2.resize(im, wymiar, interpolation=cv2.INTER_AREA)
#         zmniejszony = np.zeros((y2, x2, 3), dtype=np.uint8)
#         for i in range(y2):
#             for j in range(x2):
#                 wx = int(j*Rx)
#                 wy = int(i*Ry)
#                 zmniejszony[i, j] = im[wy, wx]
#         cv2.imwrite("zmniejszony.jpg", zmniejszony)
#     else:                            #powiekszamy
#         powiekszony = cv2.resize(im, wymiar, interpolation=cv2.INTER_AREA)
#         powiekszony = np.zeros((y1, x1, 3), dtype=np.uint8)
#         for i in range(y1):
#             for j in range(x1):
#                 wx = int(j*Rx)
#                 wy = int(i*Ry)
#                 powiekszony[i, j] = im[wy, wx]
#         cv2.imwrite("powiekszony.jpg", powiekszony)
#
#
# if __name__ == '__main__':
#     main()


