"""
C : 사용할 수 있는 문자의 개수
w : 한 줄에 들어가는 문자의 개수
L : 한 페이지에 들어가는 줄의 수
P : 한 권에 들어가는 페이지의 수
==> 책 한 권의 문자의 수 = C * L * P  
==> 가능한 책의 수 = C ^ (W * L * P)
"""

import sys

while True:
    C, W, L, P = map(int, input().split())
    
    if C == 0 and W == 0 and L == 0 and P == 0:
        break
    
    total_chars = W * L * P
    
    book_nums = C ** total_chars
    
    print(book_nums)
