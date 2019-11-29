"""
Helper Functions for temperature comparison
"""

def is_hotter_day(old_min_temp, old_max_temp, new_min_temp, new_max_temp):
    return new_min_temp > old_min_temp and new_max_temp > old_max_temp


def replace_string_in_dict(dict_data, old_key, new_key):
    if old_key in dict_data:
        dict_data[new_key] = dict_data.pop(old_key)