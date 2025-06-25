# comparador.py
from algoritmo import contar_inversoes

def comparar(ranking_user, gostos_famosos):
    resultados = []
    for nome, ranking_famoso in gostos_famosos.items():
        mapa = {g: i for i, g in enumerate(ranking_famoso)}
        ranking_convertido = [mapa[g] for g in ranking_user]
        inversoes = contar_inversoes(ranking_convertido)
        resultados.append({"nome": nome, "inversoes": inversoes})
    return sorted(resultados, key=lambda r: r["inversoes"])