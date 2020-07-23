dict = dict()
listAllSentences = []

with open("about.txt") as the_file:
    listAllSentences = the_file.read().split("\n")


# with open("about.txt") as the_file:
#     allSentences = the_file.read().split("\n")
#     for i in range(allSentences):
#         listAllSentences.append({"completed_sentence": allSentences[i], "source_text": "about.txt", "offset": i})


def init_data():
    for str in range(len(listAllSentences)):
         for j in range(len(listAllSentences[str])):
             dict.setdefault((listAllSentences[str])[:j+1], set()).add(str)

         listWords = listAllSentences[str].split(" ")

         for word in range(len(listWords)):
             for j in range(len(listWords[word])):
                 dict.setdefault((listWords[word])[:j+1], set()).add(str)

