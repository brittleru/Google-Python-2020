def recursive_sum(num):
    if type(num) == int:
        if num <= 0:
            return num
        else:
            return num + recursive_sum((num - 1))

