"""
Helper Functions for weatherman task
"""

def replace_string_in_list(list_data, old_item, new_item):
    if old_item in list_data:
        list_data[list_data.index(old_item)] = new_item
