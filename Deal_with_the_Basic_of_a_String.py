#정확성 87.5점 나와서 틀림
def solution(s):
    return s.isdigit() and (len(s) == 4 or 6)


#통과함
def solution(s):
    return s.isdigit() and (len(s) == (4 or 6))


#통과함
def solution(s):
    return s.isdigit() and (len(s) == 4 or len(s) == 6)


"""
괄호를 잘 써야 하는구나..!
"""