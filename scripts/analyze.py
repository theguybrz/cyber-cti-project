def analyze_data(data):
    # Simula análise de dados
    print(f"Analisando dados de ameaça: {data['threat']}")
    return f"Ameaça {data['threat']} é classificada como {data['level']}."

if __name__ == '__main__':
    sample_data = {'threat': 'Phishing', 'level': 'High'}
    result = analyze_data(sample_data)
    print(result)