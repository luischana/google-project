from offline import dict_substring, dict_file, list_all_sentences
from auto_complete_data import AutocompleteData
import string


def check_sentence(list_sentences, sentence, score):
    for i in range(len(list_sentences)):
        if sentence == list_sentences[i]["sentence"]:
            if score > list_sentences[i]["score"]:
                list_sentences[i]["score"] = score

            return list_sentences

    list_sentences.append({"sentence": sentence, "score": score})

    return list_sentences


def replace_letter(str, list_sentences, score):
    for i in range(len(str)):

        for letter in string.ascii_letters:
            if dict_substring.get(str[:i]+letter+str[i+1:]):

                for sentence in dict_substring[str[:i]+letter+str[i+1:]]:
                    if letter not in str[i]:
                        score = score-5+i if i < 5 else score-1
                        check_sentence(list_sentences, sentence, score)

    return list_sentences


def add_letter(str, list_sentences, score):
    for i in range(len(str)+1):

        for letter in string.ascii_letters:
            if dict_substring.get(str[:i]+letter+str[i:]):

                for sentence in dict_substring[str[:i]+letter+str[i:]]:
                    score = score-10+2*i if i < 4 else score-2
                    check_sentence(list_sentences, sentence, score)

    return list_sentences


def remove_letter(str, list_sentences, score):
    for i in range(len(str)):
        if dict_substring.get(str[:i]+str[i+1:]):
            if str[:i]+str[i+1:] != str:

                for sentence in dict_substring[str[:i]+str[i+1:]]:
                    score = score-10+2*i if i < 4 else score-2
                    check_sentence(list_sentences, sentence, score)

    return list_sentences


def five_sentences(list_sentences):
    return [AutocompleteData(list_all_sentences[list_sentences[i]["sentence"]]["completed_sentence"],
                             dict_file[list_all_sentences[list_sentences[i]["sentence"]]["source_text"]],
                             list_all_sentences[list_sentences[i]["sentence"]]["offset"],
                             list_sentences[i]["score"]) for i in range(len(list_sentences)) if i < 5]


def get_best_k_completions(str):
    list_sentences = []
    score = len(str)*2

    if dict_substring.get(str):

        for sentence in list(dict_substring[str]):
            list_sentences.append({"sentence": sentence, "score": score})

    if len(list_sentences) >= 5:
        list_sentences = sorted(list_sentences, key=lambda a: list_all_sentences[a["sentence"]]["completed_sentence"])

    else:
        replace_letter(str, list_sentences, score)
        add_letter(str, list_sentences, score)
        remove_letter(str, list_sentences, score)

        list_sentences = sorted(list_sentences, key=lambda a: a["score"], reverse=True)

    return five_sentences(list_sentences)
