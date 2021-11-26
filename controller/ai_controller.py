import os

from fairseq.models.transformer import TransformerModel
from langdetect import detect
from pinject import inject
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

AI_MODELS_PATH = os.path.abspath(os.path.join(os.getcwd(), "ai_models"))


class AIController:
    en_es_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_es')
    en_fr_model = TransformerModel.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_fr', checkpoint_file='model.pt',
                                                   source_lang='en', target_lang='fr')
    es_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_es_en')

    @inject()
    def __init__(self):
        self.ai_strategies = {
            "translate.en_es": self.translate_en_es,
            "translate.es_en": self.translate_es_en,
            "translate.en_fr": self.translate_en_fr,
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
