from robot.api.deco import keyword
from core.GetName import GetName
from core.tools.ClassInitializer import ClassInitializer


class GetNameLibrary:
    def __init__(self):
        self.get_name = ClassInitializer.create_object(GetName)

    @keyword("Get The First Name")
    def get_the_first_name(self, name):
        """
        Keyword get detail name
        """
        return self.get_name.get_first_name(name)