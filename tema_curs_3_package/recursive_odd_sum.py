def recursive_odd_sum(num):
    if type(num) == int:
        if num <= 1:
            return num
        else:
            if num % 2 == 1:
                return num + recursive_odd_sum(num - 2)
        return recursive_odd_sum(num - 1)
