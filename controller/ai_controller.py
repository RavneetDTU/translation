import os

from fairseq.models.transformer import TransformerModel
from langdetect import detect
from pinject import inject
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import FSMTForConditionalGeneration, FSMTTokenizer
import html
import requests

url = 'http://169.255.36.95:5000/translate'

# Libar URL
# Local test
# libra_url = "http://127.0.0.1:5000/translate"

# Production url
libra_url = "http://192.168.0.102:5000/translate"


AI_MODELS_PATH = os.path.abspath(os.path.join(os.getcwd(), "ai_models"))

# Seprator sets:
eng_seprator_set = ['?', '!', '.']


class AIController:
    en_es_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_es')
    en_fr_model = TransformerModel.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_fr_v2', checkpoint_file='en_fr_v2.pt', source_lang='en', target_lang='fr', bpe = 'subword_nmt', bpe_codes = f'{AI_MODELS_PATH}/tmn_en_fr_v2/bpecodes_v2')
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
    en_ru_model = FSMTForConditionalGeneration.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_ru')
    ru_en_model = FSMTForConditionalGeneration.from_pretrained(f'{AI_MODELS_PATH}/tmn_ru_en')
    pt_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_pt_en')
    en_pt_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_pt')
    en_de_model = FSMTForConditionalGeneration.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_de')
    de_en_model = FSMTForConditionalGeneration.from_pretrained(f'{AI_MODELS_PATH}/tmn_de_en')
    af_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_af_en')
    en_af_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_af')
    bg_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_bg_en')
    en_bg_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_bg')

    xh_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_xh_en')
    en_xh_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_xh')

    swc_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_swc_en')
    en_swc_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_swc')

    mk_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_mk_en')
    en_mk_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_mk')

    cy_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_cy_en')
    en_cy_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_cy')

    et_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_et_en')
    en_et_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_et')

    eu_en_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_eu_en')
    en_eu_model = AutoModelForSeq2SeqLM.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_eu')


    # Libra model
    en_zh = ""
    zh_en = ""
    en_ko = ""
    ko_en = ""
    en_hi = ""
    hi_en = ""
    en_ar = ""
    ar_en = ""
    en_uk = ""
    uk_en = ""
    en_tr = ""
    tr_en = ""
    en_vi = ""
    vi_en = ""
    en_az = ""
    az_en = ""
    en_cz = ""
    cz_en = ""
    en_fi = ""
    fi_en = ""
    en_el = ""
    el_en = ""
    en_eo = ""
    eo_en = ""

    en_hu = ""
    hu_en = ""

    en_ga = ""
    ga_en = ""

    fa_en = ""
    en_fa = ""

    en_sk = ""
    sk_en = ""
    
    en_ca = ""
    ca_en = ""

    en_cs = ""
    cs_en = ""

    en_da = ""
    da_en = ""

    en_ha = ""
    ha_en = ""

    en_pl = ""
    pl_en = ""

    en_sv = ""
    sv_en = ""

    en_th = ""
    th_en = ""

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
            "translate.en_de": self.translate_en_de,
            "translate.de_en": self.translate_de_en,
            "translate.af_en": self.translate_af_en,
            "translate.en_af": self.translate_en_af,
            "translate.en_zh": self.translate_en_zh,
            "translate.zh_en": self.translate_zh_en,
            "translate.en_ko": self.translate_en_ko,
            "translate.ko_en": self.translate_ko_en,
            "translate.en_hi": self.translate_en_hi,
            "translate.hi_en": self.translate_hi_en,
            "translate.en_ar": self.translate_en_ar,
            "translate.ar_en": self.translate_ar_en,
            "translate.en_uk": self.translate_en_uk,
            "translate.uk_en": self.translate_uk_en,
            "translate.en_tr": self.translate_en_tr,
            "translate.tr_en": self.translate_tr_en,
            "translate.en_vi": self.translate_en_vi,
            "translate.vi_en": self.translate_vi_en,
            "translate.az_en": self.translate_az_en,
            "translate.en_az": self.translate_en_az,
            "translate.cz_en": self.translate_cz_en,
            "translate.en_cz": self.translate_en_cz,
            "translate.en_fi": self.translate_en_fi,
            "translate.fi_en": self.translate_fi_en,
            "translate.en_el": self.translate_en_el,
            "translate.el_en": self.translate_el_en,
            "translate.eo_en": self.translate_eo_en,
            "translate.en_eo": self.translate_en_eo,
            "translate.en_hu": self.translate_en_hu,
            "translate.hu_en": self.translate_hu_en,
            "translate.ga_en": self.translate_ga_en,
            "translate.en_ga": self.translate_en_ga,
            "translate.en_fa": self.translate_en_fa,
            "translate.fa_en": self.translate_fa_en,
            "translate.sk_en": self.translate_sk_en,
            "translate.en_sk": self.translate_en_sk,
            "translate.ca_en": self.translate_ca_en,
            "translate.en_ca": self.translate_en_ca,

            "translate.cs_en": self.translate_cs_en,
            "translate.en_cs": self.translate_en_cs,

            "translate.da_en": self.translate_da_en,
            "translate.en_da": self.translate_en_da,

            "translate.ha_en": self.translate_ha_en,
            "translate.en_ha": self.translate_en_ha,

            "translate.pl_en": self.translate_pl_en,
            "translate.en_pl": self.translate_en_pl,

            "translate.sv_en": self.translate_sv_en,
            "translate.en_sv": self.translate_en_sv,

            "translate.th_en": self.translate_th_en,
            "translate.en_th": self.translate_en_th,

            "translate.bg_en": self.translate_bg_en,
            "translate.en_bg": self.translate_en_bg,

            "translate.xh_en": self.translate_xh_en,
            "translate.en_xh": self.translate_en_xh,

            "translate.swc_en": self.translate_swc_en,
            "translate.en_swc": self.translate_en_swc,

            "translate.mk_en": self.translate_mk_en,
            "translate.en_mk": self.translate_en_mk,

            "translate.cy_en": self.translate_cy_en,
            "translate.en_cy": self.translate_en_cy,

            "translate.et_en": self.translate_et_en,
            "translate.en_et": self.translate_en_et,

            "translate.eu_en": self.translate_eu_en,
            "translate.en_eu": self.translate_en_eu,
        }

    def translate_en_es(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_es')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_es_model.generate(input_ids)
        translated_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("English -> Spanish Model working.")
        # print("Jugard also working")
        # print("English -> Zulu Model working.")
        return translated_text

    def language_detection(self, input_text):
        lang = detect(input_text)
        print("Detected language is ", lang)
        return lang

    def translate_en_fr(self, input_text):

        # sentence_list = []
        #
        # starting_range = 0
        # for i in range(len(input_text)):
        #     if(input_text[i] in eng_seprator_set):
        #         sentence = input_text[starting_range : i+1]
        #         sentence_list.append(sentence.strip())
        #         starting_range = i+1
        #
        # ans = ""
        #
        # for i in sentence_list:
        #     query = {'source_lang': 'English',
        #     'target_lang' : 'French',
        #     'input_data': i}
        #     result = requests.post(url, params=query)
        #     rawJson = result.json()
        #     translatedOutput = html.unescape(rawJson['data'])
        #     ans = ans+ " " + translatedOutput
        # #print("English -> French Model working.")
        # return ans

        pload = {'q':input_text,
                 'source':'en',
                'target':'fr',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Korean Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_es_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_es_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.es_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("Spanish -> English Model working.")
        # print("Jugard also working")
        # print("Zulu -> English Model working.")
        return output_text

    def translate_fr_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_fr_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.fr_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("French -> English Model working.")
        return output_text

    def translate_zu_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_zu_en')
        input_ids = tokenizer.encode(('>>zul<<'+input_text), return_tensors="pt")
        output_decoded = self.zu_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("Zulu -> English Model working.")
        return output_text

    def translate_en_zu(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_zu')
        input_ids = tokenizer.encode(('>>zul<<'+input_text), return_tensors="pt")
        output_decoded = self.en_zu_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("English -> Zulu Model working.")
        return output_text

    def translate_en_id(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_id')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_id_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("English -> Indonesian Model working.")
        return output_text

    def translate_id_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_id_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.id_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("Indonesian -> English Model working.")
        return output_text

    def translate_nl_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_nl_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.nl_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("Dutch -> English Model working.")
        return output_text

    def translate_en_nl(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_nl')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_nl_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("English -> Dutch Model working.")
        return output_text

    def translate_en_it(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_it')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_it_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("English -> Italian Model working.")
        return output_text

    def translate_it_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_it_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.it_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("Italian -> English Model working.")
        return output_text

    def translate_ja_en(self, input_text):
        pload = {'q':input_text,
                 'source':'ja',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Japanese -> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_ja(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'ja',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Japanese Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_ru(self, input_text):
        tokenizer = FSMTTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_ru')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_ru_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("English -> Russian Model working.")
        return output_text

    def translate_ru_en(self, input_text):
        tokenizer = FSMTTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_ru_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.ru_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("Russian -> English Model working.")
        return output_text

    def translate_en_pt(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_pt')
        input_ids = tokenizer.encode(('>>por<<'+input_text), return_tensors="pt")
        output_decoded = self.en_pt_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("English -> Portuguese Model working.")
        return output_text

    def translate_pt_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_pt_en')
        input_ids = tokenizer.encode(('>>por<<'+input_text), return_tensors="pt")
        output_decoded = self.pt_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("Portuguese -> English Model working.")
        return output_text

    def translate_de_en(self, input_text):
        tokenizer = FSMTTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_de_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.de_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("German -> English Model working.")
        return output_text

    def translate_en_de(self, input_text):
        tokenizer = FSMTTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_de')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_de_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("English -> German Model working.")
        return output_text
    def translate_en_af(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_af')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_af_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("English -> Afrikaans Model working.")
        return output_text

    def translate_af_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_af_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.af_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("Afrikaans -> English Model working.")
        return output_text

    def translate_zh_en(self, input_text):

        pload = {'q':input_text,
                 'source':'zh',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Chinese -> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_zh(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'zh',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Chinese Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_ko_en(self, input_text):

        pload = {'q':input_text,
                 'source':'ko',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Korean -> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_ko(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'ko',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Korean Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_hi(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'hi',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Hindi Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_hi_en(self, input_text):
        pload = {'q':input_text,
                 'source':'hi',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Hindi -> English Model working.")
        output = (r.json()['translatedText'])
        return output


    def translate_en_ar(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'ar',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Arabic Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_ar_en(self, input_text):
        pload = {'q':input_text,
                 'source':'ar',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Arabic -> English Model working.")
        output = (r.json()['translatedText'])
        return output


    def translate_en_uk(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'uk',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Ukerian Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_uk_en(self, input_text):
        pload = {'q':input_text,
                 'source':'uk',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Ukerian -> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_tr(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'tr',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Turkish Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_tr_en(self, input_text):
        pload = {'q':input_text,
                 'source':'tr',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Trukish-> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_vi(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'vi',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> VI Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_vi_en(self, input_text):
        pload = {'q':input_text,
                 'source':'vi',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("VI-> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_az_en(self, input_text):
        pload = {'q':input_text,
                 'source':'az',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("AZ-> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_az(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'az',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> AZ Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_cz(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'cz',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> CZ Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_cz_en(self, input_text):
        pload = {'q':input_text,
                 'source':'cz',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("CZ -> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_fi_en(self, input_text):
        pload = {'q':input_text,
                 'source':'fi',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("FI -> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_fi(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'fi',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> FI Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_el(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'el',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Greek Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_el_en(self, input_text):
        pload = {'q':input_text,
                 'source':'el',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Greek -> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_eo_en(self, input_text):
        pload = {'q':input_text,
                 'source':'eo',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Esperanto -> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_eo(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'eo',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Esperanto Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_hu(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'hu',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Hungarian Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_hu_en(self, input_text):
        pload = {'q':input_text,
                 'source':'hu',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Hungarian Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_ga_en(self, input_text):
        pload = {'q':input_text,
                 'source':'ga',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Irish -> Hungarian Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_ga(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'ga',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Irish Model working.")
        output = (r.json()['translatedText'])
        return output


    def translate_en_fa(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'fa',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Persian -> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_fa_en(self, input_text):
        pload = {'q':input_text,
                 'source':'fa',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Persian -> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_sk_en(self, input_text):
        pload = {'q':input_text,
                 'source':'sk',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Solvik -> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_sk(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'sk',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English-> Solvik Model working.")
        output = (r.json()['translatedText'])
        return output


    def translate_en_ca(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'ca',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English-> Catalan Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_ca_en(self, input_text):
        pload = {'q':input_text,
                 'source':'ca',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Catalan-> English Model working.")
        output = (r.json()['translatedText'])
        return output

    # Adding Czech-cs

    def translate_cs_en(self, input_text):
        pload = {'q':input_text,
                 'source':'cs',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Czech -> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_cs(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'cs',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Czech Model working.")
        output = (r.json()['translatedText'])
        return output

    # Adding Danish-da

    def translate_da_en(self, input_text):
        pload = {'q':input_text,
                 'source':'da',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Danish -> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_da(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'da',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Danish Model working.")
        output = (r.json()['translatedText'])
        return output

    # Adding Hebrew-ha

    def translate_ha_en(self, input_text):
        pload = {'q':input_text,
                 'source':'ha',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Hebrew -> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_ha(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'ha',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Hebrew Model working.")
        output = (r.json()['translatedText'])
        return output

    # Adding Polish - pl

    def translate_pl_en(self, input_text):
        pload = {'q':input_text,
                 'source':'pl',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Polish -> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_pl(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'pl',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Polish Model working.")
        output = (r.json()['translatedText'])
        return output

    # Adding Swedish - sv

    def translate_sv_en(self, input_text):
        pload = {'q':input_text,
                 'source':'sv',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Swedish -> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_sv(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'sv',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Swedish Model working.")
        output = (r.json()['translatedText'])
        return output

    # Adding Thai - th

    def translate_th_en(self, input_text):
        pload = {'q':input_text,
                 'source':'th',
                'target':'en',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("Thai -> English Model working.")
        output = (r.json()['translatedText'])
        return output

    def translate_en_th(self, input_text):
        pload = {'q':input_text,
                 'source':'en',
                'target':'th',
                'format':'text'}
        r = requests.post(libra_url,data = pload)
        print("English -> Thai Model working.")
        output = (r.json()['translatedText'])
        return output

    # For BG:
    def translate_en_bg(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_bg')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_bg_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("English -> Bulgurain Model working.")
        return output_text

    def translate_bg_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_bg_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.bg_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("Bulgurain -> English Model working.")
        return output_text

    # For XH:
    def translate_en_xh(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_xh')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_xh_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("English -> Xhosa Model working.")
        return output_text

    def translate_xh_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_xh_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.xh_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("Xhosa -> English Model working.")
        return output_text

    # For SWC:
    def translate_en_swc(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_swc')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_swc_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("English -> Swahilli Model working.")
        return output_text

    def translate_swc_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_swc_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.swc_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("Swahilli -> English Model working.")
        return output_text

    # For Mk:
    def translate_en_mk(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_mk')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_mk_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("English -> Macedonian Model working.")
        return output_text

    def translate_mk_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_mk_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.mk_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("Macedonian -> English Model working.")
        return output_text

    # For Cy:
    def translate_en_cy(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_cy')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_cy_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("English -> Welish Model working.")
        return output_text

    def translate_cy_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_cy_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.cy_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("Welish -> English Model working.")
        return output_text

    # For et:
    def translate_en_et(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_et')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_et_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("English -> Estonian Model working.")
        return output_text

    def translate_et_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_et_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.et_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("Estonian -> English Model working.")
        return output_text

    # For Basque (eu):
    def translate_en_eu(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_en_eu')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.en_eu_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("English -> Basque Model working.")
        return output_text

    def translate_eu_en(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(f'{AI_MODELS_PATH}/tmn_eu_en')
        input_ids = tokenizer.encode((input_text), return_tensors="pt")
        output_decoded = self.eu_en_model.generate(input_ids)
        output_text = tokenizer.decode(output_decoded[0], skip_special_tokens=True)
        print("Basque -> English Model working.")
        return output_text


