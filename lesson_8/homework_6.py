import re

if __name__ == '__main__':
    # Task 1

    test_str_1 = 'Hello_darling1337'
    test_str_2 = "I'm not a single word pattern"


    def is_word_pattern(string) -> bool:
        if re.fullmatch('\w+', string) is not None:
            return True
        else:
            return False


    print(is_word_pattern(test_str_1))
    print(is_word_pattern(test_str_2))

    # Task 2

    test_data = ["example (.com)", "github (.com)", "stackoverflow (.com)"]


    def remove_text_in_parentheses(string) -> str:
        string = re.sub('\s\(\.\w+\)', '', string)
        return string


    for item in test_data:
        print(remove_text_in_parentheses(item))

    # Task 3

    test_string = 'itIsKindOfCamelCase'


    def add_space_to_head_letter(string) -> str:
        letter_set = set(re.findall('[A-Z]', string))
        print(f'Task_3: Letters to replace {letter_set}')
        for letter in letter_set:
            string = re.sub(letter, f' {letter}', string)
        return string


    print(add_space_to_head_letter(test_string))

