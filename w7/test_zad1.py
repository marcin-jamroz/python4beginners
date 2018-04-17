import zad1

def test_flat_list():
    result = zad1.flatten([1, 2, 3, 4])

    assert result == [1, 2, 3, 4]

def test_empty_list():
    result = zad1.flatten([])
    assert result == []

def test_one_element():
    result = zad1.flatten([1])
    assert [1] == result

def test_list_in_list():
    result = zad1.flatten([1, 2, [3, 4]])
    assert [1, 2, 3, 4] == result

def test_list_in_list_in_list():
    result = zad1.flatten([1, [2, [3, 4]]])
    assert [1, 2, 3, 4] == result