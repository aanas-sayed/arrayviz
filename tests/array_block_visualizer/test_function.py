import pytest
from arrayviz import ArrayBlockVisualizer
from tests.utils.functions import dummy_func


# NOTE: Modifying the same array is modifed and passed inside dummy_func to test deep copy
def test_func_execution():
    visualizer = ArrayBlockVisualizer(func=dummy_func, func_args=(), delay=0.5)

    visualizer.construct()

    assert len(visualizer.frames) == 2
    assert visualizer.frames[0] == ([[1, 2, 3], [4, 5, 6]], [{"i": 0}, {"j": 2}])
    assert visualizer.frames[1] == ([[10, 2, 3], [4, 5, 6]], [{"i": 1}, {"j": 2}])
