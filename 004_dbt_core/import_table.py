#%% Bibliotecas
import os
import pandas as pd 
from sqlalchemy import create_engine
from getpass import getpass

#%% Variaveis
base = os.getcwd()
path_tables = os.path.join(os.path.dirname(__file__), 'tables')
tables = os.listdir(path_tables)
password = getpass('Database password: ')

#%% Conexao com Banco de Dados
con = create_engine(f'postgresql+psycopg2://postgres:{password}@localhost:5432/postgres')

#%% Upload das tabelas
for table in tables:
    path_table = os.path.join(path_tables, table)
    table_name = os.path.splitext(table)[0]  # Remove a extensão .csvpost

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
