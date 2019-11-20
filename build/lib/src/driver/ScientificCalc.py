"""Code to Find x power y"""
import logging

logging.basicConfig(filename='ScientificCalculatorLog.log', level=logging.ERROR, format='%(name)s - %(levelname)s - '
                                                                                        '%(message)s - %(asctime)s - '
                                                                                        '%(lineno)d - %(module)s - %('
                                                                                        'funcName)s - %(pathname)s')


class ScientificCalc:
    """x_power_y function to find the result"""

    def __init__(self):
        self.base = 0
        self.power = 0
    @classmethod
    def x_power_y(self, base_val, power_val):
        """first if condition is to find the power when given power value is positive and
        the second if condition is to find the result when the power is negative if power is zero
        it returns the value 1"""
        self.answer = 1
        if power_val == 0:
            return 1
        elif power_val % 2 == 0:
            return (self.x_power_y(base_val, int(power_val / 2)) *
                    self.x_power_y(base_val, int(power_val / 2)))
        else:
            if power_val > 0:
                return (base_val * self.x_power_y(base_val, int(power_val / 2)) *
                        self.x_power_y(base_val, int(power_val / 2)))
            else:
                return (self.x_power_y(base_val, int(power_val / 2)) *
                        self.x_power_y(base_val, int(power_val / 2))) / base_val

    @classmethod
    def var_initialization(self, base_no, power_no):
        try:
            base = float(base_no)
            power = float(power_no)
            return self.x_power_y(base, power)
        except ValueError as error:
            logging.error(error)
            return "Value Error"
