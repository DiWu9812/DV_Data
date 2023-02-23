# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
# os.remove('/kaggle/working/US_Accidents_2021_11.csv')      
# os.remove('/kaggle/working/US_Accidents_2021_1015.csv')    

data = pd.read_csv('/kaggle/input/us-accidents/US_Accidents_Dec21_updated.csv')
col = data.columns
print(col)
data = data.to_numpy()[1:]

res = []
for line in data:
    if line[2] < "2017":
        res.append(line)
        
df2 = pd.DataFrame(data=res,columns=col)
df2.to_csv('US_Accidents_2016.csv')


# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
