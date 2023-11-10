import logging
import csv

class GetName:
    def __init__(self):
        self.logger = logging

    def get_first_name(self, name):
        self.logger.debug("error occurs")
        self.logger.critical("nice")
        self.logger.info(f"name is {name}")
        first_name = str(name).split(" ")[1]
        self.logger.info(f"name is {first_name}")
        return first_name

    @staticmethod
    def add_info_to_txt(order_time, order_id, order_name, order_status, order_phone, start_time, end_time):
        with open(f'C:\\core_team\\test\\order_info_{start_time}_{end_time}.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([order_time, order_id, order_name, order_status, order_phone])

    @staticmethod
    def get_order_status(order_status):
        order_status = str(order_status).split("\n")[1]
        return order_status

    @staticmethod
    def get_order_name(order_name):
        order_name = str(order_name).split("\n")[1]
        return order_name

    @staticmethod
    def get_order_time(order_time):
        order_time = str(order_time).split("\n")[1]
        return order_time
