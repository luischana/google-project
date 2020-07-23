import os, re
dictFile = dict()
dict = dict()
listAllSentences = []


def init_list_dict(path, ind):
    with open(path, encoding='UTF-8') as the_file:
        temp_list_string = the_file.read().split("\n")
    for index_line, line in enumerate(temp_list_string, 1):
        listAllSentences.append({"completed_sentence": line, "source_text": ind, "offset": index_line})


def read_from_file():
    for dirpath, dirnames, files in os.walk('c-api', topdown=True):
        for ind, file_name in enumerate(files, 1):
            dictFile[ind] = file_name
            init_list_dict(dirpath + "\\" + file_name, ind)


def ignore_char(sentence):
    return re.sub('[^a-z]+', '', sentence.lower())


def init_data():
    for sentence in range(len(listAllSentences)):
        sentene_fixed = ignore_char(listAllSentences[sentence]["completed_sentence"])
        res = [sentene_fixed[i: j] for i in range(len(sentene_fixed)) for j in range(i + 1, len(sentene_fixed) + 1)]

        for substring in range(len(res)):
            dict.setdefault(res[substring], set()).add(sentence)
