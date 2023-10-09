def find_kth_largest(arr, k):
    arr.sort(reverse=True)
    return arr[k - 1]

def find_kth_smallest(arr, k):
    arr.sort()
    return arr[k - 1]


values = list(map(int, input("Enter space-separated values for the array: ").split()))
k = int(input("Enter the value of K: "))

kth_largest = find_kth_largest(values, k)
kth_smallest = find_kth_smallest(values, k)

print(f"{k}th Largest number in the array: {kth_largest}")
print(f"{k}th Smallest number in the array: {kth_smallest}")