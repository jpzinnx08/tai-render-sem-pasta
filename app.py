from flask import Flask 
from flask import request
from classes import Jogador, Time
from classes import Competicao
from classes import Jogador
meu_time = Time("pro bolas")
times=[meu_time]

competicao=[
  Competicao(nome="libertadores"),
  Competicao(nome="brasileirao"),
  Competicao(nome="estadual")
]



jogadores = [
    Jogador(1, "Gabriel Barbosa", "111", "Atacante"),
    Jogador(2, "Pedro", "222", "Atacante"),
    Jogador(3, "Arrascaeta", "333", "Meia"),
    Jogador(4, "Everton Ribeiro", "444", "Meia"),
    Jogador(5, "Cássio", "555", "Goleiro"),
]

app= Flask("meu sitezinho")

@app.route("/teste")
def teste():
    return "rota teste ok"

@app.route("/listar_times", methods=["GET"])
def listar():
  text=""
  for time in times:
     text+=time.nome + ","
  return text

@app.route("/criar_time", methods=["POST"])
def post_Time():

    nome= request.json["nome"]
    times.append(Time(nome))
    return "cadastrado com sucesso "

@app.route("/contratar", methods=["POST"])
def contratar():
    id_jogador = request.json["id"]

    for jogador in jogadores:
        if jogador.id == id_jogador:
            meu_time.adicionar_jogador(jogador)
            jogadores.remove(jogador)
            return "Jogador contratado"

    return "Jogador não encontrado"

@app.route("/demitir", methods=["DELETE"])
def demitir():
    id_jogador = request.json["id"]

    for j in meu_time.elenco:
        if j.id == id_jogador:
            meu_time.elenco.remove(j)
            jogadores.append(j)
            return "Jogador removido"

    return "Jogador não está no time"


@app.route("/inscrever", methods=["POST"])
def inscrever():
    nome_comp = request.json["competicao"]

    for comp in competicao:
        if comp.nome == nome_comp:

            
            if meu_time in comp.times_inscritos:
                return "Time já inscrito"

            comp.times_inscritos.append(meu_time)

        

            return "Time inscrito com sucesso"

    return "Competição não encontrada"   

@app.route("/listar_elenco", methods=["GET"])
def listar_elenco():
    text = ""
    for jogador in meu_time.elenco:
        text += jogador.nome + ","
    return text


@app.route("/listar_jogadores", methods=["GET"])
def listar_jogadores():
    lista = [{"id": j.id, "nome": j.nome, "posicao": j.posicao} for j in jogadores]
    return lista, 200

@app.route("/editar_time", methods=["PUT"])
def editar_time():
    novo_nome = request.json.get("nome")

    if not novo_nome:
        return {"erro": "Nome não enviado"}, 400

    meu_time.nome = novo_nome
    return {"mensagem": "Nome do time atualizado"}, 200

import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)



