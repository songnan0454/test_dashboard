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

    @keyword("Add Info To Txt")
    def add_info_to_txt(self, order_time, order_id, order_name, order_status, order_phone, start_time, end_time):
        """
        Keyword retrieve order list
        """
        return self.get_name.add_info_to_txt(order_time, order_id, order_name, order_status, order_phone, start_time, end_time)

    @keyword("Get Order Status")
    def check_order_status(self, order_status):
        """
        Keyword retrieve order list
        """
        return self.get_name.get_order_status(order_status)

    @keyword("Get Order Name")
    def get_order_name(self, order_status):
        """
        Keyword retrieve order list
        """
        return self.get_name.get_order_name(order_status)

    @keyword("Get Order Time")
    def get_order_time(self, order_time):
        """
        Keyword retrieve order list
        """
        return self.get_name.get_order_time(order_time)