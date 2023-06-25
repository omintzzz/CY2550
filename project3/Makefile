# variables
PYTHON = python
PIP = pip
WORDS_URL = https://github.com/AllenDowney/ThinkPython2/blob/master/code/words.txt

# targets
.PHONY: install run clean

install:
	$(PIP) install -r requirements.txt

wordlist:
    curl -o words.txt $(WORDS_URL)
run:
	$(PYTHON) xkcdpwgen.py

clean:
	rm -rf __pycache__