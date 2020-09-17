'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

def find_max(nums):
    current_max = None
    for n in nums:
        if current_max is None or n > current_max:
            current_max = n
    return current_max


def sliding_window_max(nums, k):
    # Your code here
    list_to_return = list()
    if k > len(nums):
        return "Window too large for data set."
    elif k == len(nums):
        list_to_return.append(find_max(nums))
        return list_to_return
    else:
        for i in range(0, len(nums)):
            check_slice = nums[i : (i + k)]
            if len(check_slice) < k:
                break
            else:
                list_to_return.append(find_max(check_slice))
    return list_to_return



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
