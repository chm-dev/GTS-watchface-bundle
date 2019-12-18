from watchFaceParser.models.elements.common.numberElement import NumberElement
from watchFaceParser.utils.parametersConverter import uint2int

class BatteryNumberElement(NumberElement):
    def __init__(self, parameter, parent, name = 'None'):
        super(BatteryNumberElement, self).__init__(parameter, parent, name)

    #def draw3(self, drawer, resources, state):
    #    self.draw4(drawer, resources, state.getBatteryLevel())

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        temperature = self._parent
		
        images = self._parent.getText().getImagesForNumber(resources, state.getBatteryLevel())
		
        print ("DEBUGGGG-",images)
        if self._parent.getPercent():
            images.append(resources[self._parent.getPercent().getImageIndex()])

        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        DrawerHelper.drawImages(drawer, images, uint2int(self._parent.getText().getSpacing()), self._parent.getText().getAlignment(), self._parent.getText().getBox())
