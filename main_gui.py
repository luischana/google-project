from offline import init_data, read_from_file, ignore_char
from online import get_best_k_completions
from tkinter import *


read_from_file()

init_data()

root = Tk()

root.title('Auto Complete')


def search():
    input = entry.get()
    list.delete(0, END)

    if input != "":

        if input[-1] == '#':
            entry.delete(0, END)

        else:
            best_completion = get_best_k_completions(ignore_char(input))
            i = 1

            if best_completion:
                for sentence in best_completion:
                    list.insert(END, f'{i}.{sentence.get_completed_sentence()}  (source: {sentence.get_source_text()}, offset: {sentence.get_offset()}, score: {sentence.get_score()})')
                    list.insert(END, '\n')
                    i += 1

            else:
                list.insert(END, 'no results!')


entry = Entry(width=100)
entry.grid(row=0, column=0)

button_search = Button(root, text='Search', width=5, command=search)
button_search.grid(row=0, column=1)

list = Listbox(root, width=100)
list.grid(row=1, column=0)

root.mainloop()
