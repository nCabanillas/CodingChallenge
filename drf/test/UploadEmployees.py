import requests
import pandas as pd


# La URL de tu endpoint de carga de archivos CSV
url = "http://localhost:8000/api/v1/upload/employees"

# Ruta al archivo CSV que deseas subir
file_path = "hired_employees.csv"
header_names = ['id','name','datetime','department_id','job_id']
df = pd.read_csv(file_path, delimiter=',')

# Configura la solicitud POST
df_dict = df.to_dict(orient='records') # convert to dict

print(df_dict)
# Realiza la solicitud POST
response = requests.post(url, json=df_dict)

# Verifica la respuesta del servidor
if response.status_code == 200:
    print("POST request successful. Response:", response.json())
else:
    print("POST request failed. Status code:", response.status_code)
