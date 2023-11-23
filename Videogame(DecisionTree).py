
from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

players= read_csv('data/giocatori.csv')
X=players.drop(columns=['videogame'])
y= players['videogame']

model= DecisionTreeClassifier()
print("La versione è ancora in alpha")
print("Vediamo cosa regalare a Natale: ")

a=int(input("Scegli il genere, 0 per F e 1 per M: "))
b=int(input("Quanti anni ha la persona?: "))

model.fit(X.values, y.values)
prediction = model.predict([[a,b]])
print(f'Questo è il tuo risultato. Considerando che ha {b} anni direi che potresti regalare un gioco di {prediction}') 
