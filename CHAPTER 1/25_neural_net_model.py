import numpy as np

def sigmoid(x): return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x): return x * (1 - x)

inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
expected = np.array([[0],[1],[1],[0]])

weights = np.random.rand(2,1)
for _ in range(10000):
    output = sigmoid(np.dot(inputs, weights))
    error = expected - output
    weights += np.dot(inputs.T, error * sigmoid_derivative(output))

print(sigmoid(np.dot(inputs, weights)))