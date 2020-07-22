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
    for i in range(count):
        for char in string.printable[11:68]:
            for j in range(len(str)):
                if dict.get(str[:j]+char+str[j+1:]):
                    for k in range(len(str[:j]+char+str[j+1:])):
                        listSentences.append(list(dict[str[:j]+char+str[j+1:]])[k])
    #print(listSentences)


def get_best_k_completions(str):
    listSentences = []
    if dict.get(str):
        for i in list(dict[str]):
            listSentences.append(listAllSentences[i])

        listSentences.sort()

        if len(listSentences) >= 5:
            return listSentences[:5]

        else:
            listSentences.append(replace_str(str, 5-len(listSentences)))

    else:
        listSentences.append(replace_str(str, 5))

    return listSentences


init_data()
print(dict)
print(get_best_k_completions("the"))
replace_str("am", 2)
