from src.code import function_x_power_y
import sys


def main():
    input_base = sys.argv[1]
    input_power = sys.argv[2]
    final_answer = function_x_power_y.x_power_y(input_base, input_power)
    print(final_answer)
