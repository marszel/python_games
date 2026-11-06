import random

def is_word_valid(word):
    word = word.strip()
    return word.isalpha() and len(word) > 1

def checking_alpha(part_of_speech):
    while True:
        word = input(f"{part_of_speech}: ").strip()
        if is_word_valid(word):
            return word
        print("Please use one word with only letters.")

def get_story(noun, verb, adjective, place):
    return [
        f"""
        Once upon a time, a {adjective} {noun}
        decided to {verb} at the {place}.
        Everyone was surprised, but it turned out
        to be the best idea ever!
        """,
        f"""
        Breaking News! A very {adjective} {noun} 
        was spotted trying to {verb} inside the {place}.
        Local residents say they have never seen anything like it!
        """,
        f"""
        If you ever visit the {place}, watch out for the {adjective} {noun}.
        Legend says that it loves to {verb} when no one is looking!
        """
    ]

def mad_libs():
    print("\nLet's create a story! Fill in the blanks.")
    noun = checking_alpha("Noun").lower()
    verb = checking_alpha("Verb").lower()
    adjective = checking_alpha("Adjective").lower()
    place = checking_alpha("Place").lower().capitalize()
    story = get_story(noun, verb, adjective, place)
    chosen_story = random.choice(story)
    print("\nHere's a story:\n")
    print(chosen_story)
    return chosen_story

def play_again():
    while True:
        again = input("Do you want to play again? (Maybe you will discover a new story). yes/no \n").strip().lower()
        if again == "yes":
            return True
        elif again == "no":
            print("Thanks for playing!")
            return False
        else:
            print("You have to enter 'yes' or 'no'.\n ")

if __name__ == "__main__":
    while True:
        mad_libs()
        if not play_again():
            break

