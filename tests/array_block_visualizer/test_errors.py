import pytest  # pylint: disable=unused-import
from arrayviz import ArrayBlockVisualizer
from tests.utils import dummy_func


@pytest.mark.parametrize(
    "arrays,pointers,expected_array_count",
    [
        ([[1, 2, 3]], [{"i": 0}], 1),
        (None, [{"i": 0}, {"j": 0}], 2),
        ([[1, 2], [3, 4]], None, 2),
    ],
)
def test_array_count(arrays, pointers, expected_array_count):
    """
    Test the count of arrays recorded by ArrayBlockVisualizer.

    Verifies that the array count recorded by the visualizer matches the expected count
    based on the provided arrays and pointers.
    """
    visualizer = ArrayBlockVisualizer(func=dummy_func, func_args=([],), delay=0.5)

    visualizer.record_frame(arrays=arrays, pointers=pointers)
    assert visualizer.array_count == expected_array_count


@pytest.mark.parametrize(
    "arrays_1,pointers_1,arrays_2,pointers_2",
    [
        ([[1, 2, 3]], [{"i": 0}], [[1, 2, 3], [0]], [{"i": 0}]),
        ([[1, 2, 3]], [{"i": 0}], [[1, 2, 3]], [{"i": 0}, {"j": 0}]),
        (None, [{"i": 0}, {"j": 0}], None, [{"i": 0}]),
        ([[1, 2]], None, [[1, 2], [3, 4]], None),
    ],
)
def test_array_count_mismatch(arrays_1, pointers_1, arrays_2, pointers_2):
    """
    Test mismatched array counts in record_frame method.

    Ensures that a ValueError is raised when attempting to record frames with mismatched
    array counts or pointer counts.
    """
    visualizer = ArrayBlockVisualizer(func=dummy_func, func_args=([],), delay=0.5)

    visualizer.record_frame(arrays=arrays_1, pointers=pointers_1)

    with pytest.raises(ValueError):
        visualizer.record_frame(arrays=arrays_2, pointers=pointers_2)


def test_record_frame_missing_arguments():
    """
    Test the behavior of record_frame with missing arguments.

    Verifies that AttributeError is raised when record_frame is called with missing
    arrays and pointers arguments.
    """
    visualizer = ArrayBlockVisualizer(func=dummy_func, func_args=([],), delay=0.5)

    with pytest.raises(AttributeError):
        visualizer.record_frame(arrays=None, pointers=None)

    visualizer.record_frame(arrays=[[1, 2, 3]], pointers=[{"i": 0}])

    with pytest.raises(AttributeError):
        visualizer.record_frame(arrays=None, pointers=None)
