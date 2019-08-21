#Bernardo Gomes Duarte e Eduardo Borges Siqueira
#turma 1208A

from sistema import Sistema
from voo import Voo
from vooComercial import VooComercial
from vooFretado import VooFretado
from vooTransporte import VooTransporte
from reserva import Reserva
from equipeDeBordo import EquipeDeBordo
from random import randint

sistema = Sistema()

#Menu de gerenciamento de voos
def gerenciarVoos():
    escolha = -1
    while escolha != 0:
        print('-------------------------------------------------------')
        print('Digite a opcção desejada:')
        print('1.Cadastrar Voo')
        print('2.Cancelar Voo')
        print('0.Retornar ao menu principal')
        print('-------------------------------------------------------')

        escolha = int(input(''))
        #Retorna ao menu principal 
        if(escolha == 0):
           return
        #Cadastro de voo
        elif(escolha == 1):
            origem = input('Digite a origem do voo: ')
            destino = input('Digite a destino do voo: ')
            numVoo = int(input('Digite o numero do voo: '))
            piloto = input('Digite o nome do piloto: ')
            num = int(input('Digite o numero de comissarios de bordo\funcionarios: '))
            listaDeComissarios = []
            for i in range(num):
                listaDeComissarios.append(input('Digite o nome do funcionario {}:'.format(i+1)))
                
            equipeDeBordo = EquipeDeBordo(piloto, listaDeComissarios) 
            tipoDeVoo = int(input('Selecione o tipo de voo: \n1.Comercial\n2.Fretado\n3.Transporte\n'))
            if(tipoDeVoo == 1):
                capacidadeMax = int(input('Digite a quantidade de assentos do voo: '))
                novoVoo = VooComercial(origem, destino, numVoo, equipeDeBordo, capacidadeMax)
            elif(tipoDeVoo == 2):
                capacidadeMax = int(input('Digite a quantidade de assentos do voo: '))
                novoVoo = VooFretado(origem, destino, numVoo, equipeDeBordo, capacidadeMax)
            else:
                cargaMax = int(input('Digite a carga maxima do voo: '))
                novoVoo = VooTransporte(origem, destino, numVoo, equipeDeBordo, cargaMax)
            print(sistema.cadastrarVoo(novoVoo))
        #Cancelamento Voo
        elif(escolha == 2):
            numVoo = int(input('Digite o numero do voo a ser cancelado: '))
            print(sistema.cancelarVoo(numVoo))
        #Opçao invalida
        else:
            print('-------------------------------------------------------')
            print('Digite uma opção válida!')

#Menu de gerenciamento de reservas
def gerenciarReservas():
    escolha = -1
    while escolha != 0:
        print('-------------------------------------------------------')
        print('Digite a opcção desejada:')
        print('1.Reservar')
        print('2.Consultar reserva')
        print('3.Remover reserva')
        print('0. Retornar ao menu principal')
        print('-------------------------------------------------------')
        escolha = int(input(''))
        #Retorna ao menu principal
        if(escolha == 0):
           return
        #Realiza a reserva
        elif(escolha == 1):
            numVoo = int(input('Digite o numero do voo a ser realizado a reserva: '))
            voo = sistema.getVoo(numVoo)
            if(voo == 'null'):
                print('Não há voo com esse numero!')
            elif(isinstance(voo, VooComercial)):
                nome = input('Digite o nome do passageiro: ')
                cpf = int(input('Digite o cpf: '))
                tipoComida = input('Digite o tipo de comida: ')
                carga = 0
                classe = int(input('Selecione a classe: \n1.Primeirca Classe\n2.ClasseEconomica\n'))
                if(classe == 1):
                    classe = 'Primeira classe'
                else:
                    classe = 'Classe econômica'
                novaReserva = Reserva(nome, cpf, tipoComida, carga, classe)
                retorno = voo.adicionarReserva(novaReserva)
                print(retorno[0])
                if(retorno[1] == 1):
                    if(input('') != 'S'):
                        print('Reserva cancelada')
                        sistema.removeReserva(cpf)
                    else:
                        print('Reserva realizada com sucesso!')

            elif(isinstance(voo, VooFretado)):
                nome = input('Digite o nome do passageiro: ')
                cpf = int(input('Digite o cpf: '))
                tipoComida = input('Digite o tipo de comida: ')
                carga = 0
                classe = ''
                novaReserva = Reserva(nome, cpf, tipoComida, carga, classe)
                print(voo.adicionarReserva(novaReserva))
            else:
                nome = input('Digite o nome do solicitante: ')
                cpf = int(input('Digite o cpf: '))
                tipoComida = ''
                carga = int(input('Digite o peso da carga: '))
                classe = ''
                novaReserva = Reserva(nome, cpf, tipoComida, carga, classe)
                print(voo.adicionarReserva(novaReserva))
        #Consulta reserva
        elif(escolha == 2):
            reserva = sistema.getReserva(int(input('Digite o cpf: \n')))
            if(reserva == 0):
                print('Não ha reserva ligada a esse cpf')
            else:
                print('-------------------------------------------------------')
                print('Nome: ', reserva[0].nome)
                print('Cpf: ', reserva[0].cpf)
                if(reserva[1] == 'Voo de transporte'):
                    print('Peso da carga: ', reserva[0].carga)
                    precoTabela = 500
                    preco = precoTabela*(reserva[0].carga/reserva[2].getCargaTotal())
                    print('Preco da reserva: ', preco)  

                elif(reserva[1] == 'Voo Fretado'):
                    print('Tipo de comida: ', reserva[0].tipoDeComida)
                    precoTabela = 500
                    preco = precoTabela
                    preco -= precoTabela*reserva[2].capMax*4
                    distanciaPercorrida = randint(100, 500)
                    preco += 20 * distanciaPercorrida
                    print('Preco da reserva: ', preco)
                else:
                    print('Tipo de comida: ', reserva[0].tipoDeComida)
                    precoTabela = 100
                    preco = precoTabela
                    if(reserva[2].capMaxPrimeiraClasse + reserva[2].capMaxClasseEconomica > 100):
                        preco -= precoTabela*0.15
                    if(reserva[0].tipoDeComida == 'sem gluten' or reserva[0].tipoDeComida == 'vegetariana'):
                        preco += precoTabela*0.15
                    if(reserva[0].tipoDePassageiro == 'Primeira classe'):
                        preco += precoTabela
                    print('Preco da reserva: ', preco)

                print('Tipo de Voo: ', reserva[1])
                print('Numero do Voo: ', reserva[2].numVoo)
                
                
        #Remove uma reserva
        elif(escolha == 3):
            if(sistema.removeReserva(int(input('Digite o cpf ligado a reserva: ')))):
                print('Reserva removida com sucesso')
            else:
                print('Nenhuma reserva ligada a esse cpf')
        #Opção Invalida
        else:
            print('-------------------------------------------------------')
            print('Digite uma opção válida!')

##Menu principal
escolha = -1
while escolha != 0:
    print('-------------------------------------------------------')
    print('Digite a opcção desejada:')
    print('1.Gerenciar Voos')
    print('2.Gerenciar Reservas')
    print('0. Sair')
    print('-------------------------------------------------------')
    escolha = int(input(''))
    #Encerra o sistema
    if(escolha == 0):
        print('Sistema encerrado')
    #Abre o menu de gerenciamento de voos
    elif(escolha == 1):
        gerenciarVoos()
    #Abre o menu de gerenciamento de reservas
    elif(escolha == 2):
        print('')
        gerenciarReservas()
    #Opçao invalida
    else:
        escolha = -1
        print('-------------------------------------------------------')
        print('Digite uma opção válida!')
