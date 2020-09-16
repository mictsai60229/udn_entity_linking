from bs4 import BeautifulSoup
import re


chinese_sysmbols = "。，、；：？！「」『』－…"

EN_ZH_REGEX = "|".join([r"\w+", r'[\u4e00-\ufaff]', r'[^\s]'])
TOKENIZIER = re.compile(EN_ZH_REGEX, flags=re.ASCII)

def extract_text_from_html(html):
    soup = BeautifulSoup(html, features="html.parser")
    return soup.text

def tokenize_with_idx(s):
    for match in TOKENIZIER.finditer(s):
        yield match.span()

def split_string(paragraph):

    pre_end = 0
    for match in re.finditer("[{}]+".format(chinese_sysmbols), paragraph):
        start, end = match.span()
        
        if start != pre_end:
            yield  pre_end, paragraph[pre_end:start]
        
        pre_end = end
    
    if len(paragraph) != pre_end:
        yield pre_end, paragraph[pre_end:]
        
        
def gen_ngram(s, ngram_range=(2, 5)):
    
    tokens = list(tokenize_with_idx(s))
    
    for l in range(ngram_range[0], ngram_range[1]+1):
        for start in range(len(tokens)-l+1):
            end = start + l -1
            
            yield tokens[start][0], tokens[end][1]
            
def merge_span(entity_data):
    
    
    entity_data.sort(key=lambda x: x[0])
    
    res = []
    for start, text, wiki_link in entity_data:
        
        
        while res and res[-1][0]+len(res[-1][1]) > start:
            if len(text) > len(res[-1][1]):
                res.pop()
            else:
                break
        else:
            res.append((start, text, wiki_link))
    
    return res
