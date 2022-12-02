# %%
import pandas as pd

n = 'Day_2.txt'

df= pd.read_csv(n,names= ['Rounds'])

            ## A X= 1 = rock
            ## B Y= 2 = Paper
            ## C Z= 3 = Scisors
            ## 0 = loss
            ## 3 = win


gameresult = {
    'A X' : 4,
    'A Y' : 8,
    'A Z' : 3,
    'B X' : 1,
    'B Y' : 5,
    'B Z' : 9,
    'C X' : 7,
    'C Y' : 2,
    'C Z' : 6,
    
}

df['result']=df['Rounds'].map(gameresult)

print(df['result'].sum())


