def grade(g, _grades = {90: "A", 80: "B", 70: "C", 65: "D", "fail": "F"}):
	for bound in sorted(_grades, reverse=True):
		if g >= bound:
			return _grades[bound]
	return _grades["fail"]
