import pytest
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
    visualizer = ArrayBlockVisualizer(func=dummy_func, func_args=([],), delay=0.5)

    visualizer.record_frame(arrays=arrays_1, pointers=pointers_1)

    with pytest.raises(ValueError) as e:
        visualizer.record_frame(arrays=arrays_2, pointers=pointers_2)


def test_record_frame_missing_arguments():
    visualizer = ArrayBlockVisualizer(func=dummy_func, func_args=([],), delay=0.5)

    with pytest.raises(AttributeError) as e:
        visualizer.record_frame(arrays=None, pointers=None)

    visualizer.record_frame(arrays=[[1, 2, 3]], pointers=[{"i": 0}])

    with pytest.raises(AttributeError) as e:
        visualizer.record_frame(arrays=None, pointers=None)
