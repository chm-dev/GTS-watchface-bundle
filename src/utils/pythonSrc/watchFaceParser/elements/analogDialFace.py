from watchFaceParser.elements.analogDialFaceElements.clockHand import ClockHand
from watchFaceParser.elements.basicElements.image import Image

class AnalogDialFace:
    definitions = {
        1: { 'Name': 'Hours', 'Type': ClockHand},
        5: { 'Name': 'HourCenterImage', 'Type': Image}, # testit!
        2: { 'Name': 'Minutes', 'Type': ClockHand},
		6: { 'Name': 'MinCenterImage', 'Type': Image}, # testit!
        3: { 'Name': 'Seconds', 'Type': ClockHand},
        4: { 'Name': 'SecCenterImage', 'Type': Image}, # verge
    }

