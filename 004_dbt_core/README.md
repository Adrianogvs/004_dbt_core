# Configuração do Ambiente para dbt

Este guia fornece instruções detalhadas para a configuração do ambiente virtual e a instalação das dependências necessárias para utilizar o dbt (Data Build Tool).

## 1. Criação da Pasta 004_dbt_core
    mkdir 004_dbt_core
## 1.1 Logo após cria a pasta, navegue ate a pasta com o seguinte comando:
    cd .\005_dbt_core\

## 2. Criação do Arquivo import_table.py
    import_table.py

## 2.1. Inserir os seguintes códigos no arquivo import_table.py
#%% Bibliotecas

    import os
    import pandas as pd
    from sqlalchemy import create_engine
    from getpass import getpass

#%% Variáveis

    base = os.getcwd()
    path_tables = os.path.join(os.path.dirname(__file__), 'tables')
    tables = os.listdir(path_tables)
    password = getpass('Database password: ')

#%% Conexão com Banco de Dados

    con = create_engine(f'postgresql+psycopg2://postgres:{password}@localhost:5432/postgres')

#%% Upload das tabelas

    for table in tables:
        path_table = os.path.join(path_tables, table)
        table_name = os.path.splitext(table)[0]  # Remove a extensão .csv
        # Verifica se o arquivo CSV está vazio antes de tentar lê-lo
        if os.path.getsize(path_table) > 0:
            df = pd.read_csv(path_table)
            df.to_sql(
                table_name, con, schema='bronze',
                if_exists='replace', index=False
            )
            print(f'Table {table_name} uploaded!')
        else:
            print(f'Warning: Skipping empty file {table}')

## 3. Criação da Pasta tables
    mkdir tables

## 3.1. Criação do Arquivo CSV com o Nome dados_teste
    tables/dados_teste.csv

## 4. Criação do Arquivo .gitignore
    .gitignore

## 4.1. Inserir os Seguintes Dados no Arquivo .gitignore
    # .gitignore
    __pycache__/
    .venv/
    *.pyc
    *.pyo
    *.pyd
    *.db
    *.sqlite3
    *.log

## 5. Criação do Arquivo requirements.txt
    requirements.txt

## 5.1. Inserir os Seguintes Dados no Arquivo requirements.txt
    requests==2.26.0
    numpy==1.21.4
    Flask==2.0.1

## 6. Criação do Ambiente Virtual python
    python3 -m venv .venv

Certifique-se de que esses passos sejam seguidos sequencialmente para garantir uma configuração adequada do ambiente para o dbt.

## 6.1. Ativação do Ambiente Virtual (Linux/Mac)
    source .venv/bin/activate

## 6.2. Ativação do Ambiente Virtual (Windows)
    .venv\Scripts\activate

## 6.3. Instalação das Bibliotecas Necessárias
    pip install -r requirements.txt

Certifique-se de ativar o ambiente virtual antes de instalar as bibliotecas. Este passo garante que as dependências necessárias, listadas no arquivo requirements.txt, sejam instaladas no ambiente virtual, isolando assim o projeto de outras dependências do sistema.

Ao concluir essas etapas, o ambiente estará configurado com sucesso para utilizar o dbt e suas dependências. Lembre-se de ativar o ambiente virtual sempre que estiver trabalhando no projeto.