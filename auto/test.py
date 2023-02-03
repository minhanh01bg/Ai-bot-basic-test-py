import numpy as np

mask = np.random.rand(len(df)) =< 0.8
training_data = df[mask]
testing_data = df[~mask]

print(f"No. of training examples: {training_data.shape[0]}")
print(f"No. of testing examples: {testing_data.shape[0]}")

# No. of training examples: 125
# No. of testing examples: 25