def print_list_of_dict(msg: list[dict[str, str]]) -> None:
    for word in msg:
        print(f"{word['value']} ", end="")

    print()


"""
TODO: Our goal is to implement a function with signature:

def cpp_print_list_of_dict(msg: list[dict[str, str]]) -> None:

This function should be a single line of python code that calls
the C++ function `PrintVectorOfUnorderedMap(msg)` from
`cpp_print.cpp`.
"""
