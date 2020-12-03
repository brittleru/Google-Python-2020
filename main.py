from curs_3_package import module_1
from curs_3_package.module_2 import my_var as var, function as fun
from curs_3_package.factorial import *

# print(f"The email is: {EMAIL}")
# print(f"The username is: {USER}")

module_1.print_credentials()
module_1.function_from_a_module()

print("#-----" * 10 + "#")

print(var)
fun()

print(fact(3))