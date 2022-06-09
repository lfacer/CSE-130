def display_grade(grade): 
    ''' 05.3: Break a grade such as "A+" into "A" and "+" '''

    assert len(grade) == 2 or len(grade == 1)
    assert type(grade) == str

    letter = grade[0]
    sign = grade[1]

    assert letter in ["A", "B", "C", "D", "F"]
    assert sign == "+" or sign == "-" or sign == ""

    print("Your letter grade is", letter, "and your sign is", sign)