
#Calculadora 4 operações básicas em Python

num1 = float(input('Digite um número: '));
print(100 * '=');
num2 = float(input("Digite um outro número: "));
print(100 * '=');
oper = str(input('+ , -, x, / Digite um símbolo para a operação desejada: '))
print(100 * '=');
print("operação digitada é : {}".format(oper));



if(oper == '+'):
    soma = (num1 + num2);
    print(100 * '=');
    print('{} + {} = {}'.format(num1, num2 ,soma));
    print(100 * '=');
if(oper == '-'):
    sub = (num1 - num2);
    print(100 * '=');
    print("{} - {} = {}".format(num1, num2, sub));
    print(100 * '=');
if(oper == 'x'):
    multi = (num1 * num2);
    print(100 * '=');
    print("{} x {} = {}".format(num1, num2, multi));
    print(100 * '=');
if(oper == '/'):
    divi = (num1 / num2);
    print(100 * '=');
    print("{} / {} = {}".format(num1, num2, divi));
    print(100 * '=');
