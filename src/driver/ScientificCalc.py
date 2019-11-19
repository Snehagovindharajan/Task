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
        self.answer = 1

    def x_power_y(self, base_val, power_val):
        """first if condition is to find the power when given power value is positive and
        the second if condition is to find the result when the power is negative if power is zero
        it returns the value 1"""
        try:
            self.base = int(base_val)
            self.power = int(power_val)
            if self.power > 0:
                for num in range(1, self.power + 1):
                    self.answer = self.answer * self.base
            if self.power < 0:
                pos_power = self.power * -1
                pos_base = 1 / self.base
                for num in range(1, pos_power + 1):
                    self.answer = self.answer * pos_base
            return self.answer
        except ValueError as error:
            logging.error(error)
            return "Value Error"
