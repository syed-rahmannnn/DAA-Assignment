import numpy as np

def step(x): return 1 if x > 0 else 0

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0, 0, 0, 1])
w = np.zeros(2)
b = 0
lr = 0.1

for _ in range(10):
    for xi, target in zip(X, y):
        z = np.dot(w, xi) + b
        pred = step(z)
        error = target - pred
        w += lr * error * xi
        b += lr * error

print("Weights:", w, "Bias:", b)