from typing import Union,Optional

per:Union[int,float]=float(input("Enter your percentage"))
Grade:Optional[str]=None
if((per>=80) and (per<=100)):
    Grade="A+"
elif((per>=70) and (per<80)):
    Grade="A"
elif((per>=60) and (per<70)):
    Grade="B"
elif((per>=50) and (per<60)):
    Grade="C"
else:
    Grade
print(f"your percentage is {per} and your grade is {Grade}")

percentages_of_student:list[int|float]=[55,66,77,88,54.8]
gradearr:list[str]=[]
for per in percentages_of_student:
    grade:str=""
    if((per>=80) and (per<=100)):
        grade="A+"
    elif((per>=70) and (per<80)):
        grade="A"
    elif((per>=60) and (per<70)):
        grade="B"
    elif((per>=50) and (per<60)):
        grade="C"
    else:
        grade
    gradearr.append(grade)
print(percentages_of_student)
print(gradearr)

#Zip function,it is generator function who needs iteration with the help of "for loop" and "list"

# res=list(zip(percentages_of_student,gradearr))
id=(list(range(len(percentages_of_student))))
print(id)
res=list(zip(id,percentages_of_student,gradearr))
print(res)
# sorted prhna hai kal