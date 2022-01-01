import os

from fairseq.models.transformer import TransformerModel
from langdetect import detect
from pinject import inject
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

AI_MODELS_PATH = os.path.abspath(os.path.join(os.getcwd(), "ai_models"))


class AIController:
    en_es_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_es')
    en_fr_model = TransformerModel.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_fr', checkpoint_file='model.pt', source_lang='en', target_lang='fr')
    es_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_es_en')
    fr_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_fr_en')
    en_zu_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_zu')
    zu_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_zu_en')
    id_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_id_en')
    en_id_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_id')
    en_nl_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_nl')
    nl_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_nl_en')
    it_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_it_en')
    en_it_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_it')
    ja_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_ja_en')
    en_ja_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_ja')
    en_ru_model = TransformerModel.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_ru', checkpoint_file='en_ru.pt', source_lang='en', target_lang='ru')
    ru_en_model = TransformerModel.from_pretrained(f'{AI_MODELS_PATH}/tmn_ru_en', checkpoint_file='ru_en.pt', source_lang='ru', target_lang='en')
    pt_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_pt_en')
    en_pt_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_pt')

    @inject()
    def __init__(self):
        self.ai_strategies = {
            "translate.en_es": self.translate_en_es,
            "translate.es_en": self.translate_es_en,
            "translate.en_fr": self.translate_en_fr,
            "translate.fr_en": self.translate_fr_en,
            "translate.zu_en": self.translate_zu_en,
            "translate.en_zu": self.translate_en_zu,
            "translate.en_id": self.translate_en_id,
            "translate.id_en": self.translate_id_en,
            "translate.nl_en": self.translate_nl_en,
            "translate.en_nl": self.translate_en_nl,
            "translate.it_en": self.translate_it_en,
            "translate.en_it": self.translate_en_it,
            "translate.ja_en": self.translate_ja_en,
            "translate.en_ja": self.translate_en_ja,
            "translate.ru_en": self.translate_ru_en,
            "translate.en_ru": self.translate_en_ru,
            "translate.en_pt": self.translate_en_pt,
            "translate.pt_en": self.translate_pt_en,
        }

    def translate_en_es(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_es')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_es_model.generate(input_ids)
        translated_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        return translated_text

    def language_detection(self, input_text):
        lang = detect(input_text)
        return lang

    def translate_en_fr(self, input_text):
        output_text = self.en_fr_model.translate(input_text)
        return output_text

    def translate_es_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_es_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.es_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        return output_text

    def translate_fr_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_fr_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.fr_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        return output_text

    def translate_zu_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_zu_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.zu_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        return output_text

    def translate_en_zu(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_zu')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_zu_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        return output_text

    def translate_en_id(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_id')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_id_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        return output_text

    def translate_id_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_id_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.id_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        return output_text

    def translate_nl_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_nl_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.nl_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        return output_text

    def translate_en_nl(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_nl')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_nl_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        return output_text

    def translate_en_it(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_it')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_it_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        return output_text

    def translate_it_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_it_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.it_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        return output_text

    def translate_ja_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_ja_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.ja_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        return output_text

    def translate_en_ja(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_ja')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_ja_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        return output_text

    def translate_en_ru(self, input_text):
        output_text = self.en_ru_model.translate(input_text)
        return output_text

    def translate_ru_en(self, input_text):
        output_text = self.ru_en_model.translate(input_text)
        return output_text

    def translate_en_pt(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_pt')
        input_ids = tokenizer.encode(('>>por<<'+input_text), return_tensors="pt")
        output_decoded = self.en_pt_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        return output_text

    def translate_pt_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_pt_en')
        input_ids = tokenizer.encode(('>>por<<'+input_text), return_tensors="pt")
        output_decoded = self.pt_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        return output_text
