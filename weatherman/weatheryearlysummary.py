"""
Weather object for keeping relevant details
Provides keys for  data in dictionary
"""
from datetime import datetime
from utils import is_hotter_day


class WeatherYearlySummary:
    KEY_DATE = "PKT"
    KEY_DATE_ALTER = "PKST"
    KEY_SUMMARY = "SUMMARY"
    KEYS_WEATHER_ATTRIB = ["Max TemperatureC", "Min TemperatureC", "Max Humidity", "Min Humidity", KEY_DATE]
    __DATE_FORMAT = '%Y-%m-%d'
    DATE_FORMAT_OUTPUT = '%d/%m/%Y'

    def __init__(self, weather_data):
        self.data = self.__form_summary_dict(weather_data)

    def __form_summary_dict(self, data_list):
        summary = {k: None for k in self.KEYS_WEATHER_ATTRIB}

        if data_list:
            for i in range(len(self.KEYS_WEATHER_ATTRIB[:-1])):
                summary[self.KEYS_WEATHER_ATTRIB[i]] = int(data_list[i])
            summary[self.KEY_DATE] = \
                datetime.strptime(data_list[-1], self.__DATE_FORMAT)
        return summary

    def year_summary(self):
        summary_string = f'{self.get_date().year}   '
        for key in self.KEYS_WEATHER_ATTRIB[:-1]:
            summary_string += f'{self.data[key]}      '
        return summary_string

    def hot_day_summary(self):
        """
        Formatted string for temperature
        :return:
        """
        return f'{self.get_date().year}  {self.get_date().strftime(self.DATE_FORMAT_OUTPUT)}    ' \
               f'{self.get_max_temp()}'

    def get_min_temp(self):
        return self.data["Min TemperatureC"]

    def get_max_temp(self):
        return self.data["Max TemperatureC"]

    def get_date(self):
        return self.data[self.KEY_DATE]

    def update_attributes_summary(self, weather_obj_new):
        """
        Update the date for hottest day
        Updates other attributes if necessary
        :param weather_obj_new:
        """
        if is_hotter_day(self.get_min_temp(), self.get_max_temp(), weather_obj_new.get_min_temp(),
                         weather_obj_new.get_min_temp()):
            self.data[self.KEY_DATE] = weather_obj_new.get_date()

        for key in self.KEYS_WEATHER_ATTRIB:
            if self.data[key] < weather_obj_new.data[key]:
                self.data[key] = weather_obj_new.data[key]
