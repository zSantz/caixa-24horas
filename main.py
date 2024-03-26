# criar um sistema de caixa eletronico
saldo = 100
cheque_especial = 250

while True:
    opcao = int(input('''
Bem vindo ao caixa 24hrs, O que deseja fazer:

[1] Sacar
[2] Depositar
[3] Ver o Saldo
[4] Sair
                      
Digite a sua opção: '''))
# saque
    if opcao == 1:
        saque = int(input('Digite o valor do saque: '))
        if saque == 0: continue
            
        if saque <= saldo and saque >= 0:
            saldo -= saque
            print('Retire o seu Dinheiro.')

        elif (saque <= (cheque_especial + saldo) or (saque <= cheque_especial)) and saque >= 0:
            saldo -= saque
            cheque_especial += saldo
            print('Você utilizou seu Cheque especial, retire o dinheiro.')
 
        else:
            print(f'Você não tem saldo suficiente, seu saldo atual é {saldo+cheque_especial} deposite para sacar.')
# deposito
    if opcao == 2:
        depositar = int(input('Quanto deseja Depositar: '))
        
        if cheque_especial < 250:
            cheque_especial += depositar
            saldo += depositar
        else:
            saldo += depositar

        print(f'Saldo de {depositar} adicionado')
# extrato
    if opcao == 3:
        print(f'''
EXTRATO DA SUA CONTA:

Saldo: {saldo}               
Cheque Especial: {cheque_especial}
''')

# sair
    if opcao == 4:
        break
print('Obrigado por usar nosso sitema!')
