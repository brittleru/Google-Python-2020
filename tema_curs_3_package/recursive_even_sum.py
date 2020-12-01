def recursive_even_sum(num):
    if type(num) == int:
        if num <= 0:
            return num
        else:
            if num % 2 == 0:
                return num + recursive_even_sum(num - 2)
        return recursive_even_sum(num - 1)
