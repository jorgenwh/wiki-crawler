.PHONY: all install uninstall clean

all: install

install:
	pip install -e .

uninstall:
	pip uninstall wikicrawler

clean:
	$(RM) -r *.egg-info build dist
