def add_one(list_tmp = None):
    if list_tmp is None:
        list_tmp = []
    list_tmp.append(1)
    return list_tmp


test_list = [5, 6, 7]

result1 = add_one(test_list)
assert result1 == [5, 6, 7, 1]

result2 = add_one()
assert result2 == [1]

result3 = add_one()
assert result3 == [1]
