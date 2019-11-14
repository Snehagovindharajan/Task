"""Code to Find x power y"""
import sys


def x_power_y(base_val, power_val):
    """first if condition is to find the power when given power value is positive and
    the second if condition is to find the result when the power is negative if power is zero
    it returns the value 1"""
    try:
        base = int(base_val)
        power = int(power_val)
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
    except ValueError as e:
        print(e)
        return "Value Error"
