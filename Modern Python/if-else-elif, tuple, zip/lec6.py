from typing import Union,Optional

per:Union[int,float]=float(input("Enter your percentage"))
Grade:Optional[str]=None
if(per>=80):
    Grade="A+"
elif(per>=70):
    Grade="A"
elif(per>=60):
    Grade="B"
elif(per>=50):
    Grade="C"
else:
    Grade
print(f"your percentage is {per} and your grade is {Grade}")