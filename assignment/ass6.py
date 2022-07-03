import time
import random

#함수 선언
def lotto() :
    lotto_list=[]
    for i in range(6):
        num=random.randrange(1,50)
        if num not in lotto_list:
            lotto_list.append(num)
    lotto_list.sort()
    
    return lotto_list
    
#메인 코드
while 1:
    func=input("로또번호 추출을 시작합니까?(y/n) :")
    if func=="y":
        print("번호 추출중...")
        
        for i in range(1,6):
            time.sleep(1)
            print("{}...".format(i))
            
        print("로또 번호는!!\n")
        print("{} 입니다.".format(lotto()))
    else:
        print("로또 추출을 종료합니다.")
        break