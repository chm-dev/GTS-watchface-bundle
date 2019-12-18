from watchFaceParser.elements.activityElements.formattedNumber import FormattedNumber
from watchFaceParser.elements.activityElements.distance import Distance
from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.basicElements.circleScale import CircleScale
from watchFaceParser.elements.basicElements.unknownType import UnknownType

class Activity:
    definitions = {
        1: { 'Name': 'StepsGoal', 'Type': CircleScale}, # should be kcal on gts
        2: { 'Name': 'Calories', 'Type': Number},
        3: { 'Name': 'Pulse', 'Type': Number},
        4: { 'Name': 'Distance', 'Type': Distance},
        5: { 'Name': 'Steps', 'Type': FormattedNumber},
        7: { 'Name': 'StarImage', 'Type': Image}, #gtr
        9: { 'Name': 'CircleRange', 'Type': Image}, # verge
        11: { 'Name': 'Goal2', 'Type': CircleScale}, # gts circle.bin
        12: { 'Name': 'Unknown12', 'Type': 'long'}, # gts
		13: { 'Name': 'NoDataImageIndex', 'Type': 'long'}, # verge
        15: { 'Name': 'Unknown15', 'Type': 'long'}, # gts
        17: { 'Name': 'Unknown17', 'Type': UnknownType}, # gts circle.bin
    }

