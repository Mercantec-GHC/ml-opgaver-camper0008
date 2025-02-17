from datetime import date
import signal
import sys
import math

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


def terminate_program(*_):
    sys.exit(0)


def date_from_str(text: str) -> date:
    [year, month, day] = [int(value) for value in text.split("-")]
    return date(year, month, day)


def year_from_date(stop: str) -> int:
    return int(stop.split("-").pop(0))


def filter_invalid_row(frame: pd.DataFrame) -> pd.DataFrame:
    return frame.dropna(subset=["driver_gender", "violation", "stop_outcome"])


def age_from_series(row: pd.Series) -> int | None:
    if math.isnan(row["driver_age"]):
        if math.isnan(row["driver_age_raw"]):
            return None
        return int(row["stop_year"] - row["driver_age_raw"])
    return int(row["driver_age"])


def main():
    signal.signal(signal.SIGINT, terminate_program)
    signal.signal(signal.SIGTERM, terminate_program)

    stops = pd.read_csv("../data/Police/police.csv")
    stops = stops.dropna(subset=["driver_gender", "violation", "stop_outcome"])
    stops["stop_date"] = stops["stop_date"].map(date_from_str)
    stops["stop_year"] = stops["stop_date"].map(lambda x: x.year)
    stops["stop_month"] = stops["stop_date"].map(lambda x: x.month)
    stops["age"] = stops.apply(age_from_series, axis="columns")
    stops = stops.dropna(subset=["age"])
    groups = stops.groupby(pd.cut(stops["age"], np.arange(10, 110, 10)), observed=True)
    for stops in groups:
        print(stops)


if __name__ == "__main__":
    main()
