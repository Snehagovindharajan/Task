import sys
from src.code.function_x_power_y import ScientificFunction


def main():
    obj_power = ScientificFunction()
    input_base = sys.argv[1]
    input_power = sys.argv[2]
    final_answer = obj_power.x_power_y(input_base, input_power)
    print(final_answer)
