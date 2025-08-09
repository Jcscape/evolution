"""
evolution-simulator
Copyright (c) 2025 Kelsey Smith
License: GPL-3.0-only
"""

# Minimal scaffold so Codex has a place to write code.
# Tell Codex exactly what to build in the TODO spec below.

from dataclasses import dataclass, field
from typing import List, Tuple
import random

WORLD_SIZE = (50, 50)  # width, height
INITIAL_AGENTS = 100
FOOD_PER_TICK = 120
TICKS_PER_GENERATION = 500
MUTATION_RATE = 0.05

@dataclass
class Genes:
    speed: float = 1.0         # tiles per tick
    vision: int = 3            # tiles
    efficiency: float = 1.0    # energy cost multiplier

@dataclass
class Agent:
    x: int
    y: int
    energy: float
    genes: Genes
    alive: bool = True

@dataclass
class World:
    width: int
    height: int
    agents: List[Agent] = field(default_factory=list)
    food: set = field(default_factory=set)

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

# === TODO: SPEC FOR CODEX =====================================================
# Build a simple evolution simulator with these rules:
# 1) World is a grid. Each tick:
#    - Spawn FOOD_PER_TICK food pellets at random empty cells.
#    - Each agent loses base energy each tick. Moving costs more, scaled by genes.efficiency.
# 2) Behavior:
#    - Agent scans within 'vision' for nearest food. If found, step toward it.
#    - If on a food cell, eat it and gain energy.
#    - If no food seen, wander randomly.
# 3) Reproduction and selection:
#    - After TICKS_PER_GENERATION ticks, create next generation:
#       * Select parents with probability proportional to final energy.
#       * Child genes = parent genes with per-gene mutation at MUTATION_RATE
#         (small Gaussian noise, clamped to reasonable ranges).
#       * Keep population size the same as INITIAL_AGENTS.
#    - Track and print generation stats: mean speed, vision, efficiency, mean energy.
# 4) CLI:
#    - A `run()` function that runs N generations and prints stats.
#    - Optional flag to write CSV `stats.csv` with per-generation metrics.
# 5) Keep it pure Python, no GUI yet.
# 6) Make code clean and testable. Split into functions if helpful.
# =============================================================================

def run(generations: int = 20) -> None:
    """Stub so Codex has an entrypoint to fill in."""
    print("Stub run(). Codex: implement the full simulation per the TODO spec.")

if __name__ == "__main__":
    run()
