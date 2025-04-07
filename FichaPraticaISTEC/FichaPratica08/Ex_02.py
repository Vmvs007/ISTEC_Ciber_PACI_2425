def numeroMaisPequeno(a, b, c):
    if (a < b and a < c):
        return a

    if (b < a and b < c):
        return b

    if (c < a and c < b):
        return c


# ________________________________________

print(numeroMaisPequeno(10, 5, 33))
