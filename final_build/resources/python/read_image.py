import os
import cv2

from range_color import Range
from logger import Logger


class ReadImage():
    def __init__(self):
        self.__width = 0
        self.__height = 0
        self.__milBlueHair = 0
        self.__milPinkShirts = 0
        self.__milRedShorts = 0
        self.__apuColorBody = 0
        self.__apuColorPants = 0
        self.__apuColorShirt = 0
        self.__renderedImage = None
        self.__features = []
        self.__displayImage = False

    def read(self, img, displayImage=False):
        Logger.log(f'Image received {img}')
        image = cv2.imread(img)

        self.__displayImage = displayImage

        self.__height, self.__width, channels = image.shape

        if self.__displayImage == True:
            Logger.log('Cloned image')
            self.__renderedImage = image.copy()

        Logger.log('Handle width and height')
        for height in range(self.__height):
            for width in range(self.__width):
                pixel = image[height, width]
                self.handleRangeColors(pixel, width, height)

        if self.__displayImage == True:
            cv2.imshow('image', self.__renderedImage)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        return self.normalizeFeatures(img)

    """
      Receive a pixel (R, G, B) and call range_color.py
      https://stackoverflow.com/questions/28981417/how-do-i-access-the-pixels-of-an-image-using-opencv-python/50588950
    """

    def handleRangeColors(self, pixel, index_width, index_height):
        range = Range()
        b, g, r = pixel

# ---------- Analisa Milhouse ------------------------------------------------------------------------

        if range.isMilHair(r, g, b):
            self.__milBlueHair += 1

            if self.__displayImage == True:
                self.set_color(self.__milBlueHair,
                               index_width, index_height)

        if range.isMilShirt(r, g, b):
            self.__milPinkShirts += 1

            if self.__displayImage == True:
                self.set_color(self.__milPinkShirts,
                               index_width, index_height)

        if index_height > (self.__height / 2) and range.isMilShorts(r, g, b):
            self.__milRedShorts += 1

            if self.__displayImage == True:
                self.set_color(self.__milRedShorts, index_width, index_height)

# ---------- Analisa Apu ----------------------------------------------------------------------------

        if range.isApuBody(r, g, b):
            self.__apuColorBody += 1
            if self.__displayImage == True:
                self.set_color(self.__apuColorBody, index_width, index_height)

        if index_height > (self.__height / 2) and range.isApuShirt(r, g, b):
            self.__apuColorShirt += 1
            if self.__displayImage == True:
                self.set_color(self.__apuColorShirt, index_width, index_height)

        if range.isApuPants(r, g, b):
            self.__apuColorPants += 1
            if self.__displayImage == True:
                self.set_color(self.__apuColorPants, index_width, index_height)

    def set_color(self, variable, index_width, index_height):
        self.__renderedImage[index_height][index_width] = [0, 255, 128]

    def calcNormalize(self, value):
        if (value != 0.0):
            return (value / (self.__width * self.__height)) * 100

        return 0.0

    """
      Normalizes the features by the number of total pixels of the image to % 
    """

    def normalizeFeatures(self, img):
        Logger.log('Normalize Features')

        self.__milBlueHair = self.calcNormalize(self.__milBlueHair)
        self.__milPinkShirts = self.calcNormalize(self.__milPinkShirts)
        self.__milRedShorts = self.calcNormalize(self.__milRedShorts)
        self.__apuColorBody = self.calcNormalize(self.__apuColorBody)
        self.__apuColorPants = self.calcNormalize(self.__apuColorPants)
        self.__apuColorShirt = self.calcNormalize(self.__apuColorShirt)

        milhouseOrApu = 0.0  # Bart
        filename = os.path.basename(img)[0]

        if filename == 'm':
            milhouseOrApu = 1.0  # Milhouse

        features = [
            self.__milBlueHair,
            self.__milPinkShirts,
            self.__milRedShorts,
            self.__apuColorBody,
            self.__apuColorPants,
            self.__apuColorShirt,
            milhouseOrApu
        ]

        Logger.log(features)
        return features
