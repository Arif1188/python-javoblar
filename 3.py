  # 3. Manfiy va musbat elementlarni ajratish
class ArrayOperations3:
    def __init__(self, arr):
        self.arr = arr

    def segregate(self):
        self.arr.sort(key=lambda x: x >= 0)
        print(f"Ajratilgan massiv: {self.arr}")
        return self.arr

my_array3 = ArrayOperations3([0, -1, 2, -3, 4, -5])
my_array3.segregate()
