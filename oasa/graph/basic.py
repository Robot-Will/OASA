class attribute_flexible_class:
    """this class provides mechanism for addition and removing of attributes on fly"""

    def __init__(self):
        pass

    def add_attribute(self, name, value=None):
        if name not in self.__dict__:
            self.__dict__[name] = value
            return 1
        return 0

    def del_attribute(self, name):
        if name not in self.__dict__:
            del self.__dict__[name]
            return 1
        return 0
