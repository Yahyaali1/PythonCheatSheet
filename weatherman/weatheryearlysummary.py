"""
Weather object for keeping relevant details
"""


class WeatherYearlySummary:
    def __init__(self, max_temp, min_temp, max_humidity, min_humidity, date):
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.max_humidity = max_humidity
        self.min_humidity = min_humidity
        self.date = date

    def year_summary(self):
        return f'{self.date.year:<10}{self.print_attrib(self.max_temp):<10}{self.print_attrib(self.min_temp):<10}' \
               f'{self.print_attrib(self.max_humidity):<10}{self.print_attrib(self.min_temp):<10}'

    def print_attrib(self, value):
        return str(None) if value is None else value

    def hot_day_summary(self):
        """
        Formatted string for temperature
        """
        return f'{self.date.year:<10}{self.date.strftime("%d/%m/%Y")}{"":<10}{self.print_attrib(self.max_temp):<10}'

    def __get_updated_attribute(self, old_attribute, new_attribute):
        return new_attribute if self.__should_update_attribute(old_attribute, new_attribute) else old_attribute

    def __should_update_attribute(self, old_attribute, new_attribute):
        if old_attribute is None:
            return True
        elif new_attribute is None:
            return False
        return old_attribute < new_attribute

    def update_attributes_summary(self, max_temp, min_temp, max_humidity, min_humidity, date):
        """
        Update the date for hottest day
        Updates min max temp & humidity
        """
        if self.__should_update_attribute(self.max_temp, max_temp):
            self.date = date
            self.max_temp = max_temp

        self.min_temp = self.__get_updated_attribute(self.min_temp, min_temp)
        self.max_humidity = self.__get_updated_attribute(self.max_humidity, max_humidity)
        self.min_humidity = self.__get_updated_attribute(self.min_humidity, min_humidity)
