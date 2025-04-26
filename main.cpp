#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "print.hpp"

PYBIND11_MODULE(print_cpp, m)
{
    m.doc() = "Python/C++ interoperability example module";

    m.def(
        "PrintVectorOfUnorderedMap",
        &PrintVectorOfUnorderedMap,
        "Prints a Python list[dict[str, str]] binded into a C++ "
        "std::vector<std::unordered_map<std::string, std::string>>"
    );
}

int main()
{
    std::vector<std::unordered_map<std::string, std::string>> cpp_msg{
        {{"value", "Hello"}},
        {{"value", "World"}},
        {{"value", "from"}},
        {{"value", "ONLY"}},
        {{"value", "C++"}}
    };

    PrintVectorOfUnorderedMap(cpp_msg);
}
