import Lab2 as Lab2

def test_min_max():
    results = []
    input_arr = [1,3,4,5]
    results = Lab2.find_min_max(input_arr)
    assert(results == [1.0,5.0])

def test_average():
    input_arr = [1,3,4,5]
    results = Lab2.calc_average_temperature(input_arr)
    assert(results == 3.25)

def test_median():
    input_arr = [1,3,4,5]
    results = Lab2.calc_median_temperature(input_arr)
    assert(results == 3.5)