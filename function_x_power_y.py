"""Code to Find x power y"""
import sys


def x_power_y(base, power):
    """first if condition is to find the power when given power value is positive and
    the second if condition is to find the result when the power is negative if power is zero
    it returns the value 1"""
    answer = 1
    if power > 0:
        for num in range(1, power + 1):
            answer = answer * base
    if power < 0:
        pos_power = power * -1
        pos_base = 1 / base
        for num in range(1, pos_power + 1):
            answer = answer * pos_base
    return answer


if __name__ == '__main__':
    BASE_INPUT = int(sys.argv[1])
    POWER_INPUT = int(sys.argv[2])
    RESULT = x_power_y(BASE_INPUT, POWER_INPUT)
    print(RESULT)
