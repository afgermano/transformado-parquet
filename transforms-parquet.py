import pandas as pd
import glob
import os

# Identifica a pasta onde estão os arquivos Excel
pasta = "./arquivos" 

# Encontra todos os .xlsx
arquivos = glob.glob(os.path.join(pasta, "*.xlsx"))

dfs = []
for arquivo in arquivos:
    # Lê todas as abas ou só a primeira
    df = pd.read_excel(arquivo)
    df["arquivo_origem"] = os.path.basename(arquivo)  # coluna opcional para rastrear origem
    dfs.append(df)

# Junta tudo
df_final = pd.concat(dfs, ignore_index=True)

# Salva como Parquet
df_final.to_parquet("extracao_cobli.parquet", index=False)

print(f"Pronto! {len(arquivos)} arquivo(s) combinados → extracao_cobli.parquet")
print(df_final.shape)