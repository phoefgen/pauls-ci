SRC_DIR=.

all: sloc test flakes lint clone

sloc:
	sloccount --duplicates --wide --details $(SRC_DIR) | fgrep -v .git || :

test:
	cd $(SRC_DIR) && nose2 --verbose  || :

flakes:
	find $(SRC_DIR) -name *.py|egrep -v '^./tests/'|xargs pyflakes || :

lint:
	find $(SRC_DIR) -name *.py|egrep -v '^./tests/' | xargs pylint --output-format=parseable --reports=y  || :

clone:
	clonedigger --cpd-output $(SRC_DIR) || :
