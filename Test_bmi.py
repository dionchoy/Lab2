import bmi as bmi 

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.7, 65)
    assert(result == 0)

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.5, 65)
    assert(result == 1)

def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.7, 50)
    assert(result == -1)