from enum import Enum, auto

class WidgetName(Enum):
    BUTTON = auto()
    CHECKBOX_INPUT = auto()
    COLOR_INPUT = auto()
    DIV = auto()
    HEADING_1 = auto()
    HEADING_2 = auto()
    INPUT = auto()
    PARAGRAPH = auto()
    LINE_BREAK = PARAGRAPH
    RANGE_INPUT = auto()
    SELECT = auto()