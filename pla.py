import numpy as np
import matplotlib.pyplot as plt

def pla(x, y):
    
    w = np.array([0, 0, 0])
    converged = False   

    while not converged:

        output = X @ w
        sign = np.sign(output)
        
        # Find all misclassified points
        misclassified = np.where(sign != y)[0]

        # If there are no misclassified points, pla has converged
        if len(misclassified) == 0:
            converged = True
            continue
        
        # Pick a random misclassified point
        index = np.random.randint(0, len(misclassified))
        w = w + y[misclassified][index]*X[misclassified][index] 
    
    if w[1] == 0:
        x = w[2] * np.ones(100) 
        y = np.linspace(-1, 1, 100)
    else:
        x = np.linspace(-1, 1, 100)
        y = -w[0]/w[1]*x + w[2]

    plt.scatter(X[:, 0], X[:, 1], c=Y, cmap='viridis')
    plt.plot(x, y)
    plt.show()
    

if __name__ == "__main__":

    X = np.array([[1, 1, 1], [1, -1, 1], [-1, 1, 1], [-1, -1, 1]])
    Y = np.array([1, -1, 1, -1])

    pla(X, Y)