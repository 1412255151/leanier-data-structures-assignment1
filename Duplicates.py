def find_duplicates(arr):
    num_dict = {} 
    duplicates = set()


    for num in arr:

        if num in num_dict:
            duplicates.add(num)  
        else:
            num_dict[num] = 1  

    return list(duplicates)


values = list(map(int, input("Enter space-separated values for the array: ").split()))


duplicate_elements = find_duplicates(values)

if duplicate_elements:
    print(f"Duplicates in the array: {duplicate_elements}")
else:
    print("No duplicates found in the array.")