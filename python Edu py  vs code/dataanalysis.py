# import pandas as pd

# df = pd.read_csv("StudentsPerformance.csv")

# print(df.describe

# If a list containing less than 9 elements is passed into the function,
# it should raise a ValueError exception with the message: "List must contain nine numbers."
# The values in the returned dictionary should be lists and not Numpy arrays

# list = []

# for i  in range(10):
#     number = (input("enter Number: "))
#     i+= 1
#     list.append(number)

# if len(list)>8:
#         print("value error! 'Please Enter 9 numbers only")
# else:
#      print(list)



# numbers = []

# for i in range(10):
#     val = input("Enter Number: ")
#     numbers.append(val)
    
#     if len(numbers) >= 9:
#         print("🚨 ERROR: I told you only 9! I'm closing now.")
#         break # This actually stops the loop dead in its tracks
#     else:
#         print(f"Current list: {numbers}")


# Convert the input to a number immediately
a = int(input("enter a num : ")) 

b = a * a
print(b)


