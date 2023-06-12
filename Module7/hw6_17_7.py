def solve_riddle(riddle, word_length, start_letter, reverse=False):

    if reverse:
        num_start = riddle.find(start_letter)
        start = num_start - len(riddle)
        print(start)
        end = start - word_length
        word = riddle[start:end:-1]
        return word
    if not reverse:
        num_start = riddle.find(start_letter)
        # print(num_start)
        end = num_start+word_length
        word = riddle[num_start:end:1]
        return word


riddle = 'mi1powrepret'
word_length = 3
start_letter = 'r'
# rebus = 'power'

print(solve_riddle(riddle, word_length, start_letter))
