# 10. Massivni teskarisiga aylantirish
class ArrayOperations10:
    def __init__(self, arr):
        self.arr = arr

    def reverse(self):
        reversed_array = self.arr[::-1]
        print(f"Ro'yxatning teskari tartibi: {reversed_array}")
        return reversed_array

my_array10 = ArrayOperations10([1, 2, 3, 4, 5])
my_array10.reverse()