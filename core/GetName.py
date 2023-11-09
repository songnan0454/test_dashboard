import logging

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
