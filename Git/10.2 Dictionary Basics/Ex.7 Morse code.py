letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
         '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
         '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

morse_dict = dict([letters[i], morse[i]] for i in range(len(letters)))

for i in tuple(input().upper()):
    for key in morse_dict:
        if i == key:
            print(morse_dict[key], end=' ')
            break