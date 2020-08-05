import os

from ckiptagger import data_utils, construct_dictionary, WS, POS, NER


BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DATA_DIR = os.path.join(BASE_DIR, "data/ner_data")
ws = WS(DATA_DIR)
pos = POS(DATA_DIR)
ner = NER(DATA_DIR)

FILTER_NE = {'DATE', 'CARDINAL', 'TIME', 'MONEY', 'ORDINAL', 'QUANTITY', 'PERCENT'}

def gen_ner(sentence, FILTER_NE=FILTER_NE):
    sentence_list = [sentence]
    word_sentence_list = ws(sentence_list)
    pos_sentence_list = pos(word_sentence_list)
    entity_sentence_list = ner(word_sentence_list, pos_sentence_list)
    entity_sentence = entity_sentence_list[0]
    entity_sentence = [NE for NE in entity_sentence if NE[2] not in FILTER_NE]

    entity_sentence.sort(key=lambda x: x[0])

    return entity_sentence