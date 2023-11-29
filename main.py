class Average:

    def __init__(self):
        pass

    @staticmethod
    def average_value(arr: list) -> int:
        """
        Среднее значения списка
        """
        if not arr:
            return 0
        return sum(arr) / len(arr)
    def comparison_numbers(self, arr1, arr2):
        """
        Функция сравнение средних значений из двух списков
        """
        array1 = self.average_value(arr1)
        array2 = self.average_value(arr2)
        if array1 > array2:
            return "Первый список имеет большее среднее значение"
        if array2 > array1:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
