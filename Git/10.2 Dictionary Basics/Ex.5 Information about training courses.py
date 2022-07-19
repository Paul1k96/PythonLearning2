course_dict = {'CS101':('3004', 'Хайнс', '8:00'),
               'CS102':('4501', 'Альварадо', '9:00'),
               'CS103':('6755', 'Рич', '10:00'),
               'NT110':('1244', 'Берк', '11:00'),
               'CM241':('1411', 'Ли', '13:00')}
inp_key = input()
for key in course_dict:
    if inp_key == key:
        print(f'{key}:', ', '.join(course_dict[key]))
        break