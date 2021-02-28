from allennlp.predictors.predictor import Predictor
import allennlp_models.tagging

from allennlp import spacy
spacy.load('en_core_web_sm')

sent = "Tom is eating an orange. He likes it a lot. His friends are coming to meet him. He is very happy."
# srl
# srl_predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/structured-prediction-srl-bert.2020.12.15.tar.gz")
# d_srl = srl_predictor.predict(sentence=sent)

# ner_predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/ner-model-2020.02.10.tar.gz")
# d_ner = ner_predictor.predict(sentence=sent)
# print(d_ner)
# print("\n\n")
# print(d_srl)
# sent = "Tom kept eating an orange while taking a bath even though he was being stabbed by fifeen assassins."

# d = {'verbs': [{'verb': 'ate', 'description': '[ARG0: Tom] [V: ate] [ARG1: an orange] [ARGM-TMP: at 7 pm] .', 'tags': ['B-ARG0', 'B-V', 'B-ARG1', 'I-ARG1', 'B-ARGM-TMP', 'I-ARGM-TMP', 'I-ARGM-TMP', 'O']}], 'words': ['Tom', 'ate', 'an', 'orange', 'at', '7', 'pm', '.']}
# d_ner = {'logits': [[-0.8944995999336243, -0.2821699380874634, 4.111729145050049, 5.431960105895996, -0.7928966283798218, 1.6409562826156616, -2.7721023559570312, -4.8095479011535645, 15.433773040771484, -6.865987777709961, -3.172950506210327, -4.956551551818848, -3.573307514190674, -4.603107452392578, -5.627499103546143, -7.25503396987915, -6.51131010055542], [12.287548065185547, -3.259787082672119, -5.198975563049316, 0.4226338267326355, -6.452572345733643, -4.048359394073486, -4.844081878662109, -1.6231307983398438, -3.0197196006774902, -1.2246475219726562, -6.685851573944092, -1.9443731307983398, -3.173400402069092, -2.1511707305908203, -1.2762941122055054, -1.2022603750228882, -2.658850908279419], [13.720171928405762, -3.9718642234802246, -2.8336803913116455, -4.014450550079346, -4.933221340179443, -3.861921787261963, -2.5951309204101562, -1.950015664100647, -3.3052475452423096, -0.9582913517951965, -5.508761405944824, -3.819340229034424, -2.9621148109436035, -2.258315324783325, -1.4654698371887207, -3.5969035625457764, -2.846620559692383], [14.02932357788086, -4.127925872802734, -3.2175145149230957, -5.2415924072265625, -4.364380359649658, -3.5292234420776367, -2.390408515930176, -1.7163431644439697, -4.500847816467285, -1.1066012382507324, -5.243618488311768, -3.8969576358795166, -2.7855913639068604, -1.6691999435424805, -1.6415835618972778, -3.835644245147705, -2.697112798690796], [12.808060646057129, -2.5009427070617676, -2.731504201889038, -4.59443473815918, -3.874433994293213, -4.684471130371094, -2.295034646987915, -1.3214375972747803, -4.453030586242676, -0.7749080061912537, -4.318513870239258, -2.905687093734741, -3.259880781173706, -2.018951654434204, -1.4447660446166992, -3.2060000896453857, -2.0652356147766113], [13.732135772705078, -2.6416008472442627, -2.990342617034912, -5.4934797286987305, -4.176853179931641, -3.877594470977783, -2.0392954349517822, -1.9918878078460693, -5.1829071044921875, -1.450124979019165, -4.430850982666016, -3.4789767265319824, -2.8478903770446777, -1.8913609981536865, -2.0351243019104004, -3.676975727081299, -2.793400287628174], [13.573280334472656, -2.8384623527526855, -3.489760637283325, -5.433706283569336, -4.138489723205566, -2.527034044265747, -2.237649917602539, -2.2159957885742188, -4.895359516143799, -1.7765653133392334, -4.563727378845215, -3.765561819076538, -2.785114288330078, -1.7999032735824585, -2.4094321727752686, -4.040374755859375, -3.119126319885254], [12.114035606384277, -2.459475517272949, -3.422168254852295, -4.162457466125488, -2.7337265014648438, -3.8660900592803955, -2.3692586421966553, -1.3079628944396973, -3.876559257507324, -1.4217610359191895, -4.978134632110596, -2.801004409790039, -3.484952211380005, -2.2438411712646484, -1.8268369436264038, -3.717989444732666, -2.6780741214752197]], 'mask': [True, True, True, True, True, True, True, True], 'tags': ['U-PER', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 'words': ['Tom', 'ate', 'an', 'orange', 'at', '7', 'pm', '.']}

# d_srl = {'verbs': [{'verb': 'kept', 'description': '[ARG0: Tom] [V: kept] [ARG1: eating an orange while taking a bath even though he was being stabbed by fifeen assassins] .', 'tags': ['B-ARG0', 'B-V', 'B-ARG1', 'I-ARG1', 'I-ARG1', 'I-ARG1', 'I-ARG1', 'I-ARG1', 'I-ARG1', 'I-ARG1', 'I-ARG1', 'I-ARG1', 'I-ARG1', 'I-ARG1', 'I-ARG1', 'I-ARG1', 'I-ARG1', 'I-ARG1', 'O']}, {'verb': 'eating', 'description': '[ARG0: Tom] kept [V: eating] [ARG1: an orange] [ARGM-TMP: while taking a bath] even though he was being stabbed by fifeen assassins .', 'tags': ['B-ARG0', 'O', 'B-V', 'B-ARG1', 'I-ARG1', 'B-ARGM-TMP', 'I-ARGM-TMP', 'I-ARGM-TMP', 'I-ARGM-TMP', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']}, {'verb': 'taking', 'description': '[ARG0: Tom] kept eating an orange while [V: taking] [ARG1: a bath] even though he was being stabbed by fifeen assassins .', 'tags': ['B-ARG0', 'O', 'O', 'O', 'O', 'O', 'B-V', 'B-ARG1', 'I-ARG1', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']}, {'verb': 'was', 'description': 'Tom kept eating an orange while taking a bath even though he [V: was] being stabbed by fifeen assassins .', 'tags': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-V', 'O', 'O', 'O', 'O', 'O', 'O']}, {'verb': 'being', 'description': 'Tom kept eating an orange while taking a bath even though he was [V: being] stabbed by fifeen assassins .', 'tags': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-V', 'O', 'O', 'O', 'O', 'O']}, {'verb': 'stabbed', 'description': 'Tom kept eating an orange while taking a bath even though [ARG1: he] was being [V: stabbed] [ARG0: by fifeen assassins] .', 'tags': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-ARG1', 'O', 'O', 'B-V', 'B-ARG0', 'I-ARG0', 'I-ARG0', 'O']}], 'words': ['Tom', 'kept', 'eating', 'an', 'orange', 'while', 'taking', 'a', 'bath', 'even', 'though', 'he', 'was', 'being', 'stabbed', 'by', 'fifeen', 'assassins', '.']}
# d_ner = {'mask': [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], 'tags': ['U-PER', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 'words': ['Tom', 'kept', 'eating', 'an', 'orange', 'while', 'taking', 'a', 'bath', 'even', 'though', 'he', 'was', 'being', 'stabbed', 'by', 'fifeen', 'assassins', '.']}

d_ner = {'mask': [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], 'tags': ['U-PER', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 'words': ['Tom', 'is', 'eating', 'an', 'orange', '.', 'He', 'likes', 'it', 'a', 'lot', '.', 'His', 'friends', 'are', 'coming', 'to', 'meet', 'him', '.', 'He', 'is', 'very', 'happy', '.']}
d_srl = {'verbs': [{'verb': 'is', 'description': 'Tom [V: is] eating an orange . He likes it a lot . His friends are coming to meet him . He is very happy .', 'tags': ['O', 'B-V', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']}, {'verb': 'eating', 'description': '[ARG0: Tom] is [V: eating] [ARG1: an orange] . He likes it a lot . His friends are coming to meet him . He is very happy .', 'tags': ['B-ARG0', 'O', 'B-V', 'B-ARG1', 'I-ARG1', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']}, {'verb': 'likes', 'description': 'Tom is eating an orange . [ARG0: He] [V: likes] [ARG1: it] [ARGM-EXT: a lot] . His friends are coming to meet him . He is very happy .', 'tags': ['O', 'O', 'O', 'O', 'O', 'O', 'B-ARG0', 'B-V', 'B-ARG1', 'B-ARGM-EXT', 'I-ARGM-EXT', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']}, {'verb': 'are', 'description': 'Tom is eating an orange . He likes it a lot . His friends [V: are] coming to meet him . He is very happy .', 'tags': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-V', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']}, {'verb': 'coming', 'description': 'Tom is eating an orange . He likes it a lot . [ARG1: His friends] are [V: coming] [ARGM-PRP: to meet him] . He is very happy .', 'tags': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-ARG1', 'I-ARG1', 'O', 'B-V', 'B-ARGM-PRP', 'I-ARGM-PRP', 'I-ARGM-PRP', 'O', 'O', 'O', 'O', 'O', 'O']}, {'verb': 'meet', 'description': 'Tom is eating an orange . He likes it a lot . [ARG0: His friends] are coming to [V: meet] [ARG1: him] . He is very happy .', 'tags': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-ARG0', 'I-ARG0', 'O', 'O', 'O', 'B-V', 'B-ARG1', 'O', 'O', 'O', 'O', 'O', 'O']}, {'verb': 'is', 'description': 'Tom is eating an orange . He likes it a lot . His friends are coming to meet him . [ARG1: He] [V: is] [ARG2: very happy] .', 'tags': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-ARG1', 'B-V', 'B-ARG2', 'I-ARG2', 'O']}], 'words': ['Tom', 'is', 'eating', 'an', 'orange', '.', 'He', 'likes', 'it', 'a', 'lot', '.', 'His', 'friends', 'are', 'coming', 'to', 'meet', 'him', '.', 'He', 'is', 'very', 'happy', '.']}

entities = {}
for i in range(len(d_ner['tags'])):
    if d_ner['tags'][i] != 'O':
        entities[d_ner['words'][i]] = d_ner['tags'][i]
# print(entities)


tagged = {}

# for i in d_srl['verbs']:
#     print(i)

import nltk
tokenized = d_ner['words']
# print(tokenized)

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

tmp=[]
for i in range(len(arg0)):
    if arg0[i] not in tmp:
        tmp.append(arg0[i])
arg0=tmp


tmp=[]
for i in range(len(arg1)):
    if arg1[i] not in tmp:
        tmp.append(arg1[i])
arg1=tmp


sentences = []
i = 0
j = 0
while j < len(tokenized):
    if tokenized[j] == '.':
        sentences.append(tokenized[i:j])
        i = j
    j += 1

for i in range(1, len(sentences)):
    sentences[i] = sentences[i][1:]

print(sentences)

questions = []
for i in range(len(sentences)):
    for j in sentences[i]:
        if j in arg0:
            questions.append("Who")
        else:
            questions.append(j)



# for i in range(len(questions)):
#     tmp=[]
#     for j in questions[i]:
#         if j not in tmp:
#             tmp.append(j)
#     questions=tmp

print(questions)

questions = " ".join(questions).split('Who')[1:]
questions = ["Who" + i for i in questions]
    

for i in range(len(questions)):
    if questions[i]:
        print(questions[i] + "?") 

print(questions)

# print(arg0)
# print(arg1)

