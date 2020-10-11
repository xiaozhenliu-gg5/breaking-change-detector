import enum 

class FindingCategory(enum.Enum): 
    ENUM_VALUE_ADDITION = 1
    ENUM_VALUE_REMOVAL = 2
    ENUM_VALUE_NAME_CHANGE = 3
    ENUM_ADDITION = 4
    ENUM_REMOVAL = 5
    ENUM_NAME_CHANGE = 6
    FIELD_ADDITION = 7
    FIELD_REMOVAL = 8
    FIELD_NAME_CHANGE = 9
    FIELD_REPEATED_CHANGE = 10
    FIELD_TYPE_CHANGE = 11
    FIELD_ONEOF_REMOVAL = 12
    FIELD_ONEOF_ADDITION = 13
    MESSAGE_ADDITION = 14
    MESSAGE_REMOVAL = 15
    MESSAGE_NAME_CHANEG = 16

    

class Finding:
    category: FindingCategory
    location: str
    message: str
    actionable: bool
    extra_info: str = None
    _path: str

    class _Location:
        path: str
        def __init__(self, path):
            self.path = path

    def __init__(self, category, path, message, actionable, extra_info = None):
        self.category = category
        self.location = self._Location(path)
        self.message = message
        self.actionable = actionable
        self.extra_info = extra_info
        self._path = path

    def toDict(self):
        return {
            "category": self.category.value,
            "location": {
                "path": self._path,
            },
            "message": self.message,
            "actionable": self.actionable,
            "extra_info": self.extra_info,
        }

