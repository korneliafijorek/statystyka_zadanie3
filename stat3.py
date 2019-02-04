#Zadanie 3 - Zadanie 2 w wersji z Github'em#
#Kornelia Fijorek 167865#

#https://realpython.com/python-histograms/

# Importujemy potrzebne biblioteki #
import numpy as np
from scipy import stats as st
import pandas as pd
import seaborn as sns
from numpy import array
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

# Deklarujemy zmienne - możemy tutaj zmieniać ich wartości #
r = 1000
# Rozkład Normalny:
mu_n = 0
sigma_n = 1
n = r

# Rozkład Gamma:
shape = 2
scale = 1
size = r

#zaburzany wektor
s = np.random.normal(mu_n, sigma_n, n)
#zaburzający wektor
w = np.random.gamma(shape, scale, int(size))

new_s = list(s)
t = list(w)

print("Ile elementów chcesz dodać? \n")
x = input()
#dodawanie elementów do wektora
for i in range(0,int(x)):
    new_s.append(t[i])

#Średnia
srd_1 = sum(s)/len(s)
srd_2 = sum(new_s)/len(new_s)

# Test Shapiro-Wilka <0.05
p_S = st.shapiro(s)
print("Test 1: ",p_S)
p_S2 = st.shapiro(new_s)
print("Test 2: ",p_S2)
print("\n Średnia 1: ", srd_1)
print("\n Średnia 2, po dodaniu ",i+1," elementów: ", srd_2,"\n")

#zamień na array z powrotem xD
new_s = array(new_s)


#Rysowanie histogramu#
data1 = {'vector':s}
data2 ={'new_vec':new_s}
data1 = pd.DataFrame(data1)
data2 = pd.DataFrame(data2)
#performs a test of the
#distribution G(x) of an observed random variable
#against a given distribution F(x).
#Under the null hypothesis the two distributions are identical,
#G(x)=F(x).
print(st.kstest(s, "expon"))
print(st.kstest(new_s, "expon"))

sns.set()
# sns.displot - rysuje dystrybuantę
sns.distplot(data1['vector'],axlabel='',label='pierwszy',color='green')
sns.distplot(data2['new_vec'],axlabel='',label='nowy',color='crimson');
plt.legend(ncol=1, loc='upper right');

plt.show()
