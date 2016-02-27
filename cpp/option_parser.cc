#include "option_parser.hh"

char *getOption(char **begin, char **end, const std::string &option)
{
  auto itr = std::find(begin, end, option);
  if (itr != end and ++itr != end)
    return *itr;
  return nullptr;
}

bool optionExist(char **begin, char **end, const std::string &option)
{
  return std::find(begin, end, option) != end;
}
