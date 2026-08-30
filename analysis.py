"""
Canada 28 / PC28 drawing data analysis helpers.
Public-domain sample code. Data source referenced in README.
"""
import json, statistics
from collections import Counter


def sum_of_three(a, b, c):
    """Standard Canada28 result is the sum of three 0-9 draws."""
    return a + b + c


def classify(s):
    """Return size/odd-even classification for a sum 0-27."""
    return {
        "size": "big" if s >= 14 else "small",
        "parity": "odd" if s % 2 == 1 else "even",
    }


def analyze_history(sums):
    """Basic frequency / cold-hot / sum distribution summary."""
    freq = Counter(sums)
    total = len(sums) or 1
    return {
        "count": len(sums),
        "mean": round(statistics.mean(sums), 2) if sums else 0,
        "most_common": freq.most_common(5),
        "big_ratio": round(sum(1 for s in sums if s >= 14) / total, 3),
        "odd_ratio": round(sum(1 for s in sums if s % 2 == 1) / total, 3),
    }


if __name__ == "__main__":
    sample = [sum_of_three(5, 8, 2), sum_of_three(0, 9, 6), sum_of_three(7, 3, 7)]
    for s in sample:
        print(s, classify(s))
    print(analyze_history(sample))
