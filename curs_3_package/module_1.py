from . import *


def print_credentials():
    print(EMAIL, " ", USER)

def function_from_a_module():
    print(f"I'm a function from {__name__}")