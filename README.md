# Analisador de Afinidade Musical

**Número da Lista**: 4
**Conteúdo da Disciplina**: FGA0124 - PROJETO DE ALGORITMOS - T01  

## Alunos

<div align = "center">
<table>
  <tr>
    <td align="center"><a href="https://github.com/BiancaPatrocinio7"><img style="border-radius: 50%;" src="https://github.com/BiancaPatrocinio7.png" width="190;" alt=""/><br /><sub><b>Bianca Patrocínio</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/leticiatmartins"><img style="border-radius: 50%;" src="https://github.com/leticiatmartins.png" width="190px;" alt=""/><br /><sub><b>Leticia Torres </b></sub></a><br />
  </tr>
</table>

| Matrícula    | Aluno                       |
| ------------ | --------------------------- |
| 22/1008801   | Bianca Patrocínio Castro    |
| 20/2016702   | Leticia Torres Soares Martins |
</div>

## Sobre 
Este projeto tem como objetivo analisar e comparar gostos musicais. Utilizando o paradigma de **Dividir e Conquistar**, o sistema determina a similaridade entre as preferências musicais de um usuário e as de várias personalidades famosas.

O algoritmo central é a **Contagem de Inversões**, que mede o quão "diferente" é a ordem do ranking de gêneros musicais do usuário em relação ao ranking de uma celebridade. Um número menor de inversões indica uma maior afinidade musical. A complexidade do algoritmo implementado é de $O(n \log n)$, garantindo uma análise eficiente.

## Screenshots
*Substitua as imagens abaixo pelos prints do seu projeto em execução.*

<p align="center">
  <i>Tela inicial, apresentando o programa ao usuário.</i><br>
  <img src="caminho/para/seu/screenshot_1.png" alt="Tela inicial do projeto" width="700"/>
</p>
<hr>
<p align="center">
  <i>Exemplo da interação, onde o usuário escolhe a ordem dos seus gêneros preferidos.</i><br>
  <img src="caminho/para/seu/screenshot_2.png" alt="Usuário ranqueando os gêneros musicais" width="700"/>
</p>
<hr>
<p align="center">
  <i>Tela final, exibindo o ranking de celebridades com o gosto musical mais parecido.</i><br>
  <img src="caminho/para/seu/screenshot_3.png" alt="Resultado final da análise" width="700"/>
</p>

## Instalação 
**Linguagem**: Python

## Pré-requisitos

Antes de rodar o projeto, você precisará ter o **Python 3** instalado em seu sistema. Nenhuma biblioteca externa é necessária.

### Instalar Python

#### No Windows:
Baixe o instalador diretamente do [site oficial do Python](https://www.python.org/downloads/) e siga as instruções. **Lembre-se de marcar a opção "Add Python to PATH"** durante a instalação.

#### No macOS:
O Python 3 geralmente já vem instalado. Você pode verificar com o comando `python3 --version`. Caso precise instalar, use o [Homebrew](https://brew.sh/):
```bash
brew install python
