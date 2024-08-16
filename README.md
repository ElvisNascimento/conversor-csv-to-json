# CSV to JSON Converter

Este projeto é um conversor simples de arquivos CSV para JSON, desenvolvido em Python, com uma interface web criada utilizando Streamlit. O projeto também é Dockerizado para fácil implementação e execução.

## Requisitos

- Python 3.12+ (para execução local)
- Docker (para execução em container)

## Como Usar

### 1. Executar Localmente

#### Instalação de Dependências

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:
    - No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Execute o Streamlit:
    ```bash
    streamlit run csv_to_json/script.py
    ```

6. Acesse a interface web no navegador em `http://localhost:8501`.

### 2. Executar Usando Docker

#### Build da Imagem

1. Crie a imagem Docker:
    ```bash
    docker build -t csv-to-json .
    ```

#### Executar o Container

2. Execute o container:
    ```bash
    docker run --rm -p 8501:8501 csv-to-json
    ```

3. Acesse a interface web no navegador em `http://localhost:8501`.

### 3. Estrutura do Projeto

- `csv_to_json/`: Contém o script Python principal.
- `data/`: Diretório onde o arquivo CSV de entrada deve estar localizado.
- `output_files/`: Diretório onde o arquivo JSON de saída será salvo.
- `Dockerfile`: Arquivo de configuração para criar a imagem Docker.
- `requirements.txt`: Lista de dependências Python necessárias para o projeto.

### 4. Personalização

Se você deseja alterar o arquivo CSV de entrada ou o diretório de saída, modifique os seguintes parâmetros no arquivo `script.py`:

```python
csv_file = '../data/netflix_titles.csv'
output_dir = '../output_files'
