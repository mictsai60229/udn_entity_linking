import os
import csv

from .load_bold import BOLD_TABLE


BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")
DATA_DIR = os.path.join(BASE_DIR, "data/ned_data")

class redirect_table(object):
    
    def __init__(self):
        self.load_redirect()
        
        
    def load_redirect(self, file="zhwiki-latest-redirect.tsv", headers=True):
        
        redirect_file = os.path.join(DATA_DIR, file)
        self.redirect2id = {}
        
        with open(redirect_file, errors='replace') as csvfile:
            
            spamreader = csv.reader(csvfile, delimiter='\t')
            
            if headers:
                next(spamreader, None)
            
            for row in spamreader:
                
                wikiid, _, redirect, _, _ = row
                redirect = self._normalize_title(redirect)
                wikiid = int(wikiid)
                
                if wikiid not in BOLD_TABLE.id2title or redirect not in BOLD_TABLE.title2id:
                    continue
                    
                redirect_text = BOLD_TABLE.id2title[wikiid]
                redirect_id = BOLD_TABLE.title2id[redirect]
                
                    
                self.redirect2id[redirect_text] = redirect_id
                
    def _normalize_title(self, title):
        return title.replace("_", " ")
                

REDIRECT_TABLE = redirect_table()