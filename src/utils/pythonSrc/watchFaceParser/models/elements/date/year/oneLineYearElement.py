﻿import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
from watchFaceParser.utils.parametersConverter import uint2int


class OneLineYearElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._number = None
        self._delimiterImageIndex = None
        super(OneLineYearElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getNumber(self):
        return self._number

    def getDelimiterImageIndex(self):
        return self._delimiterImageIndex.getValue()


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        year = self._parent

        #print ("draw3",state.getTime().year)
        images = self.getNumber().getImagesForNumber(resources, state.getTime().year, 4)
        #print ("draw3",images)
		
        images.append(resources[self.getDelimiterImageIndex()])
        #for image in self.getNumber().getImagesForNumber(resources, state.getTime().day, 2 if monthAndDay.getTwoDigitsDay() else 1):
        #    images.append(image)

        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        DrawerHelper.drawImages(drawer, images, uint2int(self.getNumber().getSpacing()), self.getNumber().getAlignment(), self.getNumber().getBox())


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            print ("OneLineYearElement",parameterId)
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._number = NumberElement(parameter = parameter, parent = self, name = 'Number')
            return self._number
        elif parameterId == 2:
            print ("OneLineYearElement",parameterId)	
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._delimiterImageIndex = ValueElement(parameter = parameter, parent = self, name = 'DelimiterImageIndex')
            #print ("_delimiterImageIndex",self._delimiterImageIndex)
            return self._delimiterImageIndex
        else:
            return super(OneLineYearElement, self).createChildForParameter(parameter)
