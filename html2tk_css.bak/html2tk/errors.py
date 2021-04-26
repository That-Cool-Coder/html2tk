class NoHtmlProvided(BaseException):
    pass

class CssParseError(BaseException):
    def __init__(self, css_class_name):
        message = f'Error parsing CSS in class {css_class_name}'
        super().__init__(message)