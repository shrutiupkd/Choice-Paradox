# -*- coding: utf-8 -*-
"""daprojecthousing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15IS_onsZqg3P4pf59KgycH_ez5OyQZS2
"""

import numpy as np
import pandas as pd
import io
import matplotlib.pyplot as plt

from google.colab import files
uploaded = files.upload()

data = pd.read_csv(io.BytesIO(uploaded['Mumbai1.csv']))

data.describe()

data.info()

data.head()

data = data.drop(["New/Resale","Intercom","Gas Connection","Jogging Track","Landscaped Gardens","Indoor Games","Maintenance Staff","24x7 Security","Children's Play Area"],axis =1)
data.head()



data.Price.describe()

plt.plot(data.Price);