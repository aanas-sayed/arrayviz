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
        # Record [new] pointers
        record_frame(pointers=[{"i": m - 1, "target": merged_index - 1}, {"j": n - 1}])
        if nums1[m - 1] > nums2[n - 1]:
            nums1[merged_index - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[merged_index - 1] = nums2[n - 1]
            n -= 1
        merged_index -= 1

        # Record new array
        record_frame(arrays=[nums1[:], nums2[:]])

    # Record new pointers
    record_frame(pointers=[{"i": n - 1}, {"j": n - 1}])

    nums1[:n] = nums2[:n]

    # Record final array
    record_frame(arrays=[nums1[:], nums2[:]])


# Initial arrays for the merge function
NUMS1 = [4, 5, 7, 0, 0, 0, 0, 0, 0]
NUMS2 = [1, 2, 2, 3, 5, 6]
M = 3  # Number of initial valid elements in nums1
N = 6  # Number of elements in nums2


class MergeScene(ArrayBlockVisualizer):
    """
    A Manim scene to visualize the merge function using the FunctionAnimation class.
    """

    def __init__(self, **kwargs):
        """
        Initializes the MergeScene with the merge function and its arguments.

        Args:
            func (callable): The user-provided function to animate.
            func_args (tuple): Arguments to pass to the user-provided function.
            delay (float): The delay time between frames in seconds. Default is 1.
            **kwargs: Additional keyword arguments for the FunctionAnimation superclass
            (manim.Scene).
        """
        super().__init__(merge, (NUMS1, M, NUMS2, N), **kwargs)


# To render this scene, use the following command in your terminal:
# manim -pql examples/merge_sorted_arrays.py MergeScene
