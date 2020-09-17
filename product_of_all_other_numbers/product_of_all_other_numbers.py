'''
Input: a List of integers
Returns: a List of integers
'''

def get_product(arr):
    product = 1
    for x in range(0, len(arr) - 1):
        factor = arr[x]
        product *= factor
    return product

def product_of_all_other_numbers(arr):
    ret_list = list()
    if len(arr) < 2:
        return -1
    elif len(arr) == 2:
        replacement = arr[1]
        del arr[1]
        arr.insert(0, replacement)
        return arr

    for i in range(0, len(arr) - 1):
        lhs = arr[ : i]
        rhs = arr[i+1 : ]
        product_to_append = get_product(lhs) * get_product(rhs)
        ret_list.append(product_to_append)
    return ret_list


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
