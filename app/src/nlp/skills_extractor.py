import re


# ejemplo simple: mapeo CNAE -> skills/sectors heurístico
CNAE_MAP = {'6201':'Tecnologia','5611':'Restaurante'}


def detect_sector_from_cnae(cnae_code):
    return CNAE_MAP.get(str(cnae_code)[:4], 'Outros')


# extractor de keywords desde razao_social ou descricao
KW_REGEX = re.compile(r'\b(data science|software|restaurante|bar|saude)\b', re.I)


def extract_keywords(text):
    if not text: return []
    return list({m.group(0).lower() for m in KW_REGEX.finditer(text)})