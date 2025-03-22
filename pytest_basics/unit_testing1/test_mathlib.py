#all the test file must have filename as well as function name begins ith "test_" prefix 

import mathlib

def test_calc_total():
        total=mathlib.calc_sum(4,5)
        assert total==9

def test_calc_multiply():
        result=mathlib.calc_mul(4,5)
        assert result==20

        