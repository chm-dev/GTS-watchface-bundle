from watchFaceParser.models.elements.common.numberElement import NumberElement
from watchFaceParser.utils.parametersConverter import uint2int


class TemperatureElement(NumberElement):
    def __init__(self, parameter, parent, name = 'None'):
        self._temperature = None
        self._symbols = None
        super(TemperatureElement, self).__init__(parameter, parent, name)

    def getTemperature(self):
        return self._temperature

    def getSymbols(self):
        return self._symbols
		
    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        temperature = self._parent
		
        images = self.getTemperature().getImagesForNumber(resources, 27, 2) #fixed temperature for now....
		
        #print ("DEBUGGGG",self.getSymbols().getDegreesImageIndex())
        images.append(resources[self.getSymbols().getDegreesImageIndex()])

        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        DrawerHelper.drawImages(drawer, images, uint2int(self.getTemperature().getSpacing()), self.getTemperature().getAlignment(), self.getTemperature().getBox())

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            print ("TemperatureElement: (Temperature->Current)", parameterId)
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._temperature = NumberElement(parameter = parameter, parent = self, name = 'Temperature')
            print ("DEBUG",self._temperature)
            return self._temperature
        elif parameterId == 2:
            print ("TemperatureElement: (Temperature->Today)", parameterId)
            pass
        elif parameterId == 3:
            print ("TemperatureElement: (Temperature->Symbols)", parameterId)
            from watchFaceParser.models.elements.weather.symbolsElement import SymbolsElement
            self._symbols = SymbolsElement(parameter = parameter, parent = self, name = 'Symbols')
            print ("DEBUG",self._symbols)
            return self._symbols
        else:
            return super(TemperatureElement, self).createChildForParameter(parameter)
