# 1-bo'lim
class ArrayOperations1:
    def __init__(self, arr):
        self.arr = arr

    def sum(self):
        result = sum(self.arr)
        print(f"Sum: {result}")
        return result

    def product(self):
        result = 1
        for num in self.arr:
            result *= num
        print(f"Product: {result}")
        return result

    def max(self):
        result = max(self.arr)
        print(f"Max: {result}")
        return result

    def min(self):
        result = min(self.arr)
        print(f"Min: {result}")
        return result


my_array = ArrayOperations1([2, 3, 5, 7, 11])


my_array.sum()      
my_array.product() 
my_array.max()      
my_array.min()   
    
    

