import sys
from src.driver.ScientificCalc import ScientificCalc
import argparse
import logging


# logging.basicConfig(filename='ScientificCalculatorLog.log', filemode='w', level=logging.ERROR, format='%(name)s - %('
#                                                                                                       'levelname)s - '
#                                                                                                       '%(message)s - '
#                                                                                                       '%(asctime)s')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--function', type=str, required=True)
    args = parser.parse_args()
    parser.add_argument('--param', type=int, required=True, nargs=2)
    args_param = parser.parse_args()
    method_name = args.function
    print(method_name)
    parameters = args_param.param
    print(parameters)
    obj_power = ScientificCalc()
    input_base = sys.argv[1]
    input_power = sys.argv[2]
    # input_base = 2
    # input_power = 2
    final_answer = obj_power.x_power_y(input_base, input_power)
    print(final_answer)
