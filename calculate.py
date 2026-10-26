"""Per-colour nominal-length purchasing calculation; not a swatch simulator."""
import argparse
from decimal import Decimal, InvalidOperation, ROUND_CEILING


def number(value, *, positive=False):
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError('Use a finite decimal number') from exc
    if not result.is_finite() or result < 0 or (positive and result == 0):
        raise ValueError('Length must be finite and nonnegative; ball length must be positive')
    return result


def balls(required_metres, metres_per_ball, extra_metres='0'):
    required = number(required_metres)
    per_ball = number(metres_per_ball, positive=True)
    extra = number(extra_metres)
    return int(((required + extra) / per_ball).to_integral_value(rounding=ROUND_CEILING))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--metres-per-ball', required=True)
    parser.add_argument('--colour', action='append', required=True, metavar='NAME=METRES')
    parser.add_argument('--extra-per-colour', default='0')
    args = parser.parse_args()
    try:
        seen = set()
        result = []
        for item in args.colour:
            name, metres = item.rsplit('=', 1)
            if not name.strip() or name.casefold() in seen:
                raise ValueError('Colour names must be nonempty and unique')
            seen.add(name.casefold())
            result.append((name, balls(metres, args.metres_per_ball, args.extra_per_colour)))
    except ValueError as exc:
        parser.error(str(exc))
    for name, count in result:
        print(f'{name}: {count} balls')
    print(f'Total: {sum(count for _, count in result)} balls; colours rounded separately')


if __name__ == '__main__':
    main()
