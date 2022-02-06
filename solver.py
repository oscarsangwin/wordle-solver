from words import words
from datetime import date

def get_word(puzzle_date):
    diff = puzzle_date - date(2021, 6, 19)
    index = diff.days
    return words[index]

def get_today_word():
    return get_word(date.today())

if __name__ == '__main__':
    print(f'Today\'s word: {get_today_word()}')
    print(f'Word for Fri 5th Feb: {get_word(date(2022, 2, 5))}')