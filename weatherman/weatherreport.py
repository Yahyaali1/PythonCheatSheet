"""
For reading data and generating weather report
"""
import os
from datetime import datetime

from utils import replace_string_in_list
from weatheryearlysummary import WeatherYearlySummary


class WeatherReport:

    def __init__(self, path_to_dir):
        self.__path_to_dir = path_to_dir
        self.weather_data = dict()

    def __generate_header_index(self, header):
        return [header.index(attributes) for attributes in WeatherYearlySummary.KEYS_WEATHER_ATTRIB]

    def __parse_line_attribute_data(self, header_index, line):
        return [int(line[index]) if line[index] else None for index in header_index]

    def __parse_line_date(self, index, line):
        return datetime.strptime(line[index], "%Y-%m-%d") if line[index] else None

    def __get_file_summary(self, name_of_file):
        with open(name_of_file) as weather_file:
            weather_file.readline()
            header = [item.strip() for item in weather_file.readline().split(",")]
            replace_string_in_list(header, WeatherYearlySummary.KEY_DATE_ALTER, WeatherYearlySummary.KEY_DATE)
            header_index = self.__generate_header_index(header)

            for line in weather_file.readlines()[:-1]:
                line_data = line.split(",")
                temp_data_attributes = self.__parse_line_attribute_data(header_index[:-1], line_data)
                temp_date = self.__parse_line_date(header_index[-1], line_data)
                if temp_date is not None:
                    self.__update_year_summary(temp_data_attributes, temp_date)

    def __update_year_summary(self, new_summary_attributes, new_date):
            year = new_date.year
            if year in self.weather_data:
                self.weather_data[year].update_attributes_summary(new_summary_attributes, new_date)
            else:
                self.weather_data[year] = WeatherYearlySummary(new_summary_attributes, new_date)

    def read_data(self):
        for file_name in os.listdir(f'.{self.__path_to_dir}'):
            self.__get_file_summary(f'.{self.__path_to_dir}/{file_name}')

    def generate_summary_report(self):
        print(f'Year    MaxTemp    MinTemp  MaxHumidity     MinHumidity')
        for year, summary in self.weather_data.items():
            print(summary.year_summary())

    def generate_hot_days_report(self):
        print(f'Year    Date    MaxTemp')
        for year, summary in self.weather_data.items():
            print(summary.hot_day_summary())
