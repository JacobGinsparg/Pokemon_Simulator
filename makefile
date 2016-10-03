GOOD_PY = $(shell command -v python3 2>&1 >/dev/null && echo python3 || python)

run-python:
	$(GOOD_PY)

data:
	@rm -f ./pokemon/data/*.json
	@$(GOOD_PY) ./pokemon/data/pokemon_crawler.py
