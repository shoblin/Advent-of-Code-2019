#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     24.12.2020
# Copyright:   (c) atopolskiy 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    with open('data/day6_puzzle_input.txt', 'r') as file:
        question = []
        questions = []
        for line in file:
            line = line.strip()

##            print(line)
            if line:
                question.append(line)
            else:
                questions.append(question)
                question = []

    questions.append(question)

    result1 = 0
    for question in questions:
        answer = ''
        for smb in question:
            answer += smb
        result1 += len(set(answer))
##        print(question, result)
    print(result1)

    result2 = 0
    for question in questions:

        same_answers = question[0]
        for answer in question:
            same_answers = list(set(same_answers) & set(answer))

        result2 += len(same_answers)
    print(result2)

if __name__ == '__main__':
    main()
