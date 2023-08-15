
#calculadora 4 operações básicas em Python

num1 = float(input('Digite um número: '));
num2 = float(input("Diite o outro número: "));
oper = str(input('+ , -, x, / Digite um símbolo para a operação desejada: '))
print("operação digitada é : {}".format(oper));

if(oper == '+'):
    soma = (num1 + num2);
    print('{} + {} = {}'.format(num1, num2 ,soma));
if(oper == '-'):
    sub = (num1 - num2);
    print("{} - {} = {}".format(num1, num2, sub));
if(oper == 'x'):
    multi = (num1 * num2);
    print("{} x {} = {}".format(num1, num2, multi));
if(oper == '/'):
    divi = (num1 / num2);
    print("{} / {} = {}".format(num1, num2, divi));
