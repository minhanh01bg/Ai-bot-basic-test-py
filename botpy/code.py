# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(10,4),
#  columns=list('ABCD'))
# print(df)


# import pandas as pd
# data = {'name': ['Janet', 'Nad', 'Timothy', 'June', 'Amy'],
#  'year': [2012, 2012, 2013, 2014, 2014],
#  'reports': [6, 13, 14, 1, 7]}
# df = pd.DataFrame(data, index =
#  ['Singapore', 'China', 'Japan', 'Sweden', 'Norway'])
# print(df)

# import matplotlib.pyplot as plt
# 
# plt.plot(
#  [1,2,3,4,5,6,7,8,9,10],
#  [2,4.5,1,2,3.5,2,1,2,3,2]
# )

import pandas as pd

df = pd.DataFrame([2,5,67,2,3,5,23,124])
df.hist() 

# %%
