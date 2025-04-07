def parImpar(num):
    if (num % 2 == 0):
        return True
    else:
        return False


def positivoNegativo(num):
    if (num >= 0):
        return True
    else:
        return False


def primo(num):
    for i in range(2, num):
        if (num % i == 0):
            return False

    return True


def perfeito(num):
    somatorioDivisores = 0

    for i in range(1, num):
        if (num % i == 0):
            # Encontramos um divisor
            somatorioDivisores += i

    if (somatorioDivisores == num):
        return True
    else:
        return False
