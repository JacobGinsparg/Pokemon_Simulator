GOOD_PY = $(shell command -v python3 2>&1 >/dev/null && echo python3 || python)
TEAM_1 = ./pokemon/teams/NewOU.txt
TEAM_2 = ./pokemon/teams/OldSun.txt

cs4850:
	@$(GOOD_PY) ./run_simulator.py $(TEAM_1) $(TEAM_2)

run-python:
	@$(GOOD_PY)

clean:
	@rm -r **/__pycache__
