guess_word="giraffe"
word = ""
count=0
limit=3
out_of_guesses=False

while word!=guess_word and not out_of_guesses:
    if count<limit:
        word=input("Your guess= ")
        count+=1
    else:    
        out_of_guesses = True


if out_of_guesses:
    print("Out of guesses")
else:
    print("You win!!!")