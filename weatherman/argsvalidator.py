"""
Defines type functions for validating command line arguments
"""
import argparse
import os


def dir_validator(value):
    if not os.path.isdir(f'.{value}'):
        raise argparse.ArgumentTypeError("data_dir:{0} is not a valid dir".format(value))
    if os.access(f'.{value}', os.R_OK):
        return value
    else:
        raise argparse.ArgumentTypeError("readable_dir:{0} is not a readable dir".format(value))
