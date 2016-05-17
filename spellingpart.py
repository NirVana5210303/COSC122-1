from spelling import *
dictionary = load_dict_words("words_latin-1.txt")
document = load_doc_words("humnature.txt")
spellcheck_with_hashtable(document, dictionary,"Linear",10000)