"""
For reading data and generating weather report
"""
import os
from weatherobj import WeatherObj
from utils import replace_string_in_dict


class WeatherReport:
    __FILE_PREFIX = "lahore_weather"
    __KEY_DATE = "PKT"
    __KEY_DATE_ALTER = "PKST"

    def __init__(self, path_to_dir):
        self.__path_to_dir = path_to_dir
        self.weather_data = dict()

    def __get_file_list(self):
        return [f'.{self.__path_to_dir}/{file_name}' for file_name in os.listdir(f'.{self.__path_to_dir}')
                if file_name.startswith(self.__FILE_PREFIX)]

    def __should_ignore_reading(self, line):
        for key in WeatherObj.KEYS_WEATHER_ATTRIB:
            if key not in line or not line[key]:
                return True
        else:
            return False

    def __get_file_summary(self, name_of_file):
        summary = None
        with open(name_of_file) as weather_file:
            weather_file.readline()
            header = [item.strip() for item in weather_file.readline().split(",")]

            for line in weather_file.readlines()[:len(weather_file.readlines())-1]:
                temp_data = dict(zip(header, line.split(",")))
                replace_string_in_dict(temp_data, self.__KEY_DATE_ALTER, self.__KEY_DATE)

                if not self.__should_ignore_reading(temp_data):
                    temp_summary = WeatherObj(temp_data)
                    if not summary:
                        summary = temp_summary
                    else:
                        summary.update_attributes_summary(temp_summary)
        return summary

    def __update_year_summary(self, new_summary):
        if new_summary:
            year = new_summary.data[WeatherObj.KEY_DATE].year
            if year in self.weather_data:
                self.weather_data[year].update_attributes_summary(new_summary)
            else:
                self.weather_data[year] = new_summary

    def read_data(self):
        files_list = self.__get_file_list()
        for file_name in files_list:
            new_summary = self.__get_file_summary(file_name)

            self.__update_year_summary(new_summary)

    def generate_summary_report(self):
        print(f'Year    MaxTemp    MinTemp  MaxHumidity     MinHumidity')
        for year, summary in self.weather_data.items():
            print(summary.year_summary())

    def generate_hot_days_report(self):
        print(f'Year    Date    MaxTemp')
        for year, summary in self.weather_data.items():
            print(summary.hot_day_summary())
