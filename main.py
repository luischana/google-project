from offline import init_data
from online import get_best_k_completions


if __name__ == '__main__':

    print("Loading the file and preparing the system...")

    init_data()

    sentence = input("The system is ready. Enter your text:")

    while sentence[-1] != '#':
        print(sentence)

        suggestions = get_best_k_completions(sentence)

        if suggestions:
            print(f'There are {len((suggestions))} suggestions')

            for i in range(len(suggestions)):
                print(f'{i+1}. {suggestions[i].get_completed_sentence()} ({suggestions[i].get_source_text()} {suggestions[i].get_offset()})')

        else:
            print("There are'nt suggestions")


        sentence = input("Enter your text:")
