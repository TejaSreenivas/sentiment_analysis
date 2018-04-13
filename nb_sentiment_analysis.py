import pandas as pd
import nltk
from nltk.corpus import stopwords

#reading file from traindata text file
df=pd.read_csv("traindata.txt",sep="\t",names=['sentiment','text'])
print(df.head())
