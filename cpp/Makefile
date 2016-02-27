CC=g++
CXXFLAGS=-std=c++14

SRC=option_parser.cc model.cc
OBJS=$(SRC:.c=.o)

BIN=model

all: ${BIN}

${BIN}: ${OBJS}
	${CC} ${CXXFLAGS} -o $@ $^ -lboost_serialization
