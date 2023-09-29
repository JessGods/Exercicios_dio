menu = """

[d] Depositar   
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500
extrato = ''
numeros_saques = 0
LIMITE_SAQUES = 3

while True: 

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Digite o valor do depósito'))

        if valor > 0: 
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operação falhou! O valor informado é inválido. ')
                      
                    
    
    elif opcao == 's':
       valor = float(input("Informe o valor do saque: "))

       excedeu_saldo = valor > saldo
       excedeu_limite = valor > limite
       excedeu_saque = numeros_saques >= LIMITE_SAQUES

       if excedeu_saldo:
           print('Operação falhou! Verifique o saldo e tente novamente. ')

       elif excedeu_limite :
           print("Operação falhou! Verifique o limite. ") ;

       elif excedeu_saque:
           print('Operação falhou! Número máximo de saque excedido.');

       elif valor > 0:
           saldo -= valor
           extrato += f'Saque: R$ {valor:.2f}\n'
           numeros_saques += 1

       else: 
           print('Operaçãp falhou! O valor informado é inválido.')

    elif opcao == 'e':
        print('\n=============== EXTRATO ===============')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print("=========================================") 
    
    elif opcao == 'q':
        break

    else: 
        print('Operação inválida, por favor selecione novamente a operaçao desejada. ')