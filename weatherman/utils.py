"""
Helper Functions for temperature comparison
"""


def is_hotter_day(old_min_temp, old_max_temp, new_min_temp, new_max_temp):
    return new_min_temp > old_min_temp and new_max_temp > old_max_temp


def replace_string_in_list(list_data, old_item, new_item):
    if old_item in list_data:
        list_data[list_data.index(old_item)] = new_item
