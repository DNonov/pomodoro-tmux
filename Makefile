.PHONY: test install

install:
	@echo "Python install"

test:
	@python -m unittest discover

