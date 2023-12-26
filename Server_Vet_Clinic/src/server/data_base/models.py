from fastapi import APIRouter
from peewee import CharField, FloatField, IntegerField, ForeignKeyField, SqliteDatabase, Model

db = SqliteDatabase('vet_clinic.db')

class BaseModel(Model):
    class Meta:
        database = db

class Vet(BaseModel):
    name = CharField(default='')
    specialization = CharField(default='')
    created_at = CharField(default='')

class Client(BaseModel):
    name = CharField(default='')
    phone = CharField(default='')
    address = CharField(default='')
    created_at = CharField(default='')

class Patient(BaseModel):
    name = CharField(default='')
    species = CharField(default='')
    age = IntegerField(default=0)
    client = ForeignKeyField(Client, related_name='client_patients', default=1)
    created_at = CharField(default='')

class Appointment(BaseModel):
    vet = ForeignKeyField(Vet, related_name='vet_appointments', default=1)
    patient = ForeignKeyField(Patient, related_name='patient_appointments', default=1)
    date = CharField(default='')
    created_at = CharField(default='')

class Diagnosis(BaseModel):
    appointment = ForeignKeyField(Appointment, related_name='appointment_diagnoses', default=1)
    details = CharField(default='')
    created_at = CharField(default='')

class Payment(BaseModel):
    amount = FloatField(default=0)
    appointment = ForeignKeyField(Appointment, related_name='appointment_payments', default=1)
    created_at = CharField(default='')

db.connect()
db.create_tables([Vet, Client, Patient, Appointment, Diagnosis, Payment])
