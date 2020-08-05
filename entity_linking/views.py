import json

from django.shortcuts import render
from django.http import JsonResponse

from utils.extract import extract_text_from_html
from ner.ner_html import gen_ner_html
from ned.ned import disambiguate_NE

# Create your views here.

def index_view(request):
    return render(request, 'index.html')


def gen_el_view(request):
    
    paragraph = ''
    if request.method == "POST":
        data = json.loads(request.body)

        paragraph = data.get('paragraph', '')

    #paragraph = extract_text_from_html(paragraph)

    if not paragraph:
        return JsonResponse({'paragraph': '請輸入中文', 'entity': []})
    

    result = gen_ner_html(paragraph)

    new_entity = []
    for idx, (start, end, type_, text) in enumerate(result['entity']):

        wiki_title = disambiguate_NE(text)
        if wiki_title:
            new_entity.append([idx, wiki_title])
    result['entity'] = new_entity
    return JsonResponse(result)
    
    
    
