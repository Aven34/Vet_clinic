CREATE TABLE Reception (
    Reception_ID INT PRIMARY KEY,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Phone VARCHAR(20),
    Address VARCHAR(100)
);

CREATE TABLE Chief_Vets (
    Chief_Vet_ID INT PRIMARY KEY,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Specialization VARCHAR(100)
);

CREATE TABLE Veterinarians (
    Vet_ID INT PRIMARY KEY,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Specialization VARCHAR(100)
);

CREATE TABLE Clients (
    Client_ID INT PRIMARY KEY,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Phone VARCHAR(20),
    Address VARCHAR(100)
);

CREATE TABLE Patients (
    Patient_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Animal_Type VARCHAR(50),
    Age INT
);

CREATE TABLE Diagnoses (
    Diagnosis_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Description VARCHAR(200)
);

CREATE TABLE Visits (
    Visit_ID INT PRIMARY KEY,
    Visit_Date DATE,
    Patient_ID INT,
    Vet_ID INT,
    Diagnosis_ID INT,
    FOREIGN KEY (Patient_ID) REFERENCES Patients(Patient_ID),
    FOREIGN KEY (Vet_ID) REFERENCES Veterinarians(Vet_ID),
    FOREIGN KEY (Diagnosis_ID) REFERENCES Diagnoses(Diagnosis_ID)
);

CREATE TABLE Payments (
    Payment_ID INT PRIMARY KEY,
    Amount DECIMAL(10, 2),
    Payment_Date DATE,
    Description VARCHAR(200),
    Client_ID INT,
    FOREIGN KEY (Client_ID) REFERENCES Clients(Client_ID)
);

CREATE TABLE Appointments (
    Appointment_ID INT PRIMARY KEY,
    Appointment_Details VARCHAR(200),
    Visit_ID INT,
    FOREIGN KEY (Visit_ID) REFERENCES Visits(Visit_ID)
);
