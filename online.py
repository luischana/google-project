from offline import dict,listAllSentences
from auto_complete_data import AutocompleteData
import string


def check_list(listSentences, sentence, score):
    for i in range(len(listSentences)):
        if sentence == listSentences[i]["sentence"]:
            if score > listSentences[i]["score"]:
                listSentences[i]["score"] = score
            return 0
    return 1


def replace_str(str, listSentences):
    for char in string.ascii_letters:
        for j in range(len(str)):
            if dict.get(str[:j]+char+str[j+1:]):
                for k in dict[str[:j]+char+str[j+1:]]:
                    if char not in str[j]:
                        score = len(str)*2-5+j if j < 5 else len(str)-1
                        if check_list(listSentences, k, score):
                            listSentences.append({"sentence": k, "score": score})
    return listSentences


def add_str(str, listSentences):
    for char in string.printable[10:65]:
        for j in range(len(str)+1):
            if dict.get(str[:j]+char+str[j:]):
                for k in dict[str[:j]+char+str[j:]]:
                    score = len(str)*2-10+2*j if j < 4 else len(str)*2-2
                    if check_list(listSentences, k, score):
                        listSentences.append({"sentence": k, "score": score})
    return listSentences


def remove_str(str, listSentences):
    for j in range(len(str)):
        if dict.get(str[:j]+str[j+1:]):
            if str[:j]+str[j+1:] != str:
                for k in dict[str[:j]+str[j+1:]]:
                    score = len(str)*2-10+2 *j if j < 4 else len(str)*2-2
                    if check_list(listSentences, k, score):
                        listSentences.append({"sentence": k, "score": score})
    return listSentences


def five_sentences(listSentences):
    return [AutocompleteData(listAllSentences[listSentences[x]["sentence"]]["completed_sentence"],
                             listAllSentences[listSentences[x]["sentence"]]["source_text"],
                             listAllSentences[listSentences[x]["sentence"]]["offset"],
                             listSentences[x]["score"]) for x in range(len(listSentences)) if x < 5]


def get_best_k_completions(str):
    listSentences = []

    if dict.get(str):
        for i in list(dict[str]):
            listSentences.append({"sentence": i, "score": len(str)*2})

        if len(listSentences) >= 5:
            listSentences = sorted(listSentences, key=lambda a: listAllSentences[a["sentence"]]["completed_sentence"])
            return five_sentences(listSentences)

    listSentences = replace_str(str, listSentences)
    listSentences = add_str(str, listSentences)
    listSentences = remove_str(str, listSentences)

    listSentences = sorted(listSentences, key=lambda a: a["score"], reverse=True)
    return five_sentences(listSentences)

    #listSentences = sorted(listSentences, key=lambda a: listAllSentences[a["sentence"]])
    #listSentences = listSentences[:5]
