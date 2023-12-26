from pydantic import BaseModel



class BaseModelModify(BaseModel):
    id: int = 1


class Vet(BaseModelModify):
    name: str
    specialization: str
    created_at: str


class Client(BaseModelModify):
    name: str
    phone: str
    address: str
    created_at: str


class Patient(BaseModelModify):
    name: str
    species: str
    age: int
    client_id: int
    created_at: str


class Appointment(BaseModelModify):
    vet_id: int
    patient_id: int
    date: str
    created_at: str


class Diagnosis(BaseModelModify):
    appointment_id: int
    details: str
    created_at: str


class Payment(BaseModelModify):
    amount: float
    appointment_id: int
    created_at: str
