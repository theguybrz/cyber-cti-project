# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import pandas as pd
# import json
# import plotly.express as px
# import os
# import webbrowser

# # Inicializando o app Dash
# app = dash.Dash(__name__)

# # Função para ler os dados do arquivo JSON
# def load_data():
#     try:
#         with open('collected_data.json', 'r') as file:
#             data = json.load(file)
#         return data
#     except FileNotFoundError:
#         print("Erro: Arquivo 'collected_data.json' não encontrado.")
#         return None

# # Função para criar o layout do dashboard
# def create_dashboard(data):
#     if not data:
#         return html.Div([html.H3("Erro ao carregar dados")])

#     # Convertendo os dados em um DataFrame do pandas para facilitar o uso com o Dash
#     analysis_results = data['data']['attributes']['last_analysis_results']

#     # Inspecionando a estrutura de analysis_results
#     print("Estrutura de 'analysis_results':")
#     print(analysis_results)

#     # Convertendo o resultado da análise em um formato adequado para o gráfico
#     analysis_df = pd.DataFrame.from_dict(analysis_results, orient='index')
#     analysis_df.reset_index(inplace=True)

#     # Inspecionando a estrutura do DataFrame
#     print("Estrutura do DataFrame após conversão:")
#     print(analysis_df.head())

#     # Verificando as colunas existentes no DataFrame
#     if len(analysis_df.columns) == 5:
#         # Caso haja 5 colunas, renomeie corretamente
#         analysis_df.columns = ['Engine', 'Method', 'Category', 'Result', 'Engine Name']
#     else:
#         # Se não houver o número correto de colunas, imprime uma mensagem de erro
#         print("Número inesperado de colunas. Verifique os dados.")

#     # Criando o gráfico de barras com Plotly
#     fig = px.bar(analysis_df, x='Engine', y='Result', color='Category', title="Resultados da Análise do VirusTotal")

#     # Definindo o layout do Dashboard
#     return html.Div(children=[
#         html.H1("Dashboard de Ameaças do VirusTotal"),
#         html.Div([
#             dcc.Graph(
#                 id='analysis-results',
#                 figure=fig
#             ),
#         ]),
#         html.Div([
#             html.P(f"URL analisada: {data['data']['attributes']['url']}"),
#             html.P(f"Total de maliciosos: {data['data']['attributes']['last_analysis_stats']['malicious']}"),
#             html.P(f"Total de suspeitos: {data['data']['attributes']['last_analysis_stats']['suspicious']}"),
#             html.P(f"Total de inofensivos: {data['data']['attributes']['last_analysis_stats']['harmless']}")
#         ]),
#     ])

# # Função para salvar o dashboard em um arquivo HTML
# def save_dashboard():
#     # Caminho da pasta "dashboard" no diretório anterior
#     dashboard_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dashboard')

#     # Cria a pasta "dashboard" se não existir
#     if not os.path.exists(dashboard_path):
#         os.makedirs(dashboard_path)

#     # Gerar o layout e salvar o arquivo HTML
#     app.layout = create_dashboard(load_data())  # Atualizando o layout do dashboard

#     # Rodar o servidor no localhost
#     app.run(debug=False, use_reloader=False, port=8050, host='127.0.0.1')  # Alterado para 127.0.0.1 ou localhost

#     # Após o servidor ser iniciado, salvar o dashboard
#     print(f"Dashboard salvo em: {os.path.join(dashboard_path, 'dashboard.html')}")

#     # Abrir o navegador na URL do Dash
#     webbrowser.open('http://127.0.0.1:8050')  # Agora abre o navegador automaticamente no Dash

# if __name__ == '__main__':
#     save_dashboard()

#############################################################################

import json
import os
import pandas as pd
import plotly.express as px
import plotly.io as pio
import webbrowser

def generate_static_dashboard():
    # Caminho do JSON
    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'collected_data.json')

    # Caminho onde vamos salvar o index.html
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dashboard', 'index.html')

    # Criar a pasta /dashboard se não existir
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Carregar os dados
    try:
        with open(data_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{data_path}' não encontrado.")
        return

    # Transformar em DataFrame
    analysis_results = data['data']['attributes']['last_analysis_results']
    df = pd.DataFrame.from_dict(analysis_results, orient='index')
    df.reset_index(inplace=True)

    if len(df.columns) == 5:
        df.columns = ['Engine', 'Method', 'Category', 'Result', 'Engine Name']
    else:
        print("Número inesperado de colunas. Verifique os dados.")
        return

    # Gerar gráfico
    fig = px.bar(df, x='Engine', y='Result', color='Category', title="Resultados da Análise do VirusTotal")

    # Salvar o gráfico como HTML estático
    pio.write_html(fig, file=output_path, auto_open=True)

    print(f"Dashboard salvo com sucesso em: {output_path}")

if __name__ == '__main__':
    generate_static_dashboard()
