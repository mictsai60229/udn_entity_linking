import html
import os

from ner.ckip_ner import gen_ner


ENTITY_SPAN_HTML = """<span class="entity" data-start_end="{start} {end}">{entity}</span>"""

def gen_ner_html(paragraph):
    
    entity = gen_ner(paragraph)
    new_paragraph = ""
    
    prev_end = 0
    for start, end, type_, text in entity:
        new_paragraph += paragraph[prev_end:start]
        new_paragraph += ENTITY_SPAN_HTML.format(start=start, end=end, entity=text)

        prev_end = end
    
    new_paragraph += paragraph[prev_end:]

    return {'paragraph': new_paragraph, 'entity': entity}
