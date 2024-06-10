import re
import argparse

# This function is for dealing with 'NA' and 'Unknown' cases
def data_cleaning(value):
    if value in ['NA', 'Unknown', 'unknown']:
        return None
    return value

# This function is for removing suffixes to merge metabolomites
def merge_names(name):
    return re.sub(r'\(\d+\)$', '', name)

def db_format(filename):
    if not filename.endswith('.db'):
        raise argparse.ArgumentTypeError("Your Database name must have a .db extension at the end")
    return filename