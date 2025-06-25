# data.py
GENEROS_MUSICAIS = [
    "MPB", "Rock", "K-pop", "Funk", "Pop", "Indie",
    "Sertanejo", "Pagode", "Rap/Hip-Hop", "Música Clássica"
]

GOSTOS_FAMOSOS = {
    "Anitta": [
        "Funk", "Pop", "Rap/Hip-Hop", "Reggaeton", "Sertanejo",
        "Trap", "Afrobeat", "MPB", "Rock", "K-pop"
    ],
    "Lázaro Ramos": [
        "MPB", "Samba", "Rap/Hip-Hop", "Axé", "Pagode",
        "Funk", "Pop", "Música Clássica", "Rock", "Reggae"
    ],
    "Fernanda Montenegro": [
        "Música Clássica", "MPB", "Ópera", "Jazz", "Fado",
        "Choro", "Bolero", "Rock", "Samba", "Pop"
    ],
    "Chico Buarque": [
        "MPB", "Samba", "Choro", "Música Clássica", "Jazz",
        "Bossa Nova", "Fado", "Rock", "Pop", "Rap/Hip-Hop"
    ],
    "Tyler, The Creator": [
        "Rap/Hip-Hop", "Indie", "R&B", "Jazz", "Funk",
        "Trap", "Rock", "Lo-fi", "Experimental", "Pop"
    ]
}
# Garantir que todos os gêneros estejam dentro da base
for nome, gostos in GOSTOS_FAMOSOS.items():
    gostos_filtrados = [g for g in gostos if g in GENEROS_MUSICAIS]
    for genero_base in GENEROS_MUSICAIS:
        if genero_base not in gostos_filtrados:
            gostos_filtrados.append(genero_base)
    GOSTOS_FAMOSOS[nome] = gostos_filtrados[:len(GENEROS_MUSICAIS)]