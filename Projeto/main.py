from data import GOSTOS_FAMOSOS
from comparador import comparar
from utils import obter_ranking_usuario

def main():
    user_rank = obter_ranking_usuario()

    print("\nSeu ranking:")
    for i, g in enumerate(user_rank):
        print(f"{i+1}. {g}")

    print("\nCalculando similaridade musical...")
    ranking = comparar(user_rank, GOSTOS_FAMOSOS)

    print("\nResultado final:")
    for i, res in enumerate(ranking):
        print(f"{i+1}º: {res['nome']} (Diferença: {res['inversoes']})")

if __name__ == "__main__":
    main()