#!/usr/bin/env python3
from currency_convector.cli import get_parser
from currency_convector.convector import convert


def main():
    parser = get_parser()
    args = parser.parse_args()
    amount = convert(args.currency_from, args.currency_to, args.amount)
    print(amount)


if __name__ == '__main__':
    main()
