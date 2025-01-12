def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count = get_number_of_words(text)
  print(f"{word_count} words found in the text")
  
  print("Number of each character found in the text")
  char_dict = get_number_of_each_char(text)
  print(char_dict)

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

main()
