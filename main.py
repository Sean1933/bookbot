def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count = get_number_of_words(text)
  print(f"--- Begin report of {book_path} ---")
  print(f"{word_count} words found in the text")
  char_dict = get_number_of_each_char(text)
  alphabet_list = dict_to_alphabet_dict_list(char_dict)
  alphabet_list.sort(reverse=True, key=sort_on)
  print("")
  for item in alphabet_list:
    print(f"The '{item["char"]}' character was found {item["count"]} times")
  print("--- End report ---")


def sort_on(dict):
    return dict["count"]

  
def get_book_text(path):
  with open(path) as f:
    return f.read()
  
  
def get_number_of_words(text):
  words = text.split()
  return len(words)


def get_number_of_each_char(text):
  lowered_text = text.lower()
  char_dict = {}
  for char in lowered_text:
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1
  return char_dict


def dict_to_alphabet_dict_list(dict):
  list = []
  for key in dict:
    if key.isalpha():
      temp_dict = {
        "char": key, 
        "count": dict[key],
      }
      list.append(temp_dict)
  return list


main()
