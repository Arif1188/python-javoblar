# 4. Manfiy va musbat elementlar sonini hisoblash
class ArrayOperations4:
    def __init__(self, arr):
        self.arr = arr

    def count_positive_negative(self):
        positive_count = sum(1 for x in self.arr if x > 0)
        negative_count = sum(1 for x in self.arr if x < 0)
        print(f"Positive count: {positive_count}, Negative count: {negative_count}")
        return positive_count, negative_count


my_array4 = ArrayOperations4([7, -2, -3, 4, -1, 0, 5])
my_array4.count_positive_negative()  
    
