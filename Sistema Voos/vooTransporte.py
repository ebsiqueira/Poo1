#Bernardo Gomes Duarte e Eduardo Borges Siqueira
#turma 1208A

from voo import Voo

class VooTransporte(Voo):
    def __init__(self, origem, destino, numVoo, equipeBordo, cargaMax):
        Voo.__init__(self, origem, destino, numVoo, equipeBordo)
        self.cargaMax = cargaMax
        self.carga = []

    def getCargaTotal(self):
        cargaAux = 0
        for cargas in self.carga:
            cargaAux += cargas.carga
        return cargaAux

    def adicionarReserva(self, reserva):
        if(reserva.carga + self.getCargaTotal() <= self.cargaMax):
            self.carga.append(reserva)
            return "Reserva realizada com sucesso!"
        elif(reserva.carga + self.getCargaTotal() > self.cargaMax):
            return "Carga máxima da aeronave atingida. Não foi possível realizar sua reserva."

    def removeReserva(self, reserva):
        self.carga.remove(reserva)
        