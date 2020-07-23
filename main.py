from offline import init_data, dict
from online import get_best_k_completions


if __name__ == '__main__':

    print("Loading the file and preparing the system...")
    init_data()

    sentence = input("The system is ready. Enter your text:")
    print(sentence)

    while sentence != '#':

        print(get_best_k_completions(sentence))

        # if suggestions:
        #     print(f'There are {len((suggestions))} suggestions')
        #
        #     for i in range(len(suggestions)):
        #         #print(f'')
        #
        # else:
        #     print("There are'nt suggestions")
        #
        #
        sentence = input("Enter your text:")