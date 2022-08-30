import pickle

with open(f'survey_result/이서현님', 'rb') as fr:
    p = pickle.load(fr)

print('이서현\n', p,'\n\n')

with open(f'survey_result/김기현님', 'rb') as fr:
    p = pickle.load(fr)

print('김기현\n', p,'\n\n')

with open(f'survey_result/문지훈님', 'rb') as fr:
    p = pickle.load(fr)

print('문지훈\n', p,'\n\n')

with open(f'survey_result/권희경', 'rb') as fr:
    p = pickle.load(fr)

print('권희경\n', p,'\n\n')

with open(f'survey_result/이영채', 'rb') as fr:
    p = pickle.load(fr)

print('이영채\n', p,'\n\n')

