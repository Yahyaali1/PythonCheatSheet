import argparse

from argsvalidator import dir_validator
from weatherreport import WeatherReport

parser = argparse.ArgumentParser(epilog="For forming report on the data provided in data_dir")
parser.add_argument("report_type", type=int, choices=[1, 2], help="""1 for Annual Max/Min Temperature
    2 for Hottest day of each year""")
parser.add_argument("data_dir", type=dir_validator, help="Directory containing weather data files")


def main():
    try:
        args = parser.parse_args()
    except argparse.ArgumentTypeError as exception:
        print(str(exception))
    else:
        weather_report = WeatherReport(args.data_dir)
        weather_report.read_data()
        if args.report_type == 1:
            weather_report.generate_summary_report()
        else:
            weather_report.generate_hot_days_report()


if __name__ == "__main__":
    main()
