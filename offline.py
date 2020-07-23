dict = dict()
listAllSentences = []


with open("about.txt") as the_file:
     allSentences = the_file.read().split("\n")

     for i in range(len(allSentences)):
         listAllSentences.append({"completed_sentence": allSentences[i], "source_text": "about.txt", "offset": i})


def init_data():
     for sentence in range(len(listAllSentences)):
        res = [listAllSentences[sentence]["completed_sentence"][i: j]
               for i in range(len(listAllSentences[sentence]["completed_sentence"]))
               for j in range(i + 1, len(listAllSentences[sentence]["completed_sentence"]) + 1)]

        for substring in range(len(res)):
            dict.setdefault(res[substring], set()).add(sentence)
