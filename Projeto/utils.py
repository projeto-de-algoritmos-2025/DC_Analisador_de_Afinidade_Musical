from data import GENEROS_MUSICAIS

def obter_ranking_usuario():
    print("\nOrdene os gêneros musicais do seu mais amado ao menos querido:")
    generos = GENEROS_MUSICAIS[:]
    ranking = []
    for i in range(len(generos)):
        print(f"\nPosição {i+1}:")
        for idx, g in enumerate(generos):
            print(f"  {idx+1}. {g}")
        while True:
            try:
                escolha = int(input("Sua escolha: ")) - 1
                if 0 <= escolha < len(generos):
                    ranking.append(generos.pop(escolha))
                    break
                else:
                    print("Número inválido")
            except ValueError:
                print("Digite um número válido")
    return ranking