#bookbot - Read file
import string

def main() -> int:
  bk_path = "books/frankenstein.txt"
  text = get_book_path(bk_path)
  wordcount = book_words(text)

  char_dict = char_appearances(text)
  char_and_counts = dict_to_sorter(char_dict)
  char_and_counts.sort(reverse=True, key=sort_me)
  characters_report(wordcount, char_and_counts)

def book_words(text) -> int:
  words = text.split()
  ## correct but expensive
  # wordcount = 0
  # for word in words:
  #   wordcount += 1
  # return wordcount

  # better simpler
  return len(words)


def get_book_path(path):
  with open(path) as f:
    return f.read()

def char_appearances(text):
  lowered_text = text.lower()
  # initiate dictionary with lowercase letters as keys and 0 for each of their values
  lowercase_dict = dict.fromkeys(string.ascii_lowercase, 0)
  for char in lowered_text:
    if char in lowercase_dict:
      lowercase_dict[char] += 1
  return lowercase_dict

# convert from dictionary of characters to list of dictionaries
def dict_to_sorter(character_counts):
  sorter = []
  for char, count in character_counts.items():
    sorter.append({"char": char, "count": count})
  return sorter


def sort_me(dict):
  return dict["count"]

def characters_report(words, chars):
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"There are {words} words in the book\n")
  for char in chars:
    print(f"The character '{char["char"]}' was found {char["count"]} times")
  print("--- End report ---")

main()
