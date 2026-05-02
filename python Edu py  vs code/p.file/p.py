# You are tasked with designing a Python class MathOperations to perform advanced mathematical operations on a list of integers. The class should include the following methods:

# square_and_sort(numbers): Computes the square of each number in the list and returns them in sorted order.
# reverse_and_multiply(numbers): Reverses the order of numbers in the list and multiplies each number by its index position.
# find_second_largest(numbers): Finds and returns the second largest number in the list.
# product_of_odd_numbers(numbers): Computes the product of all odd numbers in the list.
# Note: Do not write code to take input or to call or print the output; the same is implemented in the backend.
# Input
# Input a list of integers separated by spaces.
# Output
# Each line will contain the result of all four functions in the given order.
# Example
# Sample Input:
# 4 7 1 9 3

# Sample Output:

# Squared and sorted numbers: [1, 9, 16, 49, 81]
# Reversed and multiplied numbers: [0, 9, 2, 21, 16]
# Second largest number: 7
# Product of odd numbers: 189




# CLASS MathOperations:
#     METHOD square_and_sort(numbers):
#         NEW_LIST = []
#         FOR each n IN numbers:
#             APPEND (n * n) TO NEW_LIST
#         SORT NEW_LIST in ascending order
#         RETURN NEW_LIST

#     METHOD reverse_and_multiply(numbers):
#         REVERSED_LIST = numbers reversed
#         RESULT_LIST = []
#         FOR index FROM 0 TO length(REVERSED_LIST) - 1:
#             APPEND (REVERSED_LIST[index] * index) TO RESULT_LIST
#         RETURN RESULT_LIST

#     METHOD find_second_largest(numbers):
#         UNIQUE_NUMBERS = convert numbers to SET to remove duplicates
#         SORT UNIQUE_NUMBERS in descending order
#         IF length(UNIQUE_NUMBERS) < 2:
#             RETURN None
#         RETURN UNIQUE_NUMBERS[1]

#     METHOD product_of_odd_numbers(numbers):
#         PRODUCT = 1
#         HAS_ODD = False
#         FOR each n IN numbers:
#             IF n % 2 != 0:
#                 PRODUCT = PRODUCT * n
#                 HAS_ODD = True
#         IF HAS_ODD is False: RETURN 0
#         RETURN PRODUCT

class MathOperations:
    @staticmethod
    def square_and_sort(numbers):
        # Square each number and return sorted list
        return sorted([n**2 for n in numbers])

    @staticmethod
    def reverse_and_multiply(numbers):
        # Reverse the list and multiply value by its index
        reversed_nums = numbers[::-1]
        return [val * i for i, val in enumerate(reversed_nums)]

    
    def find_second_largest(numbers):
        
        unique_nums = list(set(numbers))
        if len(unique_nums) < 2:
            return None
        unique_nums.sort()
        return unique_nums[-2]

    
    def product_of_odd_numbers(numbers):
        
        product = 1
        odd_found = False
        for n in numbers:
            if n % 2 != 0:
                product *= n
                odd_found = True
        return product if odd_found else 0