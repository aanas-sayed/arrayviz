import pytest  # pylint: disable=unused-import
from arrayviz import ArrayBlockVisualizer
from tests.utils.functions import dummy_func


def test_func_execution():
    """
    Test the execution of a function with ArrayBlockVisualizer.

    Verifies that the visualizer correctly constructs frames based on the function execution,
    and checks that the frames list contains the expected states of arrays and pointers.

    Also tests if deep copy is implemented as `dummy_func` modifies arrays by referrence before
    pushing frame.
    """
    visualizer = ArrayBlockVisualizer(func=dummy_func, func_args=(), delay=0.5)

    visualizer.construct()

    assert len(visualizer.frames) == 2
    assert visualizer.frames[0] == ([[1, 2, 3], [4, 5, 6]], [{"i": 0}, {"j": 2}])
    assert visualizer.frames[1] == ([[10, 2, 3], [4, 5, 6]], [{"i": 1}, {"j": 2}])
