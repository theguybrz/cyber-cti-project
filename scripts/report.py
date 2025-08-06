# def generate_report(analysis):
#     # Simula geração de relatório
#     print(f"Gerando relatório de ameaça: {analysis}")

# if __name__ == '__main__':
#     report = "Ameaça Phishing classificada como Alta."
#     generate_report(report)

##################################################################

import os

def generate_report():
    # Diretório base dos arquivos de dados
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')

    # Caminho do arquivo de entrada
    analysis_path = os.path.join(data_dir, 'analysis_result.txt')

    # Tentar ler o arquivo de análise
    try:
        with open(analysis_path, 'r') as file:
            analysis = file.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{analysis_path}' não encontrado.")
        return

    # Gerar relatório
    print("Gerando relatório de ameaça...")
    print(f"Resultado da análise: {analysis}")

    # Caminho do arquivo de saída
    report_path = os.path.join(data_dir, 'final_report.txt')

    # Salvar o relatório final
    with open(report_path, 'w') as file:
        file.write(f"Relatório de Ameaça: {analysis}\n")

    print(f"Relatório gerado com sucesso em '{report_path}'.")

if __name__ == '__main__':
    generate_report()
