from wordle import wordle
from colorama import Fore

def main():
    print("Hello Wordle!")
    wordle = wordle("APPLE")

while wordle.can_attempts:
    x = input("Type your guess:")

    if len(x) != wordle.WORD_LENGTH:
         print(
              Fore.RED 
              + f"word must be {wordle.WORD_LENGTH} character long!" 
              + Fore.RESET
              )
         continue
         
    wordle.attempts(x)
    display_results(wordle)

    result = wordle.guess(x)
    print(*result, sep="\n")

if wordle.is_solved:
        print("you've solved the puzzle.")
else:
     print("you've failed to solve the puzzle!")


def display_results(wordle:wordle):
     for word in wordle.attempts:
          result = wordle.guess(word)
     pass

def convert_result_to_color(result = List[LetterState]):
     result_with_color = []
     for letter in result:
          if letter.is_in_position:
               color = Fore.GREEN
          elif letter.is_in_word:
               color = Fore.YELLOW
          else:
               colour = Fore.WHITE
          colored_letter  = color + letter.character + Fore.RESET
          result_with_color.append(colored_letter)
          return " ".join(result_with_color)
                    


if __name__ =="__main__":
    main()