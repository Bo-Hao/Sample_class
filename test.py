import numpy as np 

def relu(x):
    ans = []
    for i in x:
        ans.append(max(0, i))
    return ans 
def sigmoid(x):
    ans = []
    for i in x:
        ans.append(round(1/(1+ np.exp(-i)), 3))
    return ans

def softmax(x):
    x = np.array(x)
    dominator = sum(np.exp(x))
    ans = np.exp(x)/dominator
    a = [round(i, 4) for i in ans] 
    return a

def cross_entropy(x, y):
    ans = 0
    for i in range(len(x)):
        elt = y[i]*np.log(x[i]) + (1 - y[i])*np.log(1 - x[i])
        ans += elt
    
          
    return round(ans*(-1/len(x)), 6)  
def deri_cross_entropy(Oout, y):
    Oout, y = np.array(Oout), np.array(y)
    ans = -(y * (1 / Oout) + (1 - y) * (1 / (1/(1-Oout))))
    return ans

def deri_softmax(oin, oout):
    
    ans = (np.exp(oin)*(sum(np.exp(oin))-np.exp(oin)))/(sum(np.exp(oin)))**2
    return ans 

y = np.array([1, 0, 0])
b = np.array([1, 1, 1]) 
Input = np.array([0.1, 0.2, 0.7])
wij = np.array([[0.1, 0.2, 0.3], [0.3, 0.2, 0.7], [0.4, 0.3, 0.9]])
wjk = np.array([[0.2, 0.3, 0.5], [0.3, 0.5, 0.7], [0.6, 0.4, 0.8]])
wkl = np.array([[0.1, 0.4, 0.8], [0.3, 0.7, 0.2], [0.5, 0.2, 0.9]])

h1out = np.dot(Input, wij)+b
h2in = np.dot(h1out, wjk)+b
h2out = sigmoid(h2in)
oin = np.dot(h2out, wkl)+b
oout = softmax(oin)
error = cross_entropy(oout, y)

print(h1out)
print(h2in)
print(h2out)
print(oin)
print(oout)
print(error)

print(deri_cross_entropy(oout, y))
print(deri_softmax(oin, oout))

