
# 🃏 Blackjack Game (Console Version)

A simple command-line Blackjack game built in **Python**. Play against the computer (dealer) and try to get as close to 21 as possible without going over!

---

## 🚀 How to Run

1. Make sure you have **Python 3** installed.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the game.
4. Run the following command:

```bash
python blackjack.py


## 🎮 How to Play

- The goal is to get a hand value as close to **21** as possible without going over.
- You will play against the **computer (dealer)**.
- At the start, both you and the dealer are dealt two cards.
- You can choose one of the following on your turn:
  - `Hit` – Draw another card.
  - `Stand` – End your turn.
- After you stand, the dealer reveals their cards and draws more if needed.

---

## 🧠 Rules

- Cards 2 through 10 are worth their face value.
- Face cards (J, Q, K) are worth **10**.
- Aces (`A`) are worth **1 or 11**, whichever helps your total more.
- If your hand goes **over 21**, you **bust** and lose.
- The dealer must draw cards until their total is **17 or more**.
- Outcomes:
  - If you bust → **You lose**
  - If dealer busts → **You win**
  - If your total > dealer's → **You win**
  - If your total < dealer's → **You lose**
  - If tied → **It's a draw**


