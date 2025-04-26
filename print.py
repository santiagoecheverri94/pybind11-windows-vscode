def print_list_of_dict(msg: list[dict[str, str]]) -> None:
    for word in msg:
        print(f"{word['value']} ", end="")

    print()


import sys
import os

sys.path.append(os.path.abspath("./build"))
import print_cpp  # type: ignore


def print_list_of_dict_cpp(msg: list[dict[str, str]]) -> None:
    print_cpp.PrintVectorOfUnorderedMap(msg)
