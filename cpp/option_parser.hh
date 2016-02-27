#ifndef OPTION_PARSER_HH

#define OPTION_PARSER_HH

  #include <algorithm>
  #include <string>
  char *getOption(char **begin, char **end, const std::string &option);
  bool optionExist(char **begin, char **end, const std::string &option);

#endif
