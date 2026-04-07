class Jogador:
    def __init__(self, id, nome, cpf, posicao):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.posicao = posicao

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cpf": self.cpf,
            "posicao": self.posicao
        }

    def __str__(self):
        return f"{self.nome} - {self.posicao}"


class Time:
    def __init__(self, nome):
        self.nome = nome
        self.elenco = []

    def adicionar_jogador(self, jogador):
        # evita duplicado
        for j in self.elenco:
            if j.id == jogador.id:
                return False
        self.elenco.append(jogador)
        return True

    def remover_jogador(self, id_jogador):
        for j in self.elenco:
            if j.id == id_jogador:
                self.elenco.remove(j)
                return True
        return False

    def listar_elenco(self):
        return [j.to_dict() for j in self.elenco]


class Competicao:
    def __init__(self, nome):
        self.nome = nome
        self.times_inscritos = []

    def inscrever_time(self, time):
        if time in self.times_inscritos:
            return False
        self.times_inscritos.append(time)
        return True