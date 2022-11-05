import numpy as np


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


b = np.array([0.3, 2.9, 4.0])
z = softmax(b)
print(z)
z1 = np.sum(z)
print(z1)

