def find_pair(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            print(f"Pair found ({complement}, {num})")
            return
        
        seen[num] = i
        
    print("Pair not found.")

#Test Case 1
print("Input 1:")
nums1 = [8, 7, 2, 5, 3, 1]
target1 = 10
find_pair(nums1, target1)
print(f"Target was:",target1)

#Test Case 2
print("\nInput 2:")
nums2 = [5, 2, 6, 8, 1, 9]
# target2 = 12
target2 = 14

print(f"Target was:",target2)
find_pair(nums2, target2)