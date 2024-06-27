# This is a sample Python script.
import cv2
import numpy as np

if __name__ == '__main__':
    mode = 0
    img = cv2.imread('img.png', cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = img.shape[:2]

    # canny Edge
    edge = cv2.Canny(gray, 185, 229)
    cv2.imshow("Canny", edge)

    #roi
    mask = np.zeros_like(edge)
    vertices = np.array(
        [[(0, h-50), (w / 2 - 45, h / 2), (w/2 + 45, h / 2), (w - 50, h-50)]],
        dtype=np.int32)
    cv2.fillPoly(mask, vertices, (255, 255, 255))
    roi = cv2.bitwise_and(edge, mask)
    cv2.imshow("roi", roi)

    # hough
    lines = cv2.HoughLinesP(roi, 1, 1 * np.pi/180, 0, 20, 0)
    print(lines)
    hough = img.copy()
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(hough, (x1, y1), (x2, y2), (0, 0, 255), 2)




    cv2.imshow("Hough", hough)


    cv2.waitKey(0)
    cv2.destroyAllWindows()