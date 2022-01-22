import mathlib123

#pytest -k cal -v ---->to run all test case with cal as substring

def test_cal_square_1():
    result=mathlib123.cal_square(5)
    assert result==25

def test_cal_square_2():
    result=mathlib123.cal_square(6)
    assert result==36

def test_cal_square_3():
    result=mathlib123.cal_square(7)
    assert result==49

def test_cal_square_4():
    result=mathlib123.cal_square(8)
    assert result==64

def test_ca1_square_4():
    result=mathlib123.cal_square(8)
    assert result==64