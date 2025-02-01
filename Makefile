VENV = venv

.PHONY: all setup install run clean


all: setup install

setup:
	python3 -m venv $(VENV)

install:
	$(VENV)/bin/pip install -r requirements.txt


run:
	$(VENV)/bin/python main.py

clean:
	rm -rf $(VENV)


