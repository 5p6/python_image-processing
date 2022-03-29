import matplotlib.pyplot as plt
import matplotlib.image as mat
import torch
import cv2 as cv
import pandas
import numpy as np
picure=cv.imread('D:/MATLAB/matlab/moon.tif');
c=picure[:,:,0];
def lace(c):
    x, y = c.shape;
    g = np.zeros((x + 2, y + 2), float);
    g[1:x + 1, 1:y + 1] = c;
    f = np.zeros((x, y));
    lace = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]);
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            f[i - 1, j - 1] = np.sum(g[i - 1:i + 2, j - 1:j + 2] * lace);
    return f;
f=lace(c);
cv.imshow('image',f)
cv.waitKey(0)