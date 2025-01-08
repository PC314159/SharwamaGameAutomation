import cv2 as cv
import numpy as np
import datetime


def template_matching(inputpath, temppath, outputpath, color=(0, 0, 255)):
    inputimg = cv.imread(inputpath, cv.IMREAD_COLOR)
    temp = cv.imread(temppath, cv.IMREAD_COLOR)
    outputimg = cv.imread(inputpath, cv.IMREAD_COLOR)

    res = cv.matchTemplate(inputimg, temp, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    # print(loc)
    for pt in zip(*loc[::-1]):
        cv.rectangle(outputimg, pt, (pt[0] + temp.shape[1], pt[1] + temp.shape[0]), color, 1)
    cv.imwrite(outputpath, outputimg)


def order_matching(inputpath, temppath):
    inputimg = cv.imread(inputpath, cv.IMREAD_COLOR)
    temp = cv.imread(temppath, cv.IMREAD_COLOR)
    res = cv.matchTemplate(inputimg, temp, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    pts = list(zip(*loc[::-1]))
    # print(pts,1)
    pts = combine_nearby_points(pts, 10)
    # print(pts,2)
    return pts


def combine_nearby_points(points: list, tolerance=10) -> list:
    res = []
    for x, y in points:
        is_new = True
        for rx, ry in res:
            if abs(x - rx) <= 10 and abs(y - ry) <= 10:
                is_new = False
                break
        if is_new:
            res.append((x, y))
    return res


if __name__ == '__main__':
    template_matching("Data/fullscreen3.png", "Data/pickles.png", "Data/output.png", (0, 0, 255))
    template_matching("Data/output.png", "Data/sourcream.png", "Data/output.png", (0, 255, 0))
    template_matching("Data/output.png", "Data/friestray.png", "Data/output.png", (255, 0, 0))
    order_matching("Data/output.png", "Data/silvercoin.png")
    template_matching("Data/output.png", "Data/silvercoin.png", "Data/output.png", (255, 255, 0))

