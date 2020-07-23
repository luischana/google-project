def replace_str(str, listSentences):

def add_str(str, listSentences):

def remove_str(str, listSentences):

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