#Bernardo Gomes Duarte e Eduardo Borges Siqueira
#turma 1208A

from voo import Voo

class VooFretado:
    def __init__(self, origem, destino, numVoo, equipeBordo, capMax):
        Voo.__init__(self, origem, destino, numVoo, equipeBordo)
        self.passageiros = []
        self.capMax = capMax

    def adicionarReserva(self, reserva):
        if(len(self.passageiros) < self.capMax):
            self.passageiros.append(reserva)
            return 'Reserva realizada com sucesso!'
        else:
            return 'Não foi possivel realizar a reserva. Voo lotado!'
    
    def removeReserva(self, reserva):
        self.passageiros.remove(reserva)