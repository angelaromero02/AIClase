import pickle

import numpy as np
from schemas.diabetes_schemas import PatientData


# Cargamos el modelo de RandomForest

with open('RFDiabetesv132.pkl','rb') as file:
    model = pickle.load(file)
labels=['Sano','Enfermo']
def diabetes_prediction(data: PatientData):
    # Aquí iría la lógica para hacer la predicción usando el modelo entrenado
    xin=np.array([[data.Pregnancies, 
                   data.Glucose, 
                   data.BloodPressure,
                   data.SkinThickness,
                   data.Insulin, 
                   data.BMI,
                   data.DiabetesPedigreeFunction,
                   data.Age]]).reshape(1, 8)


    prediction = model.predict(xin)

    print("predicción:",prediction)
    # Por simplicidad, vamos a devolver una predicción ficticia
    return labels[prediction[0]]
   