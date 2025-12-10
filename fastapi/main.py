from fastapi import FastAPI,Path,HTTPException,Query
import json
from utils import Utils

app = FastAPI()
# def load_json():
#     with open("patients.json","r") as f:
#         data = json.load(f)
#     return data

U = Utils()

@app.get("/")
def hello():
    return {"message":"hello world"}

@app.get("/about")
def about():
    return {"message":"campusx is education platform"}

@app.get("/view")
def view():
    data = U.json_data
    return data

@app.get("/patiend/{patient_id}")      #...means is required(patient_id)
def view_patient(patient_id:str = Path(..., description = "ID of the patient in the DB",example="P001") ):
    data = U.json_data

    if patient_id in data:
        return data[patient_id]
    # return{"error" : "patiend not found"}
    raise HTTPException(status_code = 404,detail = "Patient not found")

@app.get("/sort")
def sort_patients(sort_by:str = Query(..., description = "sort on the basis on height, weight or bmi") , order:str = Query("asc",description = "sort in asc or dec order")):

    valid_field = ["height","weight","bmi"]

    if sort_by not in valid_field:
        raise HTTPException(status_code = 400,detail = f"invalid field select from {valid_field}")

    if order not in ["dec","asc"]:
        raise HTTPException(status_code = 400,detail = "invalid order select between dec and asc" )

    data = U.json_data

    sort_order = True if order == "dec" else False
    sorted_data = sorted(data.values(),key = lambda x:x.get(sort_by , 0) ,reverse = sort_order)
    return sorted_data