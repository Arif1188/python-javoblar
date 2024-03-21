  # 5. Massivni k marta oldinga surish
class ArrayOperations5:
    def __init__(self, arr):
        self.arr = arr

    def rotate_forward(self, k):
        n = len(self.arr)
        k %= n  
        rotated_array = self.arr[-k:] + self.arr[:-k]
        print(f"{rotated_array}")
        return rotated_array


my_array5 = ArrayOperations5([1, 2, 3, 4, 5])
my_array5.rotate_forward(2)  