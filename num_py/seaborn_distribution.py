import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

sns.displot([0, 1, 2, 3, 4, 5])


#normal distribution (local ,scale , size)
n_d=random.normal(loc=1,scale=4,size=(3,4))
sns.displot(n_d)
plt.show()

#binomial distribution(n.p,size)
b_d=random.binomial(n=10,p=0.6,size=(2,3))

