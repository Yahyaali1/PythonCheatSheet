"""
Weather object for keeping relevant details
Provides keys for  data in dictionary
"""
from datetime import datetime
from utils import is_hotter_day


class WeatherObj:
    KEY_DATE = "PKT"
    __KEY_DATE_ALTER = "PKST"
    KEY_SUMMARY = "SUMMARY"
    KEYS_WEATHER_ATTRIB = ["Max TemperatureC", "Min TemperatureC", "Max Humidity", "Min Humidity"]
    __DATE_FORMAT = '%Y-%m-%d'
    DATE_FORMAT_OUTPUT = '%d/%m/%Y'

    def __init__(self, weather_data):
        self.data = self.__form_summary_dict(weather_data)

    def __form_summary_dict(self, data_dic):
        summary = {self.KEY_SUMMARY: {k: None for k in self.KEYS_WEATHER_ATTRIB},
                   self.KEY_DATE: None}
        if data_dic:
            for key in self.KEYS_WEATHER_ATTRIB:
                summary[self.KEY_SUMMARY][key] = int(data_dic[key])
            summary[self.KEY_DATE] = \
                datetime.strptime(data_dic[self.KEY_DATE], self.__DATE_FORMAT)

        return summary

    def year_summary(self):
        summary_string = f'{self.get_date().year}   '
        for key in self.KEYS_WEATHER_ATTRIB:
            summary_string += f'{self.data[self.KEY_SUMMARY][key]}      '
        return summary_string

    def hot_day_summary(self):
        """
        Formatted string for temperature
        :return:
        """
        return f'{self.get_date().year}  {self.data[self.KEY_DATE].strftime(self.DATE_FORMAT_OUTPUT)}    ' \
               f'{self.get_max_temp()}'

    def get_min_temp(self):
        return self.data[self.KEY_SUMMARY]["Min TemperatureC"]

    def get_max_temp(self):
        return self.data[self.KEY_SUMMARY]["Max TemperatureC"]

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
            if self.data[self.KEY_SUMMARY][key] < weather_obj_new.data[self.KEY_SUMMARY][key]:
                self.data[self.KEY_SUMMARY][key] = weather_obj_new.data[self.KEY_SUMMARY][key]