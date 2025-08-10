# Astroroids 🚀

![Astroroids Thumbnail](/Astroroids.png)

This is a classic Asteroids-style arcade game built using Python and Pygame.

## How the Game Works

- You control a spaceship (player) that can move and shoot projectiles.
- The main goal is to shoot and destroy asteroids floating around the screen.
- There are **3 types of asteroids** based on size:
  - **Large Asteroids:** When hit, they split into **2 medium asteroids**.
  - **Medium Asteroids:** When hit, they split into **2 small asteroids**.
  - **Small Asteroids:** When hit, they simply get destroyed.
- Asteroids spawn randomly and move across the screen.
- If the player's ship collides with any asteroid, the game ends.
- The game uses sprite groups to manage and update all objects efficiently.

## Gameplay Features

- Smooth movement and rotation of the player’s ship.
- Dynamic splitting of asteroids adds challenge as you clear larger rocks.
- Shots fired from the ship destroy asteroids upon impact.
- Real-time collision detection between shots, asteroids, and the player.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DarkSideDani/Astroroids.git
   cd Astroroids
   ```

2. Create and activate a Python virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   *If you don't have a `requirements.txt` file, just install pygame manually:*

   ```bash
   pip install pygame
   ```

## Usage

Run the game with:

```bash
python main.py
```

Controls:

* **W/S** — Move forward/backward
* **A/D** — Rotate left/right
* **Spacebar** (or your implemented key) — Shoot projectiles (if implemented)