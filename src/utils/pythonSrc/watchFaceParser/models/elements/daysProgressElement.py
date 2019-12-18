import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class DaysProgressElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        super(DaysProgressElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.analogDial.secondsClockHandElement import SecondsClockHandElement # must must be own. fix it!!
            self._clockHand = SecondsClockHandElement(parameter = parameter, parent = self, name = 'AnalogMonth')
            return self._clockHand
        elif parameterId == 3:
            from watchFaceParser.models.elements.analogDial.secondsClockHandElement import SecondsClockHandElement # must must be own. fix it!!
            self._clockHand = SecondsClockHandElement(parameter = parameter, parent = self, name = 'AnalogDOW')
            return self._clockHand
        else:
            return super(DaysProgressElement, self).createChildForParameter(parameter)
