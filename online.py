import string
dict = dict()
listAllSentences = []

with open("about.txt") as the_file:
    listAllSentences = the_file.read().split("\n")


def init_data():
    for str in range(len(listAllSentences)):
        for j in range(len(listAllSentences[str])):
            dict.setdefault((listAllSentences[str])[:j+1], set()).add(str)

        listWords = listAllSentences[str].split(" ")

        for word in range(len(listWords)):
            for j in range(len(listWords[word])):
                dict.setdefault((listWords[word])[:j+1], set()).add(str)


def replace_str(str, count):
    listSentences = []
    for char in string.ascii_letters:
        for j in range(len(str)):
            if char not in str[j]:
                if dict.get(str[:j]+char+str[j+1:]):
                    for k in range(len(dict[str[:j]+char+str[j+1:]])):
                        listSentences.append(listAllSentences[list(dict[str[:j]+char+str[j+1:]])[k]])
    #אם קיים ברשימה אותו משפט פעמיים...
    listSentences.sort()
    #return listSentences
    return listSentences[:count]

# def replace_character(sentence, sentences):
#     result = set()
#     for letter in string.ascii_letters:
#         for character in range(len(sentence)):
#             change_sentence = sentence[:character] + letter + sentence[character + 1:]
#             if change_sentence in sentences.keys():
#                 result.union(sentences[change_sentence])
#                 if len(result) >= 5:
#                     return result[:5]
#     return result


def add_str(str, count):
    listSentences = []
    for char in string.printable[10:65]:
        for j in range(len(str)+1):
            if dict.get(str[:j]+char+str[j:]):
                for k in range(len(dict[str[:j]+char+str[j:]])):
                    listSentences.append(list(dict[str[:j]+char+str[j:]])[k])
    #אם קיים ברשימה אותו משפט פעמיים...
    listSentences.sort()
    print(listSentences)


def remove_str(str, count):
    listSentences = []
    for j in range(len(str)):
        if dict.get(str[:j]+str[j+1:]):
            for k in range(len(dict[str[:j]+str[j+1:]])):
                listSentences.append(list(dict[str[:j]+str[j+1:]])[k])
    # אם קיים ברשימה אותו משפט פעמיים...
    listSentences.sort()
    print(listSentences)


def get_best_k_completions(str):
    listSentences = []
    if dict.get(str):
        for i in list(dict[str]):
            listSentences.append(listAllSentences[i])

        listSentences.sort()

        if len(listSentences) >= 5:
            return listSentences[:5]

        else:
            #print(replace_str(str, 5 - len(listSentences)))
            listSentences += replace_str(str, 5-len(listSentences))
            return listSentences

    listSentences += replace_str(str, 5 - len(listSentences))
    return listSentences

    #return listSentences

