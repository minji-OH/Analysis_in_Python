"""
1. 전화번호부를 정렬한다
2. (1st-2nd) -> (2nd-3rd) -> (3rd-4th) ... 순으로 비교한다
3. 같은게 하나라도 있으면 False / 모두 다르면 True
"""

def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book[1:], phone_book):
        if p1.startswith(p2):
            return False
        return True
