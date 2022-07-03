Snum=input()
score=int(input())
grade=""
if score in range(90,100):
    grade="A"
elif score in range(80,89):
    grade="B"
elif score in range(70,79):
    grade="C"
elif score in range(60,69):
    grade="D"
else:
    grade="F"
print("%s의 학점 : %s"%(Snum,grade))