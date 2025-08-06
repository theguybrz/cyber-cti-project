import requests
import json
import os
import base64

def collect_data():
    api_key = input("Cole sua chave de API do VirusTotal: ")

    url = 'https://www.virustotal.com/api/v3/urls/'
    url_to_check = 'https://rei.co.ua/'
    encoded_url = base64.urlsafe_b64encode(url_to_check.encode()).decode().strip("=")

    headers = {
        'x-apikey': api_key
    }

    response = requests.get(url + encoded_url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print("Coletando dados...")

        # Caminho para salvar no diretório anterior, na pasta 'data'
        output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'collected_data.json')
        
        # Garantir que a pasta exista
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Dados coletados e salvos em '{output_path}'.")
        return data
    else:
        print(f"Erro na coleta de dados: {response.status_code}")
        return None

if __name__ == '__main__':
    collect_data()
