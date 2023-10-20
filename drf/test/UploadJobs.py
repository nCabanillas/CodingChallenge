import requests
import pandas as pd


# La URL de tu endpoint de carga de archivos CSV
url = "http://localhost:8000/api/v1/upload_jobs"

# Ruta al archivo CSV que deseas subir
file_path = "jobs.csv"

header_names = {
    "Authorization": "Token 826025611234f25d15082dfa3359814239378a88",  # Reemplaza con tu token
    "Content-Disposition": 'attachment; filename="filename.csv"'
}

# Configura la solicitud POST
files = {'file': (file_path, open(file_path, 'rb'))}

# Realiza la solicitud POST
response = requests.post(url,headers=header_names, files=files)

# Verifica la respuesta del servidor
if response.status_code == 200:
    print("POST request successful. Response:", response.json())
else:
    print("POST request failed. Status code:", response.status_code)