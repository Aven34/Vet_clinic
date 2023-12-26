from src.server.data_base import models as database_models
from src.server.data_base import data_models
from src.server.service import *

routers = (
    RouterManager(
        database_model=database_models.Vet,
        pydantic_model=data_models.Vet
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Client,
        pydantic_model=data_models.Client
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Patient,
        pydantic_model=data_models.Patient
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Appointment,
        pydantic_model=data_models.Appointment
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Diagnosis,
        pydantic_model=data_models.Diagnosis
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Payment,
        pydantic_model=data_models.Payment
    ).fastapi_router,
)
