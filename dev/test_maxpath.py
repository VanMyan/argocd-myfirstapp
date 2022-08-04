def max_sum(array):
    max = array[0]
    curent_sum = array[0]
    for i in range(len(array)-1):
        curent_sum += array[i+1]
        if curent_sum > max :
            max = curent_sum
        if curent_sum < 0:
            curent_sum = 0
    return max

def test_max_sub1():
    a = [8,-5,4,-3,2,-10,3,-1,6,-3,8]
    result = max_sum(a)
    assert result == 13, "expected 13, actual{}}".format(result)


def test_max_sub2():
    a = []
    result = max_sum(a)
    assert result == None, "expected None, actual {}".format(result)