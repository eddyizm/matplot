last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

subjects.append("computer science")
grades.append(100)
gradebook = (subjects, grades)
subjects.append("visual arts")
grades.append(93)
print(gradebook)

full_gradebook = zip(gradebook, last_semester_gradebook)