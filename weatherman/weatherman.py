from weatherreport import WeatherReport
import sys
import argparse

PROGRAM_INSTRUCTION = """
    Usage: weatherman [report_type] [data_dir]
    [Report #]
    1 for Annual Max/Min Temperature
    2 for Hottest day of each year
    
    [data_dir]
    Directory containing weather data files
    """

parser = argparse.ArgumentParser(description=PROGRAM_INSTRUCTION)
parser.add_argument("report_type", type=int)
parser.add_argument("data_dir", type=str)


def main():
    args = parser.parse_args()
    weather_report = WeatherReport(args.data_dir)
    try:
        weather_report.read_data()
    except FileNotFoundError:
        print("invalid dir")
    else:
        if args.report_type == 1:
            weather_report.generate_summary_report()
        else:
            weather_report.generate_hot_days_report()


if __name__ == "__main__":
    main()
