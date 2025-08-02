import requests

def collect_data():
    # Simula coleta de dados de fontes fictícias
    data = {
        'threat': 'Phishing',
        'level': 'High',
        'source': 'email'
    }
    print("Coletando dados...")
    return data

if __name__ == '__main__':
    collected_data = collect_data()
    print(f"Dados coletados: {collected_data}")