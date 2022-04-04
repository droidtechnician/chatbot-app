import nltk
from nltk.tag.stanford import StanfordNERTagger, StanfordPOSTagger

# Download CoreNLP NER from https://nlp.stanford.edu/software/stanford-ner-4.2.0.zip
# Download CoreNLP NER Postagger https://nlp.stanford.edu/software/stanford-tagger-4.2.0.zip

base_url = ''
ner_tagger_jar = '/stanford-ner-4.2.0/stanford-ner-2020-11-17/stanford-ner.jar'
ner_tagger_model = '/stanford-ner-4.2.0/stanford-ner-2020-11-17/classifiers/english.conll.4class.distsim.crf.ser.gz'
pos_tagger_jar = "/stanford-tagger-4.2.0/stanford-postagger-full-2020-11-17/stanford-postagger.jar"
pos_tagger_model = "/stanford-tagger-4.2.0/stanford-postagger-full-2020-11-17/models/english-bidirectional-distsim.tagger"

# Prepare NER tagger with english model
ner_tagger = StanfordNERTagger(ner_tagger_model, ner_tagger_jar, encoding='utf8')
pos_tagger = StanfordPOSTagger(pos_tagger_model, pos_tagger_jar, encoding = "utf-8")

class ContextClassificationModel:

    def evaluate(self, sentence):
        # Tokenize: Split sentence into words
        words = nltk.word_tokenize(sentence)

        # Run NER tagger & POS Tagger on words
        print(pos_tagger.tag(words))

        tagger = {}

        tagger['tags'] = ner_tagger.tag(words)
        tagger['pos'] = pos_tagger.tag(words)

        return tagger 
        