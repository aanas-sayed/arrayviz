import pytest  # pylint: disable=unused-import
from arrayviz import ArrayBlockVisualizer
from tests.utils.functions import dummy_func


def test_initialization():
    """
    Test the initialization of ArrayBlockVisualizer.
    """
    visualizer = ArrayBlockVisualizer(func=dummy_func, func_args=([],), delay=0.5)
    assert visualizer.func is dummy_func
    assert visualizer.func_args == ([],)
    assert visualizer.delay == 0.5
    assert not visualizer.frames


def test_record_frame():
    """
    Test the record_frame method of ArrayBlockVisualizer.

    Checks if the record_frame method correctly adds frames with arrays and pointers
    to the visualizer's frames list.
    """
    visualizer = ArrayBlockVisualizer(func=dummy_func, func_args=(), delay=0.5)

    visualizer.record_frame(arrays=[[1, 2, 3]], pointers=[{"i": 0}])
    assert len(visualizer.frames) == 1
    assert visualizer.frames[0] == ([[1, 2, 3]], [{"i": 0}])

    visualizer.record_frame(arrays=[[1, 2, 4]], pointers=None)
    assert len(visualizer.frames) == 2
    assert visualizer.frames[1] == ([[1, 2, 4]], [{"i": 0}])


def test_record_frame_with_pointers_only():
    """
    Test the record_frame method of ArrayBlockVisualizer with pointers only.

    Verifies that the record_frame method correctly adds a frame with updated
    pointers when arrays are not provided.
    """
    visualizer = ArrayBlockVisualizer(func=dummy_func, func_args=([],), delay=0.5)

    visualizer.record_frame(pointers=[{"i": 1}])
    assert len(visualizer.frames) == 1
    assert visualizer.frames[0] == ([[]], [{"i": 1}])
