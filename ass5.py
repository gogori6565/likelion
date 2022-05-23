#함수 선언
def plus(a, b):
    return a+b

def minus(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def na(a,b):
    return a%b

#메인 코드
while 1:
    a,b=input("연산을 진행할 두 숫자를 입력하시오 : ").split()
    c=input("어떠한 연산을 수행할까요? ")

    if c=="+":
        print(plus(int(a),int(b)))
    elif c=="-":
        print(minus(int(a),int(b)))
    elif c=="*":
        print(mul(int(a),int(b)))
    elif c=="/":
        print(div(int(a),int(b)))
    elif c=="%":
        print(na(int(a),int(b)))