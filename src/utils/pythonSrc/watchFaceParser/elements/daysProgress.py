from watchFaceParser.elements.analogDialFaceElements.clockHand import ClockHand

class DaysProgress:
    definitions = {
		1: { 'Name': 'AnalogMonth', 'Type': ClockHand},
		2: { 'Name': 'UnknownField2', 'Type': 'long?'},
		3: { 'Name': 'AnalogDOW', 'Type': ClockHand},
    }

