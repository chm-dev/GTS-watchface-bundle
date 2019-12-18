from watchFaceParser.elements.basicElements.coordinates import Coordinates
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.basicElements.sector import Sector
from watchFaceParser.models.color import Color

class ClockHand:
    definitions = {
        1: { 'Name': 'OnlyBorder', 'Type': 'bool'},
        2: { 'Name': 'Color', 'Type': Color},
        3: { 'Name': 'CenterOffset', 'Type': Coordinates},
        4: { 'Name': 'Shape', 'Type': Coordinates}, #must be array [] fix it!
        5: { 'Name': 'Image', 'Type': Image},
        6: { 'Name': 'Sector', 'Type': Sector},
    }

