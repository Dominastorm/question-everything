from allennlp.predictors.predictor import Predictor
import allennlp_models.tagging

from allennlp import spacy
spacy.load('en_core_web_sm')

import nltk

# qsns = no. of questions
# blanks = no. of fill in the blanks
def generator(input_text, qsns=5, blanks=5):
    output_file = open(r"C:\My Folders\Competitions\SpaceJam 2021\Final Files\output.txt", "w")

    # semantic role labelling
    srl_predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/structured-prediction-srl-bert.2020.12.15.tar.gz")
    d_srl = srl_predictor.predict(sentence=input_text)

    # named entity recognition
    ner_predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/ner-model-2020.02.10.tar.gz")
    d_ner = ner_predictor.predict(sentence=input_text)

    
    entities = {}
    for i in range(len(d_ner['tags'])):
        if d_ner['tags'][i] != 'O':
            entities[d_ner['words'][i]] = d_ner['tags'][i]

    # not sure why
    tagged = {}

    tokenized = d_ner['words']
    print(tokenized)


    tagged_list = []

    def process_contents():
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged_list.append(list(nltk.pos_tag(words)[0]))

    process_contents()
    # print(tagged_list)

    arg0 = []
    arg1 = []
    for i in range(len(d_srl['verbs'])):
        verb = d_srl['verbs'][i]['verb']
        for i in d_srl['verbs'][i]['description'].split('] '):
            if 'ARG0' in i:
                start = i.index(':')+2
                arg0.append(i[start:])
            elif 'ARG1' in i:
                start = i.index(':')+2
                arg1.append(i[start:])

    print(arg0)
    print(arg1)
    output_file.write(input_text)
    output_file.write("qsns: "+str(qsns)+" fib: "+str(blanks))
    output_file.close()
