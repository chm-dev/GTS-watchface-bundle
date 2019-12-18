import logging

from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement

class ExtendedWeatherElement(ImageSetElement):
    def __init__(self, parameter, parent, name = None):
        print("init weather")
        self._images = None
        super(ExtendedWeatherElement, self).__init__(parameter = parameter, parent = parent, name = name)

#    def draw3(self, drawer, resources, state):
#        assert(type(resources) == list)
#        print("draw3 weather")
#        print ("ERATHER",state.getWeather())
#        super(ExtendedWeatherElement, self).draw3(drawer, resources, state.getWeather()) #int(state.getBatteryLevel() * self.getImagesCount() / 100))

    def getImages(self):
        return self._images

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        print ("ExtendedWeatherElement:",parameterId)
        if parameterId == 1:
            print ("ExtendedWeatherElement(1=images?!)",parameterId) # images!?!?
            from watchFaceParser.models.elements.weather.imagesElement import ImagesElement
            self._images = ImagesElement(parameter = parameter, parent = self, name = 'Images')
            return self._images	
        elif parameterId == 2:
            print ("ExtendedWeatherElement(2=NoWeatherImageIndex?!)",parameterId) # NoWeatherImageIndex!?!?
            pass
#            from watchFaceParser.models.elements.basic.valueElement import ValueElement
#            self._suffixImageIndex = parameter.getValue()
#            return ValueElement(parameter, self, 'SuffixImageIndex')
#        elif parameterId == 3:
#            from watchFaceParser.models.elements.basic.valueElement import ValueElement
#            self._decimalPointImageIndex = parameter.getValue()
#            return ValueElement(parameter, self, 'DecimalPointImageIndex')
        else:
            super(ExtendedWeatherElement, self).createChildForParameter(parameter)