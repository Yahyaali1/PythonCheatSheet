from weatherreport import WeatherReport
import sys

ALLOWED_ATTRB = [1, 2]


def print_program_instructions():
    print("""
    Usage: weatherman [report#] [data_dir]
    [Report #]
    1 for Annual Max/Min Temperature
    2 for Hottest day of each year
    
    [data_dir]
    Directory containing weather data files
    """)


def validate_args(args_list):
    return True if args_list and int(args_list[0]) in ALLOWED_ATTRB and len(args_list) == 2 else False


def main():
    args = sys.argv[1:]
    if validate_args(args):
        weather_report = WeatherReport(args[1])
        try:
            weather_report.read_data()
        except FileNotFoundError:
            print("invalid dir")
        else:
            if int(args[0]) == 1:
                weather_report.generate_summary_report()
            else:
                weather_report.generate_hot_days_report()
    else:
        print_program_instructions()


main()
