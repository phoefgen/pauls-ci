SRC_DIR=.

all: sloc test flakes lint clone

sloc:
	figlet   'sloc'
	sloccount --duplicates --wide --details $(SRC_DIR) | fgrep -v .git || :

flakes:
	figlet   ' pyflakes'
	find $(SRC_DIR) -name *.py|egrep -v '^./tests/'|xargs pyflakes || :

lint:
	figlet   'Linter'
	find $(SRC_DIR) -name *.py|egrep -v '^./tests/' | xargs pylint \
																								--rcfile=./test/pylint.conf || :

clone:
	figlet   'clone digger'
	clonedigger --cpd-output $(SRC_DIR) || :

test:
	figlet 0f banner3 'execute nose2 tests'
	cd $(SRC_DIR) && nose2 --verbose  || :
