import argparse
import logging

from src.driver.ScientificCalc import ScientificCalc

logging.basicConfig(filename='ScientificCalculatorLog.log', level=logging.ERROR, format='%(name)s - %(levelname)s - '
                                                                                        '%(message)s - %(asctime)s - '
                                                                                        '%(lineno)d - %(module)s - %('
                                                                                        'funcName)s - %(pathname)s')


def main():
    try:
        obj_power = ScientificCalc()
        parser = argparse.ArgumentParser()
        parser.add_argument('--function', type=str, required=True, nargs='+')
        args = parser.parse_args()
        method_name = args.function
        if method_name[0] == 'x_power_y':
            input_base = method_name[1]
            input_power = method_name[2]
            final_answer = obj_power.x_power_y(input_base, input_power)
            print(final_answer)
    except IndexError as index:
        logging.error(index)
