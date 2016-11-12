SRC_DIR=.

all: sloc test flakes lint clone

sloc:
	sloccount --duplicates --wide --details $(SRC_DIR) | fgrep -v .git > sloccount.sc || :

test:
	cd $(SRC_DIR) && nosetests --verbose --with-xunit --xunit-file=../xunit.xml --with-xcoverage --xcoverage-file=../coverage.xml || :

flakes:
	find $(SRC_DIR) -name *.py|egrep -v '^./tests/'|xargs pyflakes  > pyflakes.log || :

lint:
	find $(SRC_DIR) -name *.py|egrep -v '^./tests/' | xargs pylint --output-format=parseable --reports=y > pylint.log || :

clone:
	clonedigger --cpd-output $(SRC_DIR) || :
