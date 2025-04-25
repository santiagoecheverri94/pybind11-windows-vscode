#include "print.hpp"

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
