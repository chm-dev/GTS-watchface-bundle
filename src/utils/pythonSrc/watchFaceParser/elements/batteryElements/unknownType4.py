from watchFaceParser.models.textAlignment import TextAlignment
from watchFaceParser.elements.basicElements.coordinates import Coordinates
from watchFaceParser.models.color import Color

class UnknownType4:
    definitions = {
#        1: { 'Name': 'boCenterOffset', 'Type': 'long'},
#        2: { 'Name': 'boShape', 'Type': 'long'},
        1: { 'Name': 'OnlyBorder', 'Type': 'bool'},
        2: { 'Name': 'Color', 'Type': Color},
        3: { 'Name': 'CenterOffset', 'Type': Coordinates},
        4: { 'Name': 'Shape', 'Type': Coordinates},
    }
