import sys
from src.driver.ScientificCalc import ScientificCalc


def main():
    obj_power = ScientificCalc()
    input_base = sys.argv[1]
    input_power = sys.argv[2]
    final_answer = obj_power.x_power_y(input_base, input_power)
    print(final_answer)
