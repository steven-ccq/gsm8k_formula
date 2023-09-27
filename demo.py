import re
import json

def solution(question_variable, answer_variable, equation_variable, input_nums):
    var_list = re.findall(r'x[0-9]+', question_variable)
    input_nums = [str(num) for num in input_nums]
    if len(var_list) != len(input_nums):
        print('the number of input is incorrect')
        return '', '', ''
    var_num_dict = dict(zip(var_list, input_nums))
    question = question_variable
    answer = answer_variable
    equation = equation_variable
    for var, num in var_num_dict.items():
        question = re.sub(var, num, question)
        answer = re.sub(var, num, answer)
        equation = re.sub(var, num, equation)
    equation = re.sub(r'x', r'*', equation)
    try:
        # res = eval(equation)
        res = int(eval(equation))
    except Exception as e:
        res = ''
    return question, answer, res

if __name__ == '__main__':
    """{
    'question': original question,
    'answer': original answer,
    'question_variable': parameterization question,
    'answer_variable': parameterization answer,
    'equation_variable': formula
    }
    """
    with open('./gsk8k_var.json', 'r+', encoding='utf-8') as f:
        data_list = [json.loads(_) for _ in f.readlines()]

    data = data_list[0]
    print('question_template:')
    print(data['question_variable'])
    var_num = data['var_num']
    input_nums = []
    for i in range(var_num):
        input_nums.append(input('x{}='.format(i+1)))
    question, answer, res = solution(data['question_variable'], data['answer_variable'], data['equation_variable'], input_nums)
    
    print('question:')
    print(question)
    print('answer')
    print('#### ', res)