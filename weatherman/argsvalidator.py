"""
Defines type functions for validating command line arguments
"""
import argparse
import os


def dir_validator(value):
    if not os.path.isdir(f'.{value}'):
        raise argparse.ArgumentTypeError(f'data_dir:{value} is not a valid dir')
    if os.access(f'.{value}', os.R_OK):
        return value
    else:
        raise argparse.ArgumentTypeError(f'readable_dir:{value} is not a readable dir')
