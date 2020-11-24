#makefile for Zipf stats

example:
	python csvGraph.py example


create:
	python csvGraph.py create


csv:
	python csvGraph.py csv


setup:
	pip install pandas
	pip install NLTK
	pip install matplotlib

