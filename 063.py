#escreva um programa que leia um numero "n" inteiro qualquer
#mostre na tela os "N" primeiros elementos de uma (sequencia fibbonacci).
n = int(input('Qunatos termos você quer  mostra ?'))
t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print(' - Fim!')
