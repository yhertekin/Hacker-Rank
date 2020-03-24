def print_formatted(number):
    for i in range(1,number+1):
        w = len(bin(n)[2:])
        print(str(i).rjust(w,' '),oct(i).lstrip("0o").rjust(w,' '),str(hex(i)[2:].upper()).rjust(w,' '),str(bin(i)[2:]).rjust(w,' '),sep=' ')

