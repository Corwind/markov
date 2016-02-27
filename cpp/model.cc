#include <fstream>
#include <iostream>
#include <map>
#include <vector>
#include <boost/archive/text_oarchive.hpp>
#include <boost/archive/text_iarchive.hpp>
#include <boost/serialization/base_object.hpp>
#include <boost/serialization/vector.hpp>
#include <boost/serialization/map.hpp>

#include "option_parser.hh"


class model
{
    template<class Archive>
    void serialize(Archive &ar, const unsigned int version)
    {
      ar & this->chain;
      ar & this->majs;
    }

  private:
    friend class boost::serialization::access;

    std::map<std::string, std::vector<std::string>> *chain;
    std::vector<std::string> tab;
    std::vector<std::string> majs;


    void shift(std::string word)
    {
      if (tab.size() != 0)
        tab[0] = tab[1];
      tab[tab.size()] = word;
    }
    
    std::string prefix()
    {
      if (tab.size() == 1)
        return tab[0];
      return tab[0] + " " + tab[1];
    }

  public:
    model()
    {
      chain = new std::map<std::string, std::vector<std::string>>();
      tab.reserve(2);
    }
    
    ~model() {}

    std::vector<std::string> readfile(std::string filename)
    {
      std::ifstream ifs;
      ifs.open(filename);
      std::vector<std::string> f;
      std::string line;
      std::string w;
      while (getline(ifs, line))
      {
        size_t pos = 0;
        size_t next = 0;
        while (next != std::string::npos)
        {
          next = line.find(' ', pos);
          w = line.substr(pos, (next == std::string::npos) ?
          std::string::npos : next - pos);
          pos = next + 1;
          f.push_back(w);
          //std::cout << w << std::endl;
        }
      }
      return f;
    }
  
    void generate(std::string filename)
    {
      std::vector<char> *punc = new std::vector<char>({'.', '?', '!'});
      auto f = readfile(filename);
      for (auto it = f.begin(); it != f.end(); it++)
      {
        this->shift(*it);
        auto pref = this->prefix();

        if (it + 1 == f.end())
          break;

        auto next = *(it + 1);

        if (std::find(punc->begin(), punc->end(), pref.at(pref.size() - 1))
            != punc->end())
        {
          this->majs.push_back(next);
          tab.clear();
        }

        auto t = this->chain->find(pref);
        if (t == this->chain->end())
        {
          std::vector<std::string> *v = new std::vector<std::string>({next});
          auto p = std::make_pair(pref, *v);
          this->chain->insert(p);
        }
        else
          (*this->chain)[pref].push_back(next);

      }
    }
};

void usage()
{
  using namespace std;
  cout << "Usage:" << endl << "\tmodel -i input -s save" << endl;
  exit(EXIT_FAILURE);
}

int main(int argc, char *argv[])
{
  model *m = new model();
  if (optionExist(argv, argv + argc, "-h") or argc != 5)
    usage();
  char *input = getOption(argv, argv + argc, "-i");
  char *output = getOption(argv, argv + argc, "-s");
  m->generate(input);
  {
    std::ofstream ofs;
    ofs.open(output);
    boost::archive::text_oarchive oa(ofs);
    oa << m;
  }
  return 0;
}
