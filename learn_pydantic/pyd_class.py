from pydantic import BaseModel

class Patient(BaseModel):
    name : str
    age : int

# patient_info = {"name":"nitish","age":30}
patient_info = {"name":"nitish","age":"30"}  #pydantic smart enough convert this string to int


patient1 = Patient(**patient_info)   #since this is dict we have to unpack it using **  