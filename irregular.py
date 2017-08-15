import json
import random

file = open("irregular.json", "r")
irr_dict = json.loads(file.read())
file.close()
user_input = ""
print "Enter 'exit' or 'save' to exit from program."


def exits(answer):
    if answer == "exit" or answer == "save":
        file = open("irregular.json", "w")
        json.dump(irr_dict, file)
        file.close()
        print "Exiting."
        exit(0)


def get_user_input(form):
    answer = raw_input("{}  Enter {} form of _{}_ word: ".format(frequency, form, infinitive))
    exits(answer)
    return answer


def correct(word):
    correct_word = ""
    if type(word) == list:
        for part in word:
            correct_word += " {}".format(part)
    else:
        correct_word = word

    if user_input in correct_word:
        irr_dict[infinitive]['frequency'] = str(int(frequency) - 1)
        return True
    else:
        irr_dict[infinitive]['frequency'] = str(int(frequency) + 1)
        print "Correct forms: {}  {}  {}".format(
            infinitive,
            irr_dict[infinitive]['past'],
            irr_dict[infinitive]['participles'])
        print ""
        return False


while True:
    infinitive = random.choice(irr_dict.keys())
    frequency = irr_dict[infinitive]['frequency']
    if int(frequency) < 0: continue
    for tense in ['past', 'participles']:
        user_input = get_user_input(tense)
        if not correct(irr_dict[infinitive][tense]): break
