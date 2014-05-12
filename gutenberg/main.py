FILE = './story.txt'
#import pytest

def main(file):
	file = open(file, 'r')
	ptext = file.read()
	file.close()
#print text