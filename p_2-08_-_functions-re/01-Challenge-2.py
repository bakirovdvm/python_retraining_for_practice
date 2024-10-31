def print_num(numb, count=1):
    print(count)
    if count != numb:
        return print_num(numb, count+1)


print_num(10)
