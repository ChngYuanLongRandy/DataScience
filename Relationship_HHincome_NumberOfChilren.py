import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from sklearn.feature_extraction.text import CountVectorizer

# Reading the downloaded content and turning it into a pandas dataframe
url = "https://github.com/ChngYuanLongRandy/DataScience/blob/main/Stats%20From%20Singstat.xlsx?raw=true"

df = pd.read_excel(url)

df.head()