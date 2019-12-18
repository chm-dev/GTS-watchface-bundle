import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement

class SymbolsElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._unknown0800 = None
        self._minusImageIndex = None
        self._degreesImageIndex = None
        self._noDataImageIndex = None
        super(SymbolsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getUnknown0800(self):
        return self._unknown0800


    def getMinusImageIndex(self):
        return self._minusImageIndex

    def getDegreesImageIndex(self):
        return self._degreesImageIndex

    def getNoDataImageIndex(self):
        return self._noDataImageIndex

    #def draw3(self, drawer, resources, state):
    #    assert(type(resources) == list)
    #    imageIndex = self.getImageIndexAmCn() if state.getTime().hour < 12 else self.getImageIndexPmCn()
    #    temp = resources[imageIndex].getBitmap()
    #    drawer.paste(temp, (self._x, self._y), temp)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        from watchFaceParser.models.elements.basic.valueElement import ValueElement
        if parameterId == 1:
            self._unknown0800 = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'Unknown0800')
        elif parameterId == 2:
            self._minusImageIndex = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'MinusImageIndex')
        elif parameterId == 3:
            self._degreesImageIndex = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'DegreesImageIndex')
        elif parameterId == 4:
            self._noDataImageIndex = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'NoDataImageIndex')
        else:
            print ("SymbolsElement",parameterId)
            return super(SymbolsElement, self).createChildForParameter(parameter)

