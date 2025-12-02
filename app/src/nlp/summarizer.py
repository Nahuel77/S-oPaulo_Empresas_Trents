from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from ..config import MODEL_SUMMARY, DEVICE


class Summarizer:
    def __init__(self, model_name=MODEL_SUMMARY, device=DEVICE):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)


def summarize(self, text, max_length=120, min_length=20):
    if not text or len(text.strip())<10:
        return ''
    inputs = self.tokenizer(text, return_tensors='pt', truncation=True, max_length=2048).to(DEVICE)
    out = self.model.generate(**inputs, max_length=max_length, min_length=min_length, num_beams=4)
    return self.tokenizer.decode(out[0], skip_special_tokens=True)