from src.code import function_x_power_y
import sys


def main():
    try:
        input_base = int(sys.argv[1])
        input_power = int(sys.argv[2])
        final_answer = function_x_power_y.x_power_y(input_base, input_power)
        print(final_answer)
    except ValueError as e:
        print("Value Error : ", e)
        print("Enter a valid Integer")
    except Exception as e:
        print(e)
