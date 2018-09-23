word = "Christian"
guess = ""
count = 0
limit = 5
time_out = False

while guess != word and not(time_out):
    if count < limit and not(time_out):
        print("Clue: To be associated with Jesus Christ !")
        guess = input("guess a word: ")
        count += 1
    else:
        time_out = True
    

if time_out:
    print("Sorry You lost!")
else:
    print("CONGRATULATIONS!!!")