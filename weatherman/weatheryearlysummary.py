"""
Weather object for keeping relevant details
"""


class WeatherYearlySummary:
    DATE_VALUE_ERROR = "Date value is None"

    def __init__(self):
        self.max_temp, self.min_temp, self.max_humidity, self.min_humidity, self.date = [None] * 5

    def year_summary(self):
        return self.DATE_VALUE_ERROR if self.date is None else f'{self.date.year:<10}{str(self.max_temp):<10}' \
                                                               f'{str(self.min_temp):<10}{str(self.max_humidity):<10}' \
                                                               f'{str(self.min_temp):<10}'

    def hot_day_summary(self):
        """
        Formatted string for temperature
        """
        return self.DATE_VALUE_ERROR if self.date is None else f'{self.date.year:<10}' \
                                                               f'{self.date.strftime("%d/%m/%Y"):<20}' \
                                                               f'{str(self.max_temp):<10}'

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
