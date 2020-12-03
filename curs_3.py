import random

print("Curs 3")
print("\n")

my_var = 5

# Imensul if
if my_var < 6:
    print('Variabila noastra este mai mica decat 6')
elif my_var < 10:
    print('Variabila noastra este mai mare decat 6 si mai mica decat 10')
elif my_var < 25:
    print("Variabilla noastra este destul de mare")
else:
    print("Variabila noastra este mare")

# Inimaginabilul tenary
apples = 3
has_apples = "Are mere" if apples else "Nu are mere"
print(has_apples)

has_apples = "Nu are mere"
if apples:
    has_apples = "Are mere"

print(has_apples)

# Marele while
counter = 0
while counter < 10:
    print(counter)
    counter += 1

# Giganticul for
for i in range(10):
    print(i)

# Superbul list comprehension
choises = [i for i in range(11)]
print(choises)

# List comp -> in for
lista = []
for i in range(11):
    lista.append(i)
print(lista)

# Impunatorul break
while 1:
    random_choise = random.choice(choises)
    if random_choise % 3 == 0:
        break
    print(f"Random choise is {random_choise}")

print(f'Exit Random choise is {random_choise}')

# Invincibilul contiune
for i in range(10):
    if i % 2 != 0:
        continue
    print(f'Numarul {i} este un numar par')


# Incredibilele functii
def my_function(list_parameter):
    local_list_parameter = list_parameter[:]
    local_list_parameter.append(4)
    print(local_list_parameter)


list_param = [1, 2, 3]
my_function(list_param)
print(list_param)


def my_second_function(name, age):
    return f'''My name is {name}. I'm {age} years old.'''


print(my_second_function("Medi", 22))


def default_parameters_func(name, age, job_name="Student", has_car=True):
    has_car_str = "a car" if has_car else "no car"
    print("#-----" * 10 + "#")
    return f'''My name is {name}.
I'm {age} years old.
I work as a {job_name}.
And I have {has_car_str}
    '''


print(default_parameters_func("Medi", 22, "Software Developer"))
print(default_parameters_func("Laravel", 10))
print(default_parameters_func("Nume", "Varsta", has_car=False, job_name="IDk"))

dictionar_parameters = {
    'job_name': 'Developer',
    'has_car': False
}


def not_finite_number_of_args(*args, **kwargs):
    for arg in args:
        print(f'Current argument is {arg}')

    print("#-----" * 10 + "#")

    for key in kwargs.keys():
        print(f'The key is {key} has and it has the value {kwargs[key]}')

    print("#-----" * 10 + "#")
    print(args)
    print(kwargs)


not_finite_number_of_args("Medi")
not_finite_number_of_args("Medi", "are", "mere")

not_finite_number_of_args(name="Medi", verb="are", substantiv="mere")
not_finite_number_of_args(1, 2, 3, name="Medi", verb="are", substantiv="mere")
print("#-----" * 10 + "#")

# Exceptionalele exceptii
# while True:
#     my_var = input("Introduceti un numar intreg:")
#     try:
#         my_int = int(my_var)
#         # print(mi_int)
#     except ValueError as e:
#         print("Va rog introduceti un numar intreg! Eroarea: ", e)
#     except NameError as e:
#         print("Ai folosit o variabila nedefinita! Eroarea: ", e)
#     except Exception as e:
#         ...
#     else:
#         print("Nu a intervenit nicio exceptie...")
#     finally:
#         print(f"Eu apar mereu")


def namespace_function():
    global msg
    msg = "Hello Hi!"
    print(msg)


namespace_function()
print(msg)


def first_function():
    def second_function():
        print(f'my_second_function({msg_func_2})')

    msg_func_2 = "Medi"
    second_function()


first_function()


print(f"Imi plac gogosile {'medi' is 'med'} ")













