from watchFaceParser.models.elements.common.numberElement import NumberElement

class Goal2Element(NumberElement):
    def __init__(self, parameter, parent, name = 'None'):
        super(Goal2Element, self).__init__(parameter, parent, name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        #if state.getGoal2():
        #    self.draw4(drawer, resources, state.getGoal2())
