import sqlite3
import pandas as pd
from datetime import datetime

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

tabelas = cursor.fetchall()

readed = []
for tabela in tabelas:
    readed.append(tabela[0])

conn.close()

#---------------------------
current_date = datetime.now()
today = current_date.strftime('%d/%m/%Y %H:%M:%S')

for i in readed[10:-1]:
  excel_name = i[9:].upper()
  excel_name_tab = i[9:]
  table_name = i
  #print(excel_name, excel_name_tab, table_name)
  df = pd.read_excel('MATERIAL_TABLE.xlsx', excel_name)
  for a in df[excel_name]:
    input_values = f"""
          INSERT INTO {table_name}({excel_name_tab}, created_at, update_at)
          VALUES ('{a}','{today}','{today}');
    """
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute(input_values)
    conn.commit()

print('Mal Feito Feito!')