"""
Weather object for keeping relevant details
"""


class WeatherYearlySummary:
    KEY_DATE = "PKT"
    KEY_DATE_ALTER = "PKST"
    KEYS_WEATHER_ATTRIB = ["Max TemperatureC", "Min TemperatureC", "Max Humidity", "Min Humidity", KEY_DATE]

    def __init__(self, data, date):
        self.attributes = data
        self.date = date

    def year_summary(self):
        string = f'{self.date.year:<10}'
        for attribute in self.attributes:
            string += f'{attribute:<10}'
        return string

    def hot_day_summary(self):
        """
        Formatted string for temperature
        """
        return f'{self.date.year:<10}{self.date.strftime("%d/%m/%Y")}{"":<10}{self.attributes[0]:<10}'

    def __should_update_attribute(self, old_attribute, new_attribute):
        if old_attribute is None:
            return True
        elif new_attribute is None:
            return False
        return old_attribute < new_attribute

    def update_attributes_summary(self, new_attributes, date):
        """
        Update the date for hottest day
        Updates min max temp & humidity
        """
        if self.__should_update_attribute(self.attributes[0], new_attributes[0]):
            self.date = date
        for index in range(len(self.attributes)):
            if self.__should_update_attribute(self.attributes[index], new_attributes[index]):
                self.attributes[index] = new_attributes[index]
