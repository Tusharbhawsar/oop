
from pyd_class import patient1,Patient

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("inserted into database")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("updateed into database")


# insert_patient_data(patient1)
# insert_patient_data(patient1)
update_patient_data(patient1)