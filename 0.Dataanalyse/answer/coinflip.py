from enum import Enum
import random
import signal
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def render_flips(data: pd.DataFrame):
    plt.figure(figsize=(10, 6))
    plt.plot(
        data["heads%"],
        marker="o",
        linestyle="-",
        label="heads%",
        color="b",
    )
    plt.title("coin flips distribution")
    plt.xlabel("flips")
    plt.ylabel("% of flips that are heads")
    plt.xticks(range(len(data)))
    plt.ylim([0, 100])
    plt.grid(True)
    plt.legend()
    plt.show()


class Flip(Enum):
    heads = 1
    tails = 2


def coin_flip() -> Flip:
    if random.randint(0, 1) == 0:
        return Flip.tails
    return Flip.heads


def flip_coins(size: int) -> list[tuple[int, int]]:
    flips = []
    for idx in range(size):
        (heads, tails) = (0, 0) if idx == 0 else flips[idx - 1]
        flip = coin_flip()
        if flip == Flip.heads:
            flips.append((heads + 1, tails))
        else:
            flips.append((heads, tails + 1))
    return flips


def terminate_program(*_):
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, terminate_program)
    signal.signal(signal.SIGTERM, terminate_program)

    flips = np.array(flip_coins(10_000))
    columns = np.array(["heads", "tails"])
    dataframe = pd.DataFrame(data=flips, columns=columns)
    dataframe["heads%"] = (
        dataframe["heads"] / (dataframe["heads"] + dataframe["tails"])
    ) * 100
    render_flips(dataframe)


if __name__ == "__main__":
    main()
