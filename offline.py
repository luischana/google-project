import os, re
dict_file = dict()
dict_substring = dict()
list_all_sentences = []


def init_list_dict(path, ind):
    with open(path, encoding='UTF-8') as the_file:
        temp_list_string = the_file.read().split("\n")
    for index_line, line in enumerate(temp_list_string, 1):
        list_all_sentences.append({"completed_sentence": line, "source_text": ind, "offset": index_line})


def read_from_file():
    for dirpath, dirnames, files in os.walk('c-api', topdown=True):
        for ind, file_name in enumerate(files, 1):
            dict_file[ind] = file_name
            init_list_dict(dirpath + "\\" + file_name, ind)


def ignore_char(sentence):
    return re.sub('[^a-z]+', '', sentence.lower())


def init_data():
    for sentence in range(len(list_all_sentences)):
        sentence_fixed = ignore_char(list_all_sentences[sentence]["completed_sentence"])
        res = [sentence_fixed[i: j] for i in range(len(sentence_fixed)) for j in range(i + 1, len(sentence_fixed) + 1)]

        for substring in range(len(res)):
            dict_substring.setdefault(res[substring], set()).add(sentence)
