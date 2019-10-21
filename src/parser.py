"""
Argument parser for the project.
The script executor needs only three arguments: repository url, commit hash and a script argument
"""
import argparse

parser = argparse.ArgumentParser(description='Executes a script cloned from a given git repo.')
parser.add_argument('url',
                    metavar='url',
                    type=str,
                    help='git repository url which will be cloned')
parser.add_argument('commit',
                    metavar='commit',
                    type=str,
                    help='commit hash')
parser.add_argument('argument',
                    metavar='x',
                    type=float,
                    help='a float argument for script')


def parse_args():
    args = parser.parse_args()
    return args
