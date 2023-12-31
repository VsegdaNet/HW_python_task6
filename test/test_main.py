from main import Average
import pytest

concentrate = Average()


# первый список больше второго
def test_first_more():
    list1 = [1, 2, 5, 5]
    list2 = [1, 2, 1, 1]
    assert concentrate.comparison_numbers(list1, list2) == "Первый список имеет большее среднее значение"



# второй список больше первого
def test_second_more():
    list1 = [1, 2, 1, 1]
    list2 = [1, 2, 5, 5]
    assert concentrate.comparison_numbers(list1, list2) == "Второй список имеет большее среднее значение"


# списки равны
def test_equality():
    list1 = [1, 2, 1, 1]
    list2 = [1, 2, 1, 1]
    assert concentrate.comparison_numbers(list1, list2) == "Средние значения равны"


# возвращает 0 потому что список пуст
def test_empty_list():
    list1 = []
    list2 = []
    assert concentrate.comparison_numbers(list1, list2) == "Средние значения равны"


# проверка корректности нахождения среднего значения
def test_empty():
    list2 = [1, 2, 3]
    assert concentrate.average_value(list2) == 2
