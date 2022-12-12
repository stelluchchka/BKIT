def sort_array(data, temp):
    if temp == 1:
        result = sorted(data, key = abs)[::-1]
        print(result)
    elif temp == 2:
        result_with_lambda = sorted(data, key = lambda x: abs(x))[::-1]
        print(result_with_lambda)
    else:
        print("ERROR")