def solution(phone_book):
    phone_book.sort()
    
    print(help(str.startswith))
    
    for p1,p2 in zip(phone_book,phone_book[1:]):
        if p2.startswith(p1):
            return False
        
    return True