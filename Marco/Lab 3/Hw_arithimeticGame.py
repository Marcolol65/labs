import random


def ask_question():
    n1 = random.randint(1, 9)
    n2 = random.randint(1, 9)
    correct_ans = n1 * n2
    try:
        user_ans = int(input(f'What is {n1} multiplied by {n2}?'))
    except ValueError:
        print(" Stick to numbers please!")
    return user_ans == correct_ans, correct_ans


def main():
    correct_count = 0
    consecutive_correct = 0
    consecutive_incorrect = 0

    print('Let\'s test your multiplication skills!!')

    while correct_count < 5:
        is_correct, correct_answer = ask_question()

        if is_correct:
            correct_count += 1
            consecutive_correct += 1
            consecutive_incorrect = 0
            print('Correct!')
            if consecutive_correct == 3:
                print('You just did 3 in a row... wow')
        else:
            consecutive_correct = 0
            consecutive_incorrect += 1
            print(f'Nop, the correct answer is {correct_answer}')
            if consecutive_incorrect == 3:
                print('You are kind of dumb... but keep trying!')

    print('You answered 5 questions correctly')


if __name__ == '__main__':
    main()
