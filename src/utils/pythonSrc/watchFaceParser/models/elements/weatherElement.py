import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class WeatherElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._images = None
        self._icon = None
        self._temperature = None
        super(WeatherElement,self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        assert(type(images) == list)
#        if self.getImages():
#            self.getImages().draw3(drawer, images, 1)
#
        if self.getIcon():
		    #render weather icon
            self.getIcon().getImages().draw3(drawer, images, state.getWeather())

        if self.getTemperature():
            self.getTemperature().draw3(drawer, images, 1)


    def getImages(self):
        return self._images

    def getIcon(self):
        return self._icon

    def getTemperature(self):
        return self._temperature

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1: #icon
            from watchFaceParser.models.elements.weather.extendedWeatherElement import ExtendedWeatherElement
            self._icon = ExtendedWeatherElement(parameter = parameter, parent = self, name = 'Icon')
            return self._icon
        elif parameterId == 2: #temperature(text)
            print ("WeatherElement: temperature(text) writing supported")
            from watchFaceParser.models.elements.weather.temperatureElement import TemperatureElement
            self._temperature = TemperatureElement(parameter = parameter, parent = self, name = 'Temperature')
            return self._temperature
#        elif parameterId == 3:
#            from watchFaceParser.models.elements.common.twoDigitsElement import TwoDigitsElement
#            self._seconds = TwoDigitsElement(parameter = parameter, parent = self, name = 'Seconds')
#            return self._seconds
#        elif parameterId == 4:
#            from watchFaceParser.models.elements.time.amPmElement import AmPmElement
#            self._amPm = AmPmElement(parameter = parameter, parent = self, name = 'AmPm')
#            return self._amPm
#        elif parameterId == 5:
#            pass
#        elif parameterId == 10:
#            from watchFaceParser.models.elements.common.imageElement import ImageElement
#            self._delimiter = ImageElement(parameter = parameter, parent = self, name = 'Delimiter')
#            return self._delimiter
#        elif parameterId == 12:
#            from watchFaceParser.models.elements.time.pmElement import PmElement
#            self._pm = PmElement(parameter = parameter, parent = self, name = 'Pm')
#            return self._pm
        else:
            print ("WeatherElement: unsupported", parameterId)
            return super(WeatherElement, self).createChildForParameter(parameter)

