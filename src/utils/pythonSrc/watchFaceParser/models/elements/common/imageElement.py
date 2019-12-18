import logging

from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
from watchFaceParser.config import Config


class ImageElement(CoordinatesElement):
    def __init__(self, parameter, parent, name = None):
        self._imageIndex = None
        super(ImageElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def getImageIndex(self):
        return self._imageIndex


    def setImageIndex(self, imageIndex):
        self._imageIndex = imageIndex


    def draw3(self, drawer, resources, state):
        self.draw2(drawer, resources, None)


    def draw2(self, drawer, images, angle, center = None):
        x = self._x
        y = self._y
        if angle is None:
            temp = images[self._imageIndex].getBitmap()
            drawer.paste(temp, (x,y), temp)
        else:
            bitmap = images[self._imageIndex].getBitmap()
            from PIL import Image

            temp = Image.new('RGBA', Config.getImageSize())
            temp.paste(bitmap, (Config.getImageSizeHalf()[0] - x, Config.getImageSizeHalf()[1] - y), bitmap)
            temp = temp.rotate(angle)

            if center is None:
                drawer.paste(temp, (0,0), temp)
            else:
                drawer.paste(temp, (center.getX(),center.getY()), temp)			


    def createChildForParameter(self, parameter):
        if parameter.getId() == 3:
            self._imageIndex = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, '?ImageIndex?')
        else:
            super(ImageElement, self).createChildForParameter(parameter)
