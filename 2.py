   # 2. Eng katta elementning indeksini topish
class ArrayOperations2:
    def __init__(self, arr):
        self.arr = arr

    def max_index(self):
        index = self.arr.index(max(self.arr)) + 1  
        print(f"Maksimal element indeksi (1-asosli): {index}")
        return index

my_array2 = ArrayOperations2([4, 8, 1, 10, 5])
my_array2.max_index() 
