# pip install pydantic

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from typing import List, Optional


class Student(BaseModel):
    name : str
    age : int = 24 # default age is 24
    course : Optional[str] = None # for optional None has to be there
    email: EmailStr
    cgpa : float = Field(gt=0, lt = 10, description= 'A decimal value representing the cgpa of the student') # cgpa should be between 0 and 10
    
    
# new_student = {'name': 'Mohit','email': 'abc'} # as email is not correct it waill raise error
# new_student = {'name': 'Mohit','email': 'abc@gmail.com'} # now it will run
# new_student = {'name': 'Mohit','email': 'abc@gmail.com', 'cgpa': 11.2} # will not run as cgpa > 10
new_student = {'name': 'Mohit','email': 'abc@gmail.com', 'cgpa': 5}

student = Student(**new_student)

print(student)
print(type(student))
print(student.age)
print(student.course)


# converting student to json
student_json = student.model_dump_json()
print(student_json)