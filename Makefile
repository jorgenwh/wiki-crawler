.PHONY: all install uninstall clean

all: install

install: clean
	pip install -e .

uninstall: clean
	pip uninstall wikicrawler

clean:
	$(RM) -r *.egg-info build dist
