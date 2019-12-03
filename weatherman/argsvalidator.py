"""
Defines action class for validating command line arguments
"""
import argparse
import os


class DirValidator(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not os.path.isdir(f'.{values}'):
            raise argparse.ArgumentTypeError("data_dir:{0} is not a valid dir".format(values))
        if os.access(f'.{values}', os.R_OK):
            setattr(namespace, self.dest, values)
        else:
            raise argparse.ArgumentTypeError("readable_dir:{0} is not a readable dir".format(values))


class ReportNumberValidator(argparse.Action):
    REPORT_TYPES = [1, 2]

    def __call__(self, parser, namespace, values, option_string=None):
        if values not in self.REPORT_TYPES:
            raise argparse.ArgumentTypeError("report_type:{0} is not a valid report number".format(values))
        else:
            setattr(namespace, self.dest, values)
