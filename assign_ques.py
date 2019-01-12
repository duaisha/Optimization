import numpy as np
import pandas as pd
import random

def get_assignQues(student_list, OM_ques_list, quesTypes, quesVar):
    
    students = pd.read_csv(student_list).values
    questions = pd.read_csv(OM_ques_list).values[:,1:]
    for i in range(quesTypes):
        temp = []
        for j in range(len(students)):
            temp.append(questions[i,random.randint(0,quesVar-1)])
        students = np.concatenate((students, np.array(temp).reshape(len(temp),1)), axis =1)
    data = pd.DataFrame(students)
    data.to_csv('assign_ques.csv', sep='\t', header =False, index=False)
    
get_assignQues('studentlist_final.csv', 'OM_queslist_final.csv', quesTypes = 2, quesVar = 4)
