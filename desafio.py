def primo(number):
    number = int(number)
    n = 2
    while n <= number:
        if (n/number) == 1 and (n%number) == 0:
            return True
        elif (number%n) == 0:
            return False
        n+=1

def palindromo(number):
    numberReverse = str(number)[len(str(number))::-1]
    if str(number) == numberReverse:
        return True
    return False

#def numbers():
#    for n in range(100000000, 999999999):
#        if palindromo(n) and primo(n)

def formatArq(arq):
    bruto = open(arq, "r")
    pi = bruto.readline()
    return pi

def desafio():
    pi = formatArq('number_pi.txt')
    n = 0
    while (n+9) <= len(pi):
        num = pi[n:(n+9)]
        if palindromo(num):
            if primo(num):
                return print(num, n)
        n+=1

desafio()