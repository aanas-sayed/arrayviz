# ArrayViz

<!-- badges: start -->
| | |
| --- | --- |
| Meta | [![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT) |
| Testing | [![Pylint and Tests](https://github.com/aanas-sayed/arrayviz/actions/workflows/lint_and_test.yaml/badge.svg)](https://github.com/aanas-sayed/arrayviz/actions/workflows/lint_and_test.yaml) [![Release](https://github.com/aanas-sayed/arrayviz/actions/workflows/build_and_release.yaml/badge.svg)](https://github.com/aanas-sayed/arrayviz/actions/workflows/build_and_release.yaml) |

<!-- badges: end -->

This package allows users to pass a function and visualize it as blocks and elements using Manim, a powerful mathematical animation engine. It provides an easy way to animate algorithms step-by-step, helping with educational purposes and debugging.

Note

This project is a work in progress. Package has not been released yet but is planned to be. Only limited functionality is implemented as of now.

## Installation

First, install Manim according to the instructions on [Manim's official website](https://docs.manim.community/en/stable/installation.html).

Install the package via PyPI:

```bash
python -m pip install --upgrade arrayviz
```

## Usage

### ArrayBlockVisualizer Class

The `ArrayBlockVisualizer` class is designed to animate the execution of a user-provided function. Users can control when the pointers should update in relation to the array frame updates (before, at the same time, or after).

#### Parameters

- `func`: The user-provided function to animate.
- `func_args`: Arguments to pass to the user-provided function.
- `delay` (float): The delay time between frames in seconds. Default is 1.
- `**kwargs`: Additional keyword arguments for the `Scene` superclass.

### Example

![merge sorted arrays](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHdkaTQ0dmNxZ2Zzems0dTRmcGgyMjltNDkwMnB4M2c1eDFnM3hqbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/16ka9sdzYT5rACNM6O/giphy.gif)

The following example demonstrates how to use the `ArrayBlockVisualizer` class to animate an example merge function for sorted arrays.

**`examples/merge_sorted_arrays.py`**

```python
from arrayviz import ArrayBlockVisualizer


def merge(nums1, m, nums2, n, record_frame):
    """
    Merges two sorted arrays nums1 and nums2 into a single sorted array in place.

    Args:
        nums1 (list): The first sorted array with extra space at the end to hold nums2 elements.
        m (int): The number of valid elements in nums1.
        nums2 (list): The second sorted array.
        n (int): The number of elements in nums2.
        record_frame (callable): A callback function to record the state of arrays and pointers.
    """
    merged_index = m + n

    # Record initial array
    record_frame(arrays=[nums1[:], nums2[:]])

    while m > 0 and n > 0:
        # Record pointers
        record_frame(pointers=[{"i": m - 1}, {"j": n - 1}])
        if nums1[m - 1] > nums2[n - 1]:
            nums1[merged_index - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[merged_index - 1] = nums2[n - 1]
            n -= 1
        merged_index -= 1

        # Record new array
        record_frame(arrays=[nums1[:], nums2[:]])

    # Record final pointers
    record_frame(pointers=[{"i": n - 1}, {"j": n - 1}])

    nums1[:n] = nums2[:n]

    # Record final array
    record_frame(arrays=[nums1[:], nums2[:]])


# Initial arrays for the merge function
nums1 = [4, 5, 7, 0, 0, 0, 0, 0, 0]
nums2 = [1, 2, 2, 3, 5, 6]
m = 3  # Number of initial valid elements in nums1
n = 6  # Number of elements in nums2


class MergeScene(ArrayBlockVisualizer):
    """
    A Manim scene to visualize the merge function using the FunctionAnimation class.
    """

    def __init__(self, **kwargs):
        """
        Initializes the MergeScene with the merge function and its arguments.

        Args:
            **kwargs: Additional keyword arguments for the ArrayBlockVisualizer superclass.
        """
        super().__init__(merge, (nums1, m, nums2, n), **kwargs)


# To render this scene, use the following command in your terminal:
# manim -pql examples/merge_sorted_arrays.py MergeScene
```

### Running the Example

To render the `MergeScene`, run the following command in your terminal:

```bash
manim -pql example.py MergeScene
```

- `-pql` stands for play in low quality. You can adjust this based on the desired rendering quality.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

[Manim Community](https://github.com/ManimCommunity/manim) for developing the Manim library.
