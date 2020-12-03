def fact(n):
    return 1 if n == 1 else n * fact(n - 1)

# Ca modulul sa se poata executa in terminal
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))