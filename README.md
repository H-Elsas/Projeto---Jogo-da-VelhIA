# Jogo da VelhIA 🎮🤖

Um jogo da velha desenvolvido em Python usando Pygame, com um modo de jogo contra uma Inteligência Artificial (IA) baseada no algoritmo Minimax.

## 📌 Índice

- [Introdução](#introdução)
- [Recursos](#recursos)
- [Instalação](#instalação)
- [Como Jogar](#como-jogar)
- [Modos de Jogo](#modos-de-jogo)
- [IA e Algoritmo Minimax](#ia-e-algoritmo-minimax)
- [Dependências](#dependências)
- [Contribuição](#contribuição)
- [Licença](#licença)

## 🚀 Introdução

**Jogo da VelhIA** é uma implementação do clássico jogo da velha, onde o jogador pode competir contra outro jogador ou contra uma IA inteligente. A IA utiliza o algoritmo Minimax, permitindo jogadas estratégicas e desafiadoras.

## ⭐ Recursos

✔ Interface gráfica com Pygame  
✔ Modo Jogador vs Jogador ou Jogador vs IA  
✔ IA com níveis de dificuldade:

- **Fácil**: jogadas aleatórias
- **Difícil**: jogadas estratégicas com Minimax  

✔ Indicação de vencedor com linhas visuais  
✔ Reinício rápido da partida  

## 💾 Instalação

1️⃣ Clone este repositório:

```sh
git clone https://github.com/seu-usuario/jogo-da-velhia.git
cd jogo-da-velhia
```

2️⃣ Instale as dependências:

```sh
pip install -r requirements.txt
```

3️⃣ Execute o jogo:

```sh
python jogo_da_velhia.py
```

## 🎮 Como Jogar

- O jogo inicia no modo IA por padrão
- Clique em uma célula vazia para fazer sua jogada
- O jogador 1 (**X**) sempre começa
- Pressione **M** para alternar entre modo PvP e IA
- Pressione **R** para reiniciar o jogo
- Pressione **0** para definir a IA no modo fácil
- Pressione **1** para definir a IA no modo difícil

## 🔄 Modos de Jogo

| Modo | Descrição |
|------|-------------|
| **PvP** | Dois jogadores alternam as jogadas |
| **IA** | O jogador humano joga contra a IA |

## 🧠 IA e Algoritmo Minimax

A IA do jogo pode operar em dois níveis:

- **Modo Fácil**: joga aleatoriamente
- **Modo Difícil**: usa o **Minimax**, um algoritmo de tomada de decisão baseado na busca pelo melhor movimento possível

- **Mas afinal, como o algoritmo Minimax funciona?**
No código, especificamente a partir da linha 118, podemos ver o funcionamento do algoritmo. Ele prevê todas as jogadas possíveis do jogador
e todas as jogadas possíveis que a própria máquina pode realizar para contestação. Dentro da função Minimax, percebemos que a máquina compreende
que ao jogador ganhar, retorna um valor +1 (maximizando) onde o jogador ganha, e um valor -1 (minimizando) onde a IA ganha. A máquina percorre
uma árvore de decisões simulando todas as jogadas dela e do jogador, e escolhe a que irá minimizar o resultado final da partida, nesse caso
retornando o valor (-1), logicamente o valor que representa sua vitória. Empates também minimizam o resultado, pois a máquina possui uma variável
interna que representa um infinito positivo e ao empatar, essa variável é zerada.

## 🤔 Curiosidades!

São um total de: $3^9 = 19.683$ possibilidades em um tabuleiro de jogo da velha! O minimax não irá considerar todas as possibilidades,
otimizando assim, todas as jogadas.


## 📦 Dependências

O jogo utiliza as seguintes bibliotecas:

- `pygame`
- `numpy`

Instale-as com comando no 3º index logo acima.

## ❓ Por que do projeto?

Esse projeto teve como objetivo treinar conceitos de lógica de programação e inteligência artificial. O projeto foi bem desafiador
e me proporcionou um bom entendimento das libraries usadas, bem como também, conceitos matemáticos e lógicos.

## 📷 Screenshots

![image](https://github.com/user-attachments/assets/25636075-4f83-44e3-817f-ced3439d564a)

![image](https://github.com/user-attachments/assets/402de69d-0e09-4f18-bf19-58568003f332)

![image](https://github.com/user-attachments/assets/1f614f07-e982-4471-a5ee-ee12a3370c57)

## 👨‍💻 Contribuição

Sinta-se à vontade para contribuir! Se encontrar bugs ou tiver sugestões, abra uma issue ou faça um pull request.

## 📜 Licença

Este projeto está sob a licença MIT. Para mais detalhes, consulte o arquivo `LICENSE`.
