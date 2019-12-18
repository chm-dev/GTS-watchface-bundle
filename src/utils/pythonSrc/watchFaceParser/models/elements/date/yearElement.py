import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class YearElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._oneLine = None	
        super(YearElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getOneLine(self):
        return self._oneLine

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        print ("YEARELEMENT:",parameterId)
        if parameterId == 1:
            from watchFaceParser.models.elements.date.year.oneLineYearElement import OneLineYearElement
            self._oneLine = OneLineYearElement(parameter = parameter, parent = self, name = 'OneLineYearElement')
            return self._oneLine
        else:
            return super(YearElement, self).createChildForParameter(parameter)

