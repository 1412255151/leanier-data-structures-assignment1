def count_pairs_with_sum(arr, target_sum):
    count = 0
    num_dict = {} 
    

    for num in arr:
        complement = target_sum - num
        
      
        if complement in num_dict:
            count += num_dict[complement] 
        
       
        num_dict[num] = num_dict.get(num, 0) + 1
    
    return count


values = list(map(int, input("Enter space-separated values for the array: ").split()))
target_sum = int(input("Enter the target sum: "))


pair_count = count_pairs_with_sum(values, target_sum)

print(f"Number of pairs with sum {target_sum}: {pair_count}")