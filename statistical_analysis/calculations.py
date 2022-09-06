def average(arr, count):
    summ = 0

    for elem in arr:
        summ += elem

    summ = summ / count

    return summ

def dispersion(arr, count):
    aver = average(arr, count);
    num = 0;

    for elem in arr:
        num += float((elem - aver) ** 2)

    num /= count

    return num

def median(arr, count):
    arr2 = arr.copy()
    arr3 = sorted(arr2)
    half_count = int(count / 2)
    aver = 0

    if count % 2 == 0 and arr3[(half_count) - 1] != arr3[(half_count) + 1]:
        aver = float(arr3[(half_count) - 1])
        aver += float(arr3[(half_count) + 1])
        aver /= 2
    else:
        aver = float(arr3[half_count])

    return aver

_number = 0
_len = 0

def mode(arr):
    global _number
    global _len

    num = arr[0]
    count = 0
    del_num = []
    i = 0

    for elem in arr:
        if num == elem:
            count += 1
            del_num.append(i)
        i += 1

    a = len(del_num)

    while a > 0:
        arr.pop(del_num[a - 1])
        a -= 1

    if count > _len:
        _len = count
        _number = num

    if len(arr) > 1:
        mode(arr)

    return _number

arr_n = []
arr_p = []

def mathDistribution(arr, arr_count):
    num = arr[0]
    count = 0
    del_num = []
    i = 0

    for elem in arr:
        if num == elem:
            count += 1
            del_num.append(i)
        i += 1

    global arr_n
    global arr_p

    arr_n.append(num)
    count /= arr_count
    arr_p.append(count)

    a = len(del_num)

    while a > 0:
        arr.pop(del_num[a - 1])
        a -= 1

    if len(arr) > 0:
        mathDistribution(arr, arr_count)

    return 0

def expectedValue(arr, factor, count):
    result = 0

    global arr_n
    global arr_p

    arr_n = []
    arr_p = []

    mathDistribution(arr, count)

    i = 0
    arr_len = len(arr_n)

    while i < arr_len:
        result += ((arr_n[i] ** factor) * arr_p[i])
        i += 1

    return result

exp_v = 0
exp_v2 = 0
exp_v3 = 0
st_deviation = 0

def asymmetry(arr, count):
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()

    global exp_v
    global exp_v2
    global exp_v3
    global st_deviation

    exp_v = expectedValue(arr2, 1, count)
    exp_v2 = expectedValue(arr3, 2, count)
    exp_v3 = expectedValue(arr4, 3, count)
    st_deviation = (exp_v2 - (exp_v ** 2)) ** (0.5)
    cen_moment = exp_v3 - 3 * exp_v2 * exp_v + 2 * (exp_v ** 3)
    result = cen_moment / (st_deviation ** 3)

    return result

def excess(arr, count):
    exp_v4 = expectedValue(arr, 4, count)

    global exp_v
    global exp_v2
    global exp_v3
    global st_deviation

    cen_moment = exp_v4 - 4 * exp_v3 * exp_v + 6 * exp_v2 * (exp_v ** 2) - 3 * (exp_v ** 4)
    result = cen_moment / (st_deviation ** 4) - 3

    return result