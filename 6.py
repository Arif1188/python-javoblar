 # 6. Massivni k marta orqaga surish
class ArrayOperations6:
    def __init__(self, arr):
        self.arr = arr

    def rotate_backward(self, k):
        n = len(self.arr)
        k %= n  # Adjust for k greater than the length of the array
        rotated_array = self.arr[k:] + self.arr[:k]
        print(f" {rotated_array}")
        return rotated_array


my_array6 = ArrayOperations6([1, 2, 3, 4, 5, 6])
my_array6.rotate_backward(3)  