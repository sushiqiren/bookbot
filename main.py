def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

main()

def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()

        count = 0
        for word in words:
            count += 1

    return count

word_number = count_words()
print(word_number)

def count_characters():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        all_words = file_contents.lower()

        result = {}
        for character in all_words:
            if character in result:
                result[character] += 1
            else:
                result[character] = 1

        return result

char_count = count_characters()
print(char_count)

def print_report():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        words_length = len(words)
        all_words = file_contents.lower()

        result = {}
        for character in all_words:
            if character in result:
                result[character] += 1
            else:
                result[character] = 1

        list_of_dicts = [{"char": key, "count": value} for key, value in result.items()]
        filtered_list = []
        def sort_on(dict):
            return dict["count"]
        for item in list_of_dicts:
            if item["char"].isalpha():
                filtered_list.append(item)
        
        filtered_list.sort(reverse=True, key=sort_on)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words_length} words found in the document")
        print()
        print()
        for item in filtered_list:
            print(f"The {item['char']} character was found {item['count']} times")

        print("--- End report ---")

print_report()