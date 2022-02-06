import argparse


def get_parser():
    parser = argparse.ArgumentParser(description='Convert currency')
    parser.add_argument('currency_from', default='RUB', type=str)
    parser.add_argument('currency_to', type=str)
    parser.add_argument('amount', type=float)

    return parser
