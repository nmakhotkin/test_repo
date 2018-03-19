import argparse
import math

from mlboardclient.api import client

m = client.Client()

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--argument',
        help='Define x for func',
        dest='x',
        type=float
    )
    
    return parser

def f(x):
    return math.exp(-(x - 2)**2) + math.exp(-(x - 6)**2/10) + 1/ (x**2 + 1)

def main():
    parser = get_parser()
    parser.parse_args()
    
    checked_value = f(args.x)
    m.update_task_info({'checked_value': float(checked_value)})


if __name__ == '__main__':
    main()
