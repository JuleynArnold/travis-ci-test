import unittest
import calc

class test_calc(unittest.TestCase):

    #Test the parsing of whole single digit numbers
    def test_single_digit_number_parse(self):
        zero_to_nine = '0123456789'
        for i in range (0,9):
            assert(calc.evaluate_single_digit(zero_to_nine[i]) == i)

    #Test the parsing of for whole positive numbers
    def test_postive_number_parse(self):
        #Scaling
        assert(calc.evaluate_positive_number('1') == 1)
        assert(calc.evaluate_positive_number('10') == 10)
        assert(calc.evaluate_positive_number('100') == 100)
        assert(calc.evaluate_positive_number('1000') == 1000)
        assert(calc.evaluate_positive_number('10000') == 10000)
        assert(calc.evaluate_positive_number('100000') == 100000)
        #Random values
        assert(calc.evaluate_positive_number('124809214') == 124809214)
        assert(calc.evaluate_positive_number('821944014122') == 821944014122)
        assert(calc.evaluate_positive_number('5395783105175091') == 5395783105175091)
        #Edge case
        assert(calc.evaluate_positive_number('9223372036854775807') == 9223372036854775807)

    #Test the parsing of postive floating point numbers
    def test_floating_point_numbers_parse(self):
        #Basic
        assert(calc.evaluate_floating_point_number('1.0') == 1)
        assert(calc.evaluate_floating_point_number('1.01') == 1.01)
        assert(calc.evaluate_floating_point_number('1.012') == 1.012)
        assert(calc.evaluate_floating_point_number('1.0123') == 1.0123)

        assert(calc.evaluate_floating_point_number('213.124') == 213.124)
        assert(calc.evaluate_floating_point_number('53215.21124') == 53215.21124)

    #Test the parsing of positive single digit hexadecimal numbers
    def test_single_digit_hexadecimal_parse(self):
        myList = '0123456789ABCDEF'
        num = 0
        for i in myList:
            assert(calc.evaluate_single_hexadecimal_digit(i) == num)
            num = num + 1

    #Test the parsing of positive hexadecimal numbers
    def test_hexadecimal_parse(self):
        myList ='0123456789ABCDEF'
        #Test all possible values
        for one in myList:
            for two in myList:
                assert(calc.evaluate_hexadecimal(one + two) == (calc.evaluate_single_hexadecimal_digit(one) * 16 + calc.evaluate_single_hexadecimal_digit(two)))

    #Test everything previously + Negative decimal/floating numbers and hexadecimal including 0x notation
    def test_evaluate_section(self):
        assert(calc.evaluate_section('-10000') == -10000)
        assert(calc.evaluate_section('-124809214') == -124809214)
        assert(calc.evaluate_section('-821944014122') == -821944014122)

        assert(calc.evaluate_section('-1.0123') == -1.0123)
        assert(calc.evaluate_section('-213.124') == -213.124)
        assert(calc.evaluate_section('-53215.21124') == -53215.21124)

        assert(calc.evaluate_section('0x01') == 1)
        assert(calc.evaluate_section('0x0A') == 10)
        assert(calc.evaluate_section('0xAF') == 175)
        assert(calc.evaluate_section('0xC4') == 196)
        assert(calc.evaluate_section('0xF9') == 249)

if __name__ == '__main__':
    unittest.main(verbosity=2)
