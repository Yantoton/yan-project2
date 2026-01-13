program_ing = ['python','java','','ruby','c+']

for program in program_ing:
   if program == '':
    program = program.replace('','c#')
   print(f'name of language: {program}')
