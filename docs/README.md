# Cyber CTI Project

## Descrição

Este projeto coleta dados de ameaças cibernéticas de URLs suspeitas usando a **API do VirusTotal**, realiza a análise dos dados coletados e gera relatórios detalhados sobre o risco das URLs. O projeto também cria um dashboard interativo para visualização das análises.

## Estrutura do Projeto

- **`/data`**: Contém os dados brutos, processados e os relatórios gerados.
  - **`collected_data.json`**: Dados coletados da API do VirusTotal.
  - **`analysis_result.txt`**: Resultado da análise da URL.
  - **`final_report.txt`**: Relatório final gerado com a análise.

- **`/scripts`**: Scripts Python para coleta, análise, geração de relatórios e criação do dashboard.
  - **`collect.py`**: Coleta dados da API do VirusTotal.
  - **`analyze.py`**: Analisa os dados coletados e classifica o risco da URL.
  - **`report.py`**: Gera um relatório final com a análise realizada.
  - **`dashboard.py`**: Cria um dashboard interativo utilizando Dash para visualizar as ameaças.

- **`/dashboard`**: Contém o arquivo **`index.html`** gerado pelo **Dash**, que pode ser visualizado no navegador.

- **`.gitignore`**: Arquivos a serem ignorados pelo Git.

- **`LICENSE`**: Licença MIT para o projeto.

- **`requirements.txt`**: Dependências do projeto.

## Como Executar

### 1. Clonar o Repositório

Clone o repositório para a sua máquina local:

```bash
git clone https://github.com/seu-usuario/cyber-cti-project.git
````

### 2. Criar um Ambiente Virtual (Opcional, mas Recomendado)

Para isolar as dependências, crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

* No **Windows**:

  ```bash
  .venv\Scripts\activate
  ```

* No **macOS/Linux**:

  ```bash
  source .venv/bin/activate
  ```

### 3. Instalar as Dependências

Instale as dependências listadas no **`requirements.txt`**:

```bash
pip install -r requirements.txt
```

### 4. Coletar Dados com o `collect.py`

Execute o script **`collect.py`** para coletar dados sobre uma URL do **VirusTotal**. O script pedirá que você insira sua chave de API do VirusTotal.

```bash
python scripts/collect.py
```

Isso criará o arquivo **`collected_data.json`** com os dados coletados.

### 5. Analisar os Dados com o `analyze.py`

Execute o script **`analyze.py`** para analisar os dados coletados e gerar o arquivo **`analysis_result.txt`** com o resultado da análise.

```bash
python scripts/analyze.py
```

### 6. Gerar o Relatório com o `report.py`

Execute o script **`report.py`** para gerar um relatório final sobre a análise da URL. O relatório será salvo em **`final_report.txt`**.

```bash
python scripts/report.py
```

### 7. Criar o Dashboard com o `dashboard.py`

Execute o script **`dashboard.py`** para criar um dashboard interativo que exibe as análises. O arquivo HTML será salvo na pasta **`/dashboard`**.

```bash
python scripts/dashboard.py
```

O servidor **Dash** será iniciado e você poderá acessar o dashboard no navegador através de **`http://127.0.0.1:8050`**. O arquivo **`index.html`** também será gerado na pasta **`/dashboard`**.

### 8. Acessar o Dashboard

Abra o arquivo **`dashboard/index.html`** em seu navegador ou acesse o servidor **Dash** no navegador em **`http://127.0.0.1:8050`**.

## Observações

* **Chave de API**: A chave de API do **VirusTotal** é necessária para a coleta de dados. Você pode obter a chave de API ao criar uma conta no [VirusTotal](https://www.virustotal.com/).
* **Ambiente Virtual**: Usar um ambiente virtual é recomendado para isolar as dependências do seu projeto.
* **Rodando o Dash**: O dashboard será gerado e exibido localmente no **localhost** (127.0.0.1) na porta **8050**.
