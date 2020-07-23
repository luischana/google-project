class AutocompleteData:
    def __init(self, completed_sentence, source_text, offset, score):
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.offset = offset
        self.score = score

    def get_completed_sentence(self):
        return self.completed_sentence

    def get_source_text(self):
        return self.source_text
