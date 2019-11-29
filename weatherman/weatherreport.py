"""
For reading data and generating weather report
"""
import os
from weatheryearlysummary import WeatherYearlySummary
from utils import replace_string_in_dict


class WeatherReport:

    def __init__(self, path_to_dir):
        self.__path_to_dir = path_to_dir
        self.weather_data = dict()

    def __should_ignore_reading(self, line):
        for key in WeatherYearlySummary.KEYS_WEATHER_ATTRIB[:-1]:
            if key not in line or not line[key]:
                return True
        else:
            return False

    def __get_file_summary(self, name_of_file):
        summary = None
        with open(name_of_file) as weather_file:
            weather_file.readline()
            header = [item.strip() for item in weather_file.readline().split(",")]

            for line in weather_file.readlines()[:-1]:
                temp_data = dict(zip(header, line.split(",")))
                replace_string_in_dict(temp_data, WeatherYearlySummary.KEY_DATE_ALTER, WeatherYearlySummary.KEY_DATE)

                if not self.__should_ignore_reading(temp_data):
                    temp_summary = WeatherYearlySummary(temp_data)
                    if not summary:
                        summary = temp_summary
                    else:
                        summary.update_attributes_summary(temp_summary)
        return summary

    def __update_year_summary(self, new_summary):
        if new_summary:
            year = new_summary.data[WeatherYearlySummary.KEY_DATE].year
            if year in self.weather_data:
                self.weather_data[year].update_attributes_summary(new_summary)
            else:
                self.weather_data[year] = new_summary

    def read_data(self):
        for file_name in os.listdir(f'.{self.__path_to_dir}'):
            new_summary = self.__get_file_summary(f'.{self.__path_to_dir}/{file_name}')

            self.__update_year_summary(new_summary)

    def generate_summary_report(self):
        print(f'Year    MaxTemp    MinTemp  MaxHumidity     MinHumidity')
        for year, summary in self.weather_data.items():
            print(summary.year_summary())

    def generate_hot_days_report(self):
        print(f'Year    Date    MaxTemp')
        for year, summary in self.weather_data.items():
            print(summary.hot_day_summary())
