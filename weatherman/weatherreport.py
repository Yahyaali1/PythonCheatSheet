"""
For reading data and generating weather report
"""
import os
from datetime import datetime


class WeatherReport:
    __FILE_PREFIX = "lahore_weather"
    __KEY_DATE = "PKT"
    __KEY_SUMMARY = "SUMMARY"
    __KEYS_WEATHER_ATTRIB = ["Max TemperatureC", "Min TemperatureC", "Max Humidity", "Min Humidity"]
    __DATE_FORMAT = '%Y-%m-%d'

    def __init__(self, path_to_dir):
        self.__path_to_dir = path_to_dir
        self.weather_data = dict()

    def __get_file_list(self):
        return [file_name for file_name in os.listdir(f'.{self.__path_to_dir}')
                      if file_name.startswith(self.__FILE_PREFIX)]

    def __update_attributes_summary(self, summary_old, summary_new):
        """
        Update the date for hottest day
        Updates other attributes if necessary
        :param summary_old:
        :param summary_new:
        :return:
        """
        if self.__is_hotter_day(summary_old, summary_new[self.__KEY_SUMMARY]["Min TemperatureC"],
                                summary_new[self.__KEY_SUMMARY]["Max TemperatureC"]):
            summary_old[self.__KEY_DATE] = summary_new[self.__KEY_DATE]

        for key in self.__KEYS_WEATHER_ATTRIB:
            if summary_old[self.__KEY_SUMMARY][key] < summary_new[self.__KEY_SUMMARY][key]:
                summary_old[self.__KEY_SUMMARY][key] = summary_new[self.__KEY_SUMMARY][key]

    def __is_hotter_day(self, summary, new_min_temp, new_max_temp):
        return new_min_temp > summary[self.__KEY_SUMMARY]["Min TemperatureC"] and \
               new_max_temp > summary[self.__KEY_SUMMARY]["Max TemperatureC"]

    def __form_summary_dict(self, data_dic):
        summary = {self.__KEY_SUMMARY: {k: None for k in self.__KEYS_WEATHER_ATTRIB},
                   self.__KEY_DATE: None}
        if data_dic:
            for key in self.__KEYS_WEATHER_ATTRIB:
                summary[self.__KEY_SUMMARY][key] = int(data_dic[key])
            summary[self.__KEY_DATE] = datetime.strptime(data_dic[self.__KEY_DATE], self.__DATE_FORMAT)
        return summary

    def __get_file_summary(self, name_of_file):
        summary = {}
        with open(name_of_file) as weather_file:
            blank = weather_file.readline()
            header = weather_file.readline()
            for line in weather_file.readlines()[:len(weather_file.readlines())-1]:
                temp_data = dict(zip(header, line.split(",")))
                temp_summary = self.__form_summary_dict(temp_data)
                if not summary:
                    summary = temp_summary
                else:
                    self.__update_attributes_summary(summary, temp_summary)
        return summary

    def read_data(self):
        files_list = self.__get_file_list()
        for file_name in files_list:
            summary = self.__get_file_summary(file_name)
            if summary[self.__KEY_DATE].year in self.weather_data:
                self.__update_attributes_summary(self.weather_data[summary[self.__KEY_DATE].year], summary)
            else:
                self.weather_data[summary[self.__KEY_DATE].year] = summary

    def __form_year_summary_string(self, summary):
        summary_string = ""
        for keys in self.__KEYS_WEATHER_ATTRIB:
            summary_string += f''
    def generate_summary_report(self):
        print(f'')
        for year, summary in self.weather_data:
            print(f'{year}  {self.__form_year_summary_string(summary)}')

    def generate_hot_days_report(self):
        pass

