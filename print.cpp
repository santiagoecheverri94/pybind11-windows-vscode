#include "print.hpp"

void PrintVectorOfUnorderedMap(std::vector<std::unordered_map<std::string, std::string>> msg)
{
    for (const std::unordered_map<std::string, std::string>& word : msg)
    {
        std::cout << word.at("value") << " ";
    }

    std::cout << std::endl;
}
