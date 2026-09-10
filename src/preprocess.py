"""Small, testable preprocessing helpers."""

import os

import numpy as np


def normalize(values):
    """Min-max normalize a 1D list or array into the range [0, 1]."""
    arr = np.asarray(values, dtype=float)

    if arr.size == 0:
        raise ValueError("values cannot be empty")

    minimum = arr.min()
    maximum = arr.max()

    if minimum == maximum:
        return np.zeros_like(arr)

    return (arr - minimum) / (maximum - minimum)
