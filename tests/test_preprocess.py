import numpy as np
import pytest

from src.preprocess import normalize


def test_normalize_basic():
    result = normalize([10, 20, 30])
    expected = np.array([0.0, 0.5, 1.0])

    assert np.allclose(result, expected)


def test_normalize_constant_values():
    result = normalize([5, 5, 5])

    assert np.allclose(result, np.array([0.0, 0.0, 0.0]))


def test_normalize_empty_input():
    with pytest.raises(ValueError, match="values cannot be empty"):
        normalize([])
