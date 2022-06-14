secret_word = "dolphin"
guess = ""
guess_count = 1
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count <= guess_limit:
        guess = input("Enter guess :")
        guess_count +=1
    else:
        out_of_guesses = True

if out_of_guesses is True:
    print("You Lose")
else:
    print("You Win!")