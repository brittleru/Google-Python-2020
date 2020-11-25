print(7 is 7)

l = [1, 2, 3]
print(l)

if 1 in l:
    print("found!")
else:
    print("not found")


s = "python"

print('a is no in python', 'y' not in s)

user_name = 'sebastian'
user = 'brittle'

print(id(user_name))
print(id(user))

my_var = 1
# my_var = my_var + 2
my_var *= 2
print(my_var)

user = "seba\\stian"

print(user)

sentance = 'ana\nare\nmere'
print(sentance)

s = """
 Hello world
 Meow meow
 Django when?
 """
print(s)

s = "{} are {} mere".format("Ana", 42)
print(s)


print(F"For only {49:.2f} you will get {s}")


l = [1, 2, 3, 'Anna', [11, 12]]
print(l)
# print(sorted(l))
print(len(l))

my_list = []
for i in range(11):
    my_list.append(i)

print(my_list)
print(my_list[2:])
print(my_list[-2:])
my_list.append(my_list)
print(my_list)


my_list.extend(my_list)
print(my_list)

d = dict()
b = {}
d[1] = '1'
d[2] = 'Gogosi'
print(d)
# f = d
print(d.get(1, 'default'))
f = d.copy()
print(f)

d ={
    1: 'Anna',
    2: 'are',
    3: 'mere'
}

for key, value in d.items():
    print('{} -> {}'.format(key, value))
