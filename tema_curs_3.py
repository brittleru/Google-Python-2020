# Create a function with infinite number of parameters and add the parameters if
# they are integer
print("#-----" * 10 + "#")


def infinite_parameters(*args, **kwargs):
    result = 0
    for argument in args:
        if type(argument) == int or type(argument) == float:
            result += argument
        else:
            ...
    return result


print(f'First result = {infinite_parameters(1, 5, -3, "abc", [12, 56, "cad"])}')
print(f'Second result = {infinite_parameters()}')

# Expected to also add param_1 but in
print(f'Last result = {infinite_parameters(2, 4, "abc", param_1=2)}')

print("#-----" * 10 + "#")
print("\n")
print("#-----" * 10 + "#")

# Create a function that read user input and return it's value if the user enter
# an integer number else return 0


def user_input():
    user = input("Please enter an integer: ")
    try:
        int(user)
        print("Nice, your number is")
    except Exception as e:
        user = 0
        print(f"You didn't enter an integer... Now you caused the error {e}")
    finally:
        return user


print(user_input())
print("#-----" * 10 + "#")
print("\n")


# Access the module with the recursive sums
from tema_curs_3_package.recursive_sum import recursive_sum as rs
from tema_curs_3_package.recursive_even_sum import recursive_even_sum as res
from tema_curs_3_package.recursive_odd_sum import recursive_odd_sum as rod

num = 10
print("#-----" * 10 + "#")
print(f"The recursive sum of all numbers form 0 to {num} is = {rs(num)}")
print(f"The recursive sum of all even numbers from 0 to {num} is = {res(num)}")
print(f"The recursive sum of all odd numbers from 0 to {num} is = {rod(num)}")
print("#-----" * 10 + "#")