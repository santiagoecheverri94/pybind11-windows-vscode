from print import print_list_of_dict, print_list_of_dict_cpp
import os


def main():
    py_msg = [
        {"value": "Hello"},
        {"value": "World"},
        {"value": "from"},
        {"value": "ONLY"},
        {"value": "Python"},
    ]

    print_list_of_dict(py_msg)

    py_msg = [
        {"value": "Hello"},
        {"value": "World"},
        {"value": "from"},
        {"value": "Python/C++ interop"},
    ]

    print_list_of_dict_cpp(py_msg)


if __name__ == "__main__":
    if os.environ.get("VSCODE_DEBUG") == "True":
        print(f"Current process ID: {os.getpid()}")
        breakpoint()

    main()
