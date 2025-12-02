import pandas as pd


def normalize_receita_csv(path):
    df = pd.read_csv(path, dtype=str)
    df.columns = [c.strip().lower() for c in df.columns]
    # columnas esperadas: razao_social, cnpj, data_abertura, cnae, municipio, tipo
    df['data_abertura'] = pd.to_datetime(df['data_abertura'], errors='coerce')
    df['cnae'] = df['cnae'].str.replace('[^0-9]','', regex=True).str.slice(0,6)

    return df