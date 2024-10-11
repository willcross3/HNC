import matplotlib.pyplot as plt
import numpy as np
import time

def plot_towers(pegs, moves, num_disks):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(-1, 4)
    ax.set_ylim(0, num_disks + 1)
    ax.set_xticks([])
    ax.set_yticks([])

    # Draw pegs
    for i in range(3):
        ax.add_patch(plt.Rectangle((i, 0), 0.1, num_disks + 1, color='black'))

    # Draw disks
    for peg in range(3):
        for disk in pegs[peg]:
            ax.add_patch(plt.Rectangle((peg + 0.1 - disk / (2 * num_disks), disk), disk / num_disks, 0.5, color='cyan'))

    plt.title("Towers of Hanoi")
    plt.pause(0.5)

def move_disk(pegs, from_peg, to_peg):
    disk = pegs[from_peg].pop()
    pegs[to_peg].append(disk)

def hanoi(n, from_peg, to_peg, aux_peg, pegs, moves):
    if n == 1:
        moves.append((from_peg, to_peg))
        move_disk(pegs, from_peg, to_peg)
        plot_towers(pegs, moves, len(pegs[0]) + len(pegs[1]) + len(pegs[2]))
        return
    hanoi(n - 1, from_peg, aux_peg, to_peg, pegs, moves)
    moves.append((from_peg, to_peg))
    move_disk(pegs, from_peg, to_peg)
    plot_towers(pegs, moves, len(pegs[0]) + len(pegs[1]) + len(pegs[2]))
    hanoi(n - 1, aux_peg, to_peg, from_peg, pegs, moves)

def main(num_disks):
    pegs = [list(range(num_disks, 0, -1)), [], []]
    moves = []
    plot_towers(pegs, moves, num_disks)
    hanoi(num_disks, 0, 2, 1, pegs, moves)
    plt.show()

if __name__ == "__main__":
    num_disks = 5  # Change this number for more disks
    main(num_disks)