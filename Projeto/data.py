GENEROS_MUSICAIS = [
    "MPB", "Rock", "K-pop", "Funk", "Pop", "Indie",
    "Sertanejo", "Pagode", "Rap/Hip-Hop", "Música Clássica"
]

GOSTOS_FAMOSOS = {
    "Anitta": ["Funk", "Pop", "Rap/Hip-Hop", "MPB", "Pagode", "Sertanejo", "Rock"],
    "Lázaro Ramos": ["MPB", "Rap/Hip-Hop", "Funk", "Música Clássica", "Rock", "Pop", "Pagode"],
    "Fernanda Montenegro": ["Música Clássica", "MPB", "Pop", "Rock", "Indie", "Pagode", "Funk"],
    "Chico Buarque": ["MPB", "Música Clássica", "Pagode", "Pop", "Rock", "Indie", "Funk"],
    "Seu Jorge": ["MPB", "Funk", "Rock", "Pop", "Pagode", "Rap/Hip-Hop", "Indie"],
    "Wagner Moura": ["Rock", "MPB", "Pop", "Indie", "Rap/Hip-Hop", "Funk", "Pagode"],
    "Taís Araújo": ["MPB", "Pop", "Rap/Hip-Hop", "Pagode", "Funk", "Rock", "Sertanejo"],
    "Gilberto Gil": ["MPB", "Rock", "Funk", "Pop", "Música Clássica", "Rap/Hip-Hop", "Indie"],
    "Caetano Veloso": ["MPB", "Rock", "Pop", "Música Clássica", "Indie", "Funk", "Rap/Hip-Hop"],
    "Emicida": ["Rap/Hip-Hop", "MPB", "Funk", "Pagode", "Rock", "Pop", "Música Clássica"],
    "IZA": ["Pop", "Funk", "Rap/Hip-Hop", "MPB", "Rock", "Pagode", "Indie"],
    "Marisa Monte": ["MPB", "Pop", "Rock", "Música Clássica", "Pagode", "Indie", "Funk"],
    "Ivete Sangalo": ["Pop", "MPB", "Pagode", "Sertanejo", "Funk", "Rock", "Rap/Hip-Hop"],
    "Lulu Santos": ["Rock", "Pop", "Funk", "MPB", "Indie", "Rap/Hip-Hop", "Música Clássica"],
    "Manu Gavassi": ["Pop", "Indie", "Rock", "MPB", "Rap/Hip-Hop", "Funk", "Pagode"],
    "Bruna Marquezine": ["Pop", "Rap/Hip-Hop", "Indie", "MPB", "Funk", "Rock", "Pagode"],
    "Fábio Porchat": ["MPB", "Pop", "Rock", "Pagode", "Funk", "Sertanejo", "Música Clássica"],
    "Paolla Oliveira": ["MPB", "Rock", "Pop", "Funk", "Pagode", "Sertanejo", "Rap/Hip-Hop"],
    "Selton Mello": ["Rock", "MPB", "Indie", "Música Clássica", "Pop", "Rap/Hip-Hop", "Funk"],
    "Pabllo Vittar": ["Pop", "Funk", "Sertanejo", "Pagode", "Rap/Hip-Hop", "Rock", "MPB"],
    "Juliette Freire": ["MPB", "Pop", "Sertanejo", "Pagode", "Funk", "Rock", "Rap/Hip-Hop"],
    "Milton Nascimento": ["MPB", "Música Clássica", "Pop", "Rock", "Indie", "Pagode", "Funk"],
    "Alexandre Nero": ["Rock", "MPB", "Música Clássica", "Indie", "Pop", "Pagode", "Funk"],
    "Tyler, The Creator": ["Rap/Hip-Hop", "Indie", "Funk", "MPB", "Pop", "Rock", "Música Clássica"],
    "Billie Eilish": ["Indie", "Pop", "Rap/Hip-Hop", "Rock", "Funk", "MPB", "Música Clássica"],
    "RM (BTS)": ["Rap/Hip-Hop", "Indie", "Rock", "MPB", "Pop", "Música Clássica", "Funk"],
    "V (BTS)": ["Música Clássica", "MPB", "Funk", "Indie", "Pop", "Rock", "Rap/Hip-Hop"],
    "Jungkook (BTS)": ["Pop", "Funk", "Rock", "Indie", "Rap/Hip-Hop", "K-pop", "Pagode"],
    "SUGA (BTS)": ["Rap/Hip-Hop", "Música Clássica", "Pop", "Rock", "Funk", "Indie", "Pagode"],
    "Jennie (BLACKPINK)": ["Pop", "Rap/Hip-Hop", "Funk", "Indie", "Rock", "Pagode", "MPB"],
    "Rosé (BLACKPINK)": ["Pop", "Indie", "Rock", "MPB", "Funk", "Rap/Hip-Hop", "Pagode"],
    "Lisa (BLACKPINK)": ["Rap/Hip-Hop", "Funk", "Pop", "K-pop", "Rock", "Pagode", "Sertanejo"],
    "Jisoo (BLACKPINK)": ["Pop", "K-pop", "Rock", "MPB", "Pagode", "Indie", "Funk"]
    
}


for nome, gostos in GOSTOS_FAMOSOS.items():
    gostos_filtrados = [g for g in gostos if g in GENEROS_MUSICAIS]
    for genero_base in GENEROS_MUSICAIS:
        if genero_base not in gostos_filtrados:
            gostos_filtrados.append(genero_base)
    GOSTOS_FAMOSOS[nome] = gostos_filtrados[:len(GENEROS_MUSICAIS)]