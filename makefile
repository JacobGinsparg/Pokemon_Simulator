GOOD_PY = $(shell command -v python3 2>&1 >/dev/null && echo python3 || python)

run-python:
	$(GOOD_PY)
