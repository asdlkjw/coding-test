
import pandas as pd

stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 5

answer = [0]*N
stages = pd.DataFrame(stages, columns = ['stages'])

stages['stages'] = stages.sort_values(by= 'stages')

print(stages.pivot_table(

print(stages['stages'].sort_values().unique())