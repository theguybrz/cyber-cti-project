# def analyze_data(data):
#     # Simula análise de dados
#     print(f"Analisando dados de ameaça: {data['threat']}")
#     return f"Ameaça {data['threat']} é classificada como {data['level']}."

# if __name__ == '__main__':
#     sample_data = {'threat': 'Phishing', 'level': 'High'}
#     result = analyze_data(sample_data)
#     print(result)

#########################################################################

import json
import os

def analyze_data():
    # Caminho para o diretório de dados (um nível acima, na pasta "data")
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
    
    # Caminho completo para o arquivo JSON
    json_path = os.path.join(data_dir, 'collected_data.json')
    
    # Tentar ler os dados coletados
    try:
        with open(json_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{json_path}' não encontrado.")
        return

    # Extrair informações relevantes
    url = data['data']['attributes']['url']
    last_analysis_stats = data['data']['attributes']['last_analysis_stats']
    
    malicious_count = last_analysis_stats['malicious']
    suspicious_count = last_analysis_stats['suspicious']
    harmless_count = last_analysis_stats['harmless']
    
    if malicious_count > 0:
        level = "High"
    elif suspicious_count > 0:
        level = "Medium"
    else:
        level = "Low"
    
    print(f"Analisando dados de ameaça para a URL: {url}")
    print(f"Número de ameaças maliciosas: {malicious_count}")
    print(f"Número de ameaças suspeitas: {suspicious_count}")
    print(f"Número de respostas inofensivas: {harmless_count}")
    
    analysis = f"A URL {url} foi classificada como risco {level}."

    # Caminho completo para salvar o resultado
    analysis_path = os.path.join(data_dir, 'analysis_result.txt')
    
    with open(analysis_path, 'w') as file:
        file.write(analysis)

    print(f"Análise concluída e salva em '{analysis_path}'.")
    return analysis

if __name__ == '__main__':
    analyze_data()
