from offline import dict,listAllSentences
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
            if dict.get(str[:j] + char + str[j + 1:]):
                for k in dict[str[:j] + char + str[j + 1:]]:
                    if char not in str[j]:
                        score = len(str) * 2 - 5 + j if j < 5 else len(str) - 1
                        if check_list(listSentences, k, score):
                            listSentences.append({"sentence": k, "score": score})
    return listSentences

def add_str(str, listSentences):
    return

def remove_str(str, listSentences):
    return

def get_best_k_completions(str):
    listSentences = []

    if dict.get(str):
        for i in list(dict[str]):
            listSentences.append({"sentence": i, "score": len(str)*2})

        if len(listSentences) >= 5:
            listSentences = sorted(listSentences, key=lambda a: listAllSentences[a["sentence"]])

            return listSentences[:5]

    listSentences = replace_str(str, listSentences)
    listSentences = add_str(str, listSentences)
    listSentences = remove_str(str, listSentences)

    listSentences = sorted(listSentences, key=lambda a: a["score"], reverse=True)

    if len(listSentences) <= 5:
        return listSentences

    #listSentences = sorted(listSentences, key=lambda a: listAllSentences[a["sentence"]])
    #listSentences = listSentences[:5]
    return listSentences[:5]