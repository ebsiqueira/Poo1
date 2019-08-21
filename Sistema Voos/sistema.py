#Bernardo Gomes Duarte e Eduardo Borges Siqueira
#turma 1208A

from vooComercial import VooComercial
from vooFretado import VooFretado
from reserva import Reserva

class Sistema:
    def __init__(self):
        self.listaDeVoos = []

    def cadastrarVoo(self, novoVoo):
        if(len(self.listaDeVoos) < 3):
            self.listaDeVoos.append(novoVoo)
            return 'Voo cadastrado com sucesso!'
        else:
            return 'Voo não cadastrado, número máximo de voos atingido!'
    
    def cancelarVoo(self, numVoo):
        for voo in self.listaDeVoos:
            if(voo.numVoo == numVoo):
               self.listaDeVoos.remove(voo)
               return 'Voo cancelado com sucesso!'
        
        return 'Não foi possivel cancelar.Nao há voo com esse numero!'
    
    def getVoo(self, numVoo):
        for voo in self.listaDeVoos:
            if(voo.numVoo == numVoo):
               return voo
        return 'null'

                
    def getReserva(self, cpf):
        for voo in self.listaDeVoos:
            if(isinstance(voo, VooComercial)):
                for passageiro in voo.passPrimeiraClasse:
                    if(passageiro.cpf == cpf):
                        return [passageiro, 'Voo Comercial, Primeira Classe', voo]
                for passageiro in voo.passClasseEconomica:
                    if(passageiro.cpf == cpf):
                        return [passageiro, 'Voo Comercial, Classe Economica', voo]
            elif(isinstance(voo, VooFretado)):
                for passageiro in voo.passageiros:
                    if(passageiro.cpf == cpf):
                        return [passageiro, 'Voo Fretado', voo]
            else:
                for solicitante in voo.carga:
                    if(solicitante.cpf == cpf):
                        return [solicitante, 'Voo de transporte', voo]
        return 0

    def removeReserva(self, cpf):
        for voo in self.listaDeVoos:
            if(isinstance(voo, VooComercial)):
                print('Voo Comercial')
                for passageiro in voo.passPrimeiraClasse:
                    if(passageiro.cpf == cpf):
                        voo.removeReserva(passageiro)
                        return 1
                for passageiro in voo.passClasseEconomica:
                    if(passageiro.cpf == cpf):
                        voo.removeReserva(passageiro)
                        return 1
            elif(isinstance(voo, VooFretado)):
                print('Voo Fretado')
                for passageiro in voo.passageiros:
                    if(passageiro.cpf == cpf):
                        voo.removeReserva(passageiro)
                        return 1
            else:
                print('Voo Transporte')
                for solicitante in voo.carga:
                    print(cpf)
                    print(solicitante.cpf)
                    if(solicitante.cpf == cpf):
                        voo.removeReserva(solicitante)
                        return 1
        return 0