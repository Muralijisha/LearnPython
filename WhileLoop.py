secret_number = 8
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    number = int(input("Guess(1-9): "))
    guess_count += 1
    if number == secret_number:
        print("You Win")
        break
else:
    print("Exceeded 3 Attempts --- YOU FAILED")