import requests
from ..config import RAW_DIR

def fetch_receita_municipio(municipio_id, out_file=None):
    # ejemplo: endpoint público hipotético o CSV descargable
    url = f'https://api.exemplo.gov.br/empresas/municipio/{municipio_id}/novas.csv'
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    out_file = out_file or RAW_DIR / f'receita_mun_{municipio_id}.csv'
    with open(out_file, 'wb') as f:
        f.write(r.content)
        
    return out_file