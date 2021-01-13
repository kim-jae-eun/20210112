def myemail_info(p):
    if '@' in p:
        return tuple(p.split('@'))
    else:
        return None
print(myemail_info('kj6659@naver.com'))
print(myemail_info('naver'))