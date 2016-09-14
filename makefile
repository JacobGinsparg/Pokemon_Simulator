PROG = sim
TEST_PROG = tests
CC = g++

PK_SRC = Ability.cpp EffortValue.cpp IndividualValue.cpp Move.cpp Pokemon.cpp Type.cpp
PK_OBJS = $(PK_SRC:.cpp=.o)
PK_FLAGS = -g -I./Pokemon

T_SRC = Tests.cpp
T_OBJS = $(T_SRC:.cpp=.o) $(PK_OBJS)
T_FLAGS = -g -I./Tests

$(TEST_PROG): $(T_SRC)
	$(CC) $(T_FLAGS) -o $(TEST_PROG) $(T_OBJS)

$(PK_OBJS): $(PK_SRC)
	$(CC) $(PK_FLAGS) -c $(PK_OBJS)

clean:
	rm -f $(PROG) $(TEST_PROG)
