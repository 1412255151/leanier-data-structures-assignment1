values = list(map(int, input("Enter space-separated values for the array: ").split()))


left = 0
right = len(values) - 1

while left <= right:
   
    if values[left] < 0:
        left += 1
  
    elif values[right] >= 0:
        right -= 1
   
    else:
        values[left], values[right] = values[right], values[left]
        left += 1
        right -= 1

print("Array after moving negative elements to one side:", values)