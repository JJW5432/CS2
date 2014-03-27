"""
Jake Waksbaum
IntroCS2 pd 1
HW#15
2014-03-11
"""
# I'm trying out docstrings and doctests because I read something about them online
# to see my tests run from terminal with -v tag ie "$ python grade.py -v"
def gradeConv(g):
	"""takes a numeric input g, representing a student's grade, and returns its letter grade equivalent
	
	>>> gradeConv(106)
	'A'

	>>> gradeConv(90)
	'A'

	>>> gradeConv(80)
	'B'

	>>> gradeConv(70)
	'C'

	>>> gradeConv(65)
	'D'

	>>> gradeConv(64)
	'F'
	"""
	if g >= 90:
		return "A"
	elif g >= 80:
		return "B"
	elif g >= 70:
		return "C"
	elif g >= 65:
		return "D"
	else:
		return "F"

def gradeConv_fancy(g, grades= {90: "A", 80: "B", 70: "C", 65: "D", "fail": "F"}): 
	"""alternate way that is shorter, more maintainable, and more semantically correct (bc we want to do the same thing to a set of bounds)
	optional argument grades is a dictionary where the keys are the bounds (the lowest grade that can receive the grade) for the letter grades (values), and where the "fail" key has a value of the grade that is given to anything below the lowest bound

	>>> gradeConv_fancy(106)
	'A'

	>>> gradeConv_fancy(90)
	'A'

	>>> gradeConv_fancy(80)
	'B'

	>>> gradeConv_fancy(70)
	'C'

	>>> gradeConv_fancy(65)
	'D'

	>>> gradeConv_fancy(64)
	'F'
	"""
	for bound in sorted(grades, reverse=True): #sort so that highest is checked first VERY IMPORTANT
		if g >= bound:
			return grades[bound] #exits the function so next line is not evaluated
	return grades["fail"] #if we haven't exited the function yet, g is below the lowest bound therefore fail

def passJudgement(grade):
	"""takes a string input letterGrade and prints congratulatory or scolding messages.
	>>> passJudgement("A")
	'YAY'

	>>> passJudgement("B")
	'eh'


	>>> passJudgement("C")
	'eh'


	>>> passJudgement("D")
	'loser'


	>>> passJudgement("F")
	'failure'
	"""
	if grade == "A":
		return "YAY"
	elif grade == "B":
		return "eh"
	elif grade == "C":
		return "eh"
	elif grade == "D":
		return "loser"
	else:
		return "failure"

def passJudgement_fancy(letterGrade):
	"""another better way to implement this function using a dictionary
	judgmenents is a dictionary where the keys are the letter grades and the values are the corresponding comments
		the key can be a string containing multiple letter grades

	>>> passJudgement_fancy("A")
	'YAY'

	>>> passJudgement_fancy("B")
	'eh'


	>>> passJudgement_fancy("C")
	'eh'


	>>> passJudgement_fancy("D")
	'loser'


	>>> passJudgement_fancy("F")
	'failure'
	"""
	judgements = {"A":"YAY", "B C":"eh", "D":"loser"}
	for grade, comment in judgements.items():
		if letterGrade in grade:
			return comment
	return "failure"


if __name__ == "__main__":
	import doctest
	doctest.testmod()
