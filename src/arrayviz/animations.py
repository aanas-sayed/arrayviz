from manim import *
from typing import Callable, Optional


class ArrayBlockVisualizer(Scene):
    """
    A class to visualise the execution of a user-provided function involving arrays.

    Attributes:
        func (callable): The user-provided function to animate.
        func_args (tuple): Arguments to pass to the user-provided function.
        delay (float): The delay time between frames in seconds. Default is 1.
        frames (list): A list to store the recorded frames during function execution.
    """

    def __init__(
        self,
        func: Callable,
        func_args,
        delay: float = 1.0,
        **kwargs,
    ):
        """
        Initializes the FunctionAnimation class with a function, its arguments, and additional kwargs.
        """
        self.func = func
        self.func_args = func_args
        self.delay = delay
        self.frames = []
        self.array_count = None
        super().__init__(**kwargs)

    def construct(self):
        """
        Constructs the animation by running the user-provided function and recording frames.

        This method overrides the construct method of the Scene class.
        """
        # Run the function with the frame recording callback
        self.func(*self.func_args, self.record_frame)

        # Animate each recorded frame
        for frame_index in range(len(self.frames)):
            self.show_frame(frame_index)

    def record_frame(
        self, arrays: Optional[list[list]] = None, pointers: Optional[list[dict]] = None
    ):
        """
        Records the state of arrays and pointers at each step of the function execution.

        Args:
            arrays (list): The list of arrays representing the function's data state.
            pointers (list): The list of pointers indicating specific positions in the arrays.
        """
        # Set the array count if not set
        if self.array_count is None:
            if arrays is not None:
                self.array_count = len((arrays))
            elif pointers is not None:
                self.array_count = len((pointers))

        # Check if arrays or pointers are of the set length
        if arrays is not None:
            if len(arrays) != self.array_count:
                raise ValueError(
                    f"Length of array is: {len(arrays)}. Expected: {self.array_count}"
                )
        if pointers is not None:
            if len(pointers) != self.array_count:
                raise ValueError(
                    f"Length of pointers is: {len(pointers)}. Expected: {self.array_count}"
                )

        # Set frame based on which combination of arrays and/or pointers has been passed
        # and wether its the first frame or not
        if arrays is not None and pointers is not None:
            self.frames.append((arrays[:], pointers[:]))
        elif self.frames and arrays is not None:
            self.frames.append((arrays[:], self.frames[-1][1][:]))
        elif self.frames and pointers is not None:
            self.frames.append((self.frames[-1][0][:], pointers[:]))
        elif arrays is not None:
            self.frames.append((arrays[:], [{} for _ in range(self.array_count)]))
        elif pointers is not None:
            self.frames.append(([[] for _ in range(self.array_count)], pointers[:]))
        else:
            raise AttributeError("No attribute passed")

    def show_frame(self, frame_index: int):
        """
        Displays a single frame of the animation based on the given arrays and pointers.

        Args:
            arrays (list): The list of arrays representing the function's data state.
            pointers (list): The list of pointers indicating specific positions in the arrays.
        """
        self.clear()

        array_mobjects, pointer_mobjects = self.create_objects(frame_index=frame_index)

        for array_mobject in array_mobjects:
            if frame_index == 0:
                self.play(Create(array_mobject))
            else:
                self.add(array_mobject)

        for pointer_mobject in pointer_mobjects:
            self.add(pointer_mobject)

        self.wait(self.delay)

    def create_objects(self, frame_index: int):
        """
        Creates Manim objects (squares and text) to represent arrays and pointers.

        Args:
            arrays (list): The list of arrays representing the function's data state.
            pointers (list): The list of pointers indicating specific positions in the arrays.

        Returns:
            tuple: Two lists of Manim VGroups, one for array objects and one for pointer objects.
        """
        current_arrays, pointers = self.frames[frame_index]
        if frame_index != 0:
            previous_arrays, _ = self.frames[frame_index - 1]
            updated_indices_for_all_arrays = []
            for current_array, previous_array in zip(current_arrays, previous_arrays):
                updated_indices = []
                for i in range(len(current_array)):
                    if current_array[i] != previous_array[i]:
                        updated_indices.append(i)
                updated_indices_for_all_arrays.append(updated_indices)
        array_groups = []
        pointer_groups = []
        for array_no, array in enumerate(current_arrays):
            array_group = VGroup()
            pointer_group = VGroup()
            y_pos = 1 - 2 * array_no
            x_pos = -len(array) // 2
            for idx, val in enumerate(array):
                rect = Square(side_length=1, color=BLUE if array_no == 0 else RED)
                if frame_index != 0:
                    if idx in updated_indices_for_all_arrays[array_no]:
                        rect.set_fill(PINK, opacity=0.5)
                rect.move_to([x_pos + idx, y_pos, 0])
                text = Text(str(val), font_size=24)
                text.move_to(rect.get_center())
                array_group.add(rect, text)
                for pointer_name, pointer_value in pointers[array_no].items():
                    if idx == pointer_value:
                        pointer_text = Text(pointer_name, font_size=24, color=WHITE)
                        pointer_text.move_to([x_pos + idx, y_pos + 1, 0])
                        pointer_group.add(pointer_text)

            array_groups.append(array_group)
            pointer_groups.append(pointer_group)
        return array_groups, pointer_groups
