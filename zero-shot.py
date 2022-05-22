import openai 
import json
import pandas as pd

openai.api_key = "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" #given by OpenAI
courses = ['18.01', '18.02', '18.03', '6.042', '18.05', '18.06', 'COMS3251']
questions_per_course = 20

#make csv files for each course
#put in course id, original question, and codex input. Then prompt gpt-3 and codex for all the columns.
#make column that indicates if the question is solved by zero-shot learning. if not we will continue to few-shot.py

#makes input for each prompt
front_piece = "\"\"\"\n"  #these two lines add triple quotes to the prompt like a doc string
back_piece = "\n\"\"\""
context = 'Write a program, using numpy, sympy and other python libraries, that answers the following question: '


#makes CSV's for each course:
for course in courses:
    questions = []
    for num in [i for i in range(1, questions_per_course+1)]:
        with open(f'./Data/{course}/{course}_Question_{num}.json', 'r') as f:
            data = json.load(f)
        raw_question = data['Original question']
        questions.append(raw_question)
    # entries = [[i+1,questions[i],front_piece+context+questions[i]+back_piece] for i in range(questions_per_course)]
    entries = [[i+1,questions[i],'''"""\n'''+context+questions[i]+'''\n"""\n'''] for i in range(questions_per_course)]

    info = pd.DataFrame(entries, columns=['Question', 'Original Question', 'Codex Input'])
    info.to_csv(course+'.csv', index=False)
