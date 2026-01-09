# 🪙 Coin Flip

Um mini-jogo de **cara ou coroa** feito em Python, com foco em:
- organização de projeto (`src/ layout`)
- orientação a objetos
- testes automatizados com `pytest`

Este projeto foi criado como exercício de estudo e prática.

---

## 📖 Descrição

O jogo simula uma disputa entre dois jogadores em um lançamento de moeda.

A cada rodada:
- um jogador é escolhido aleatoriamente para escolher o lado da moeda
- a moeda é lançada
- quem acertar o lado vence a rodada

🏆 O jogo termina quando um jogador vence **3 rodadas consecutivas**.

---

## 🎮 Como funciona o jogo

1. Dois jogadores informam seus nomes
2. O sistema escolhe aleatoriamente quem começa
3. O jogador escolhe entre `cara` ou `coroa`
4. A moeda é lançada
5. O vencedor da rodada acumula vitórias consecutivas
6. O primeiro a alcançar **3 vitórias seguidas** vence o jogo

---

## 🗂 Estrutura do projeto

```text
CoinFlip/
├─ src/
│  └─ coinflip/
│     ├─ main.py
│     ├─ utils.py
│     └─ classes/
│        ├─ coin.py
│        └─ player.py
│
├─ tests/
│  ├─ test_coin.py
│  ├─ test_player.py
│  └─ test_utils.py
│
├─ pyproject.toml
└─ README.md
```

## ▶️ Como executar
1. Clone o repositório
2. Crie e ative um ambiente virtual
3. Execute o jogo a partir da raiz do projeto

```
python src/coinflip/main.py
```
---

## Testes
Os testes são feitos em `pytest`.
Para rodar todos os testes:
```
pytest
```
Atualmente, o projeto possui testes para:
- lógica da moeda
- comportamento do jogador
- funções utilitárias

---

## 🛠️ Tecnologias utilizadas
- Python 3.13
- Pytest
- Ruff (linting)
- Git & GitHub

---

## 🚀 Proximos passos
Ideias de evolução para o projeto:
- animação da moeda no terminal
- melhoria da interface do jogo
- uso de `Enum` para os lados da moeda
- um arquivo que guarda quem venceu e quando