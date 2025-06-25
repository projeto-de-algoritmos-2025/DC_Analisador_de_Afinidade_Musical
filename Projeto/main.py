# --------------------------------------------------------------------------
# --- PASSO 1: DEFINIÇÃO DOS DADOS
# --------------------------------------------------------------------------

# Lista de gêneros musicais que será a base para a votação
GENEROS_MUSICAIS = [
    "MPB",
    "Rock",
    "K-pop",
    "Funk",
    "Pop",
    "Indie",
    "Sertanejo",
    "Pagode",
    "Rap/Hip-Hop",
    "Música Clássica"
]

# Base de dados com os gostos musicais de pessoas famosas (exemplo fictício)
GOSTOS_FAMOSOS = {
    "Anitta": [
        "Funk", "Pop", "Rap/Hip-Hop", "Pagode", "Sertanejo", "Rock", "MPB", "K-pop", "Indie", "Música Clássica"
    ],
    "Lázaro Ramos": [
        "MPB", "Rap/Hip-Hop", "Funk", "Rock", "Pagode", "Pop", "Indie", "Sertanejo", "K-pop", "Música Clássica"
    ],
    "Fernanda Montenegro": [
        "Música Clássica", "MPB", "Pop", "Rock", "Indie", "Sertanejo", "Pagode", "Funk", "K-pop", "Rap/Hip-Hop"
    ],
    "Chico Buarque": [
        "MPB", "Música Clássica", "Pagode", "Pop", "Rock", "Indie", "Funk", "Rap/Hip-Hop", "Sertanejo", "K-pop"
    ],
    "Tyler, The Creator": [
        "Rap/Hip-Hop", "Indie", "Pop", "Rock", "Funk", "MPB", "Música Clássica", "Sertanejo", "Pagode", "K-pop"
    ]
}

for nome, gostos in GOSTOS_FAMOSOS.items():
    gostos_filtrados = [genero for genero in gostos if genero in GENEROS_MUSICAIS]
    for genero_base in GENEROS_MUSICAIS:
        if genero_base not in gostos_filtrados:
            gostos_filtrados.append(genero_base)
    GOSTOS_FAMOSOS[nome] = gostos_filtrados[:len(GENEROS_MUSICAIS)]


def contar_inversoes(arr):
    """
    Função principal que inicia o processo de contagem de inversões.
    Utiliza uma abordagem de dividir e conquistar (baseada no Merge Sort).
    Complexidade: O(n log n).
    """
    _, total_inversoes = _merge_sort_e_contar(arr)
    return total_inversoes

def _merge_sort_e_contar(arr):
    """
    Função recursiva que ordena a lista e conta as inversões.
    Retorna a lista ordenada e o número de inversões.
    """
    if len(arr) <= 1:
        return arr, 0

    meio = len(arr) // 2

    metade_esquerda, inv_esquerda = _merge_sort_e_contar(arr[:meio])
    metade_direita, inv_direita = _merge_sort_e_contar(arr[meio:])

    arr_juntado, inv_merge = _merge_e_contar(metade_esquerda, metade_direita)

    total_inversoes = inv_esquerda + inv_direita + inv_merge
    return arr_juntado, total_inversoes

def _merge_e_contar(esquerda, direita):
    """
    Junta duas listas ordenadas (sub-rotina do Merge Sort) e conta as 
    inversões que ocorrem entre as duas listas.
    """
    arr_final = []
    inversoes = 0
    i, j = 0, 0 

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            arr_final.append(esquerda[i])
            i += 1
        else:
            arr_final.append(direita[j])
            j += 1
            inversoes += (len(esquerda) - i)

    arr_final.extend(esquerda[i:])
    arr_final.extend(direita[j:])

    return arr_final, inversoes

def obter_ranking_usuario():
    """
    Pede ao usuário para ordenar a lista de gêneros musicais de forma interativa.
    """
    print("Olá! Vamos descobrir com qual famoso seu gosto musical parece.")
    print(f"Por favor, ordene os {len(GENEROS_MUSICAIS)} estilos musicais a seguir, do seu mais preferido (1) ao menos preferido.")
    print("-" * 30)

    generos_para_ordenar = GENEROS_MUSICAIS[:]
    ranking_usuario = []

    for i in range(len(GENEROS_MUSICAIS)):
        print(f"\n--- Escolha para a Posição {i + 1} ---")
        for idx, genero in enumerate(generos_para_ordenar):
            print(f"  {idx + 1}: {genero}")

        while True:
            try:
                escolha_str = input(f"\nDigite o número do seu {i+1}º gênero preferido: ")
                escolha = int(escolha_str)
                if 1 <= escolha <= len(generos_para_ordenar):
                    genero_escolhido = generos_para_ordenar.pop(escolha - 1)
                    ranking_usuario.append(genero_escolhido)
                    print(f"Você escolheu: {genero_escolhido}")
                    break
                else:
                    print(f"Opção inválida. Por favor, digite um número entre 1 e {len(generos_para_ordenar)}.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

    return ranking_usuario

def comparar_gostos(ranking_usuario, gostos_famosos):
    """
    Compara o ranking do usuário com o de cada famoso e calcula a similaridade
    usando o algoritmo de contagem de inversões.
    """
    resultados = []

    for nome, ranking_famoso in gostos_famosos.items():
        mapa_referencia = {genero: i for i, genero in enumerate(ranking_famoso)}

        ranking_numerico_usuario = [mapa_referencia[genero] for genero in ranking_usuario]

        num_inversoes = contar_inversoes(ranking_numerico_usuario)

        resultados.append({"nome": nome, "inversoes": num_inversoes})

    resultados.sort(key=lambda x: x["inversoes"])
    return resultados

def main():
    """
    Função principal que executa o programa.
    """
    meu_ranking = obter_ranking_usuario()
    print("\n" + "="*40)
    print("Seu ranking final de gostos musicais:")
    for i, genero in enumerate(meu_ranking):
        print(f"  {i+1}. {genero}")
    print("="*40 + "\n")

    print("Calculando a similaridade com os gostos dos famosos...")
    ranking_de_similaridade = comparar_gostos(meu_ranking, GOSTOS_FAMOSOS)

    print("\n--- RESULTADO FINAL ---")
    print("Ranking de famosos com gosto musical mais parecido com o seu:")
    print("(Um nível de 'diferença' menor significa maior similaridade)\n")
    for i, resultado in enumerate(ranking_de_similaridade):
        print(f"{i+1}º Lugar: {resultado['nome']} (Nível de diferença: {resultado['inversoes']})")
    print("\n--- FIM DO PROGRAMA ---")


if __name__ == "__main__":
    main()