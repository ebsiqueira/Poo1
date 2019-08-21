#Bernardo Gomes Duarte e Eduardo Borges Siqueira
#turma 1208A

from voo import Voo

class VooComercial:
    def __init__(self, origem, destino, numVoo, equipeBordo, capacidadeMax):
        Voo.__init__(self, origem, destino, numVoo, equipeBordo)
        self.passClasseEconomica = []
        self.passPrimeiraClasse = []
        self.capMaxPrimeiraClasse = int(capacidadeMax*0.2)
        self.capMaxClasseEconomica = int(capacidadeMax*0.8)

    def adicionarReserva(self, reserva):
        if(reserva.tipoDePassageiro == 'Classe econômica'):
            if (len(self.passClasseEconomica) < self.capMaxClasseEconomica):
                self.passClasseEconomica.append(reserva)
                return ['Reserva na classe econômica realizada com sucesso!', 0]
            elif(len(self.passPrimeiraClasse) < self.capMaxPrimeiraClasse):
                self.passPrimeiraClasse.append(reserva)
                return ['Classe economica lotada, deseja realizar a reserva na primeira classe(S/N)?', 1]
            else:
                return ['Não foi possivel realizar a reserva. Voo lotado!', 0]
        elif(reserva.tipoDePassageiro == 'Primeira classe'):
            if (len(self.passPrimeiraClasse) < self.capMaxPrimeiraClasse):
                self.passPrimeiraClasse.append(reserva)
                return ['Reserva realizada com sucesso!', 0]
            elif(len(self.passClasseEconomica) < self.capMaxClasseEconomica):
                self.passClasseEconomica.append(reserva)
                return ['Primeira classe lotada, deseja realizar a reserva na classe economica?(S/N)', 1]
            else:
                return ['Não foi possivel realizar a reserva. Voo lotado!', 0]

    def removeReserva(self, reserva):
        for passageiro in self.passClasseEconomica:
            if(passageiro == reserva):
                self.passClasseEconomica.remove(reserva)
        for passageiro in self.passPrimeiraClasse:
            if(passageiro == reserva):
                self.passPrimeiraClasse.remove(reserva)