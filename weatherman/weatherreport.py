"""
For reading data and generating weather report
"""
import os
from collections import defaultdict
from datetime import datetime

from weatheryearlysummary import WeatherYearlySummary


class WeatherReport:
    KEY_DATE = "PKT"
    KEY_DATE_ALTER = "PKST"
    KEYS_WEATHER_ATTRIB = ["Max TemperatureC", "Min TemperatureC", "Max Humidity", "Min Humidity"]

    def __init__(self, path_to_dir):
        self.__path_to_dir = path_to_dir
        self.weather_data = defaultdict(WeatherYearlySummary)
        self.read_data()

    def __generate_attribute_index(self, header):
        attributes_index = [header.index(attributes) for attributes in self.KEYS_WEATHER_ATTRIB]
        try:
            attributes_index.append(header.index(self.KEY_DATE))
        except ValueError:
            attributes_index.append(header.index(self.KEY_DATE_ALTER))
        return attributes_index

    def __parse_line_attribute_data(self, header_index, line):
        return [int(line[index]) if line[index] else None for index in header_index]

    def __parse_line_date(self, index, line):
        return datetime.strptime(line[index], "%Y-%m-%d") if line[index] else None

    def __get_file_summary(self, name_of_file):
        with open(name_of_file) as weather_file:
            weather_file.readline()
            header = [item.strip() for item in weather_file.readline().split(",")]
            attributes_index = self.__generate_attribute_index(header)

            for line in weather_file.readlines()[:-1]:
                line_data = line.split(",")
                temp_data_attributes = self.__parse_line_attribute_data(attributes_index[:-1], line_data)
                temp_date = self.__parse_line_date(attributes_index[-1], line_data)
                if temp_date is not None:
                    self.weather_data[temp_date.year].update_attributes_summary(*temp_data_attributes, temp_date)

    def read_data(self):
        for file_name in os.listdir(f'.{self.__path_to_dir}'):
            self.__get_file_summary(f'.{self.__path_to_dir}/{file_name}')

    def generate_summary_report(self):
        print(f'{"Year":<10}{"MaxTemp":<10}{"MinTemp":<10}{"MaxHumidity":<10}{"MinHumidity":<20}')
        for year, summary in self.weather_data.items():
            print(summary.year_summary())

    def generate_hot_days_report(self):
        print(f'{"Year":<10}{"Date":<20}{"MaxTemp":<10}')
        for year, summary in self.weather_data.items():
            print(summary.hot_day_summary())
