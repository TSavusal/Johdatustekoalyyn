import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

def drawBarDiagram(labels, predict_probs):
    """
    Tämä funktio piirtää pylväsdiagrammin luokkien ja todennäköisyyksien mukaan annetulle testinäytteelle.
    """
    elements = list(set(labels))
    elements.sort()
    for i in range(len(predict_probs)):
        print(" The class {} has propability: {:.3f}%".format(elements[i], predict_probs[i]*100))
    x = range(len(predict_probs))
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.bar(x, predict_probs, align="center")
    ax.set_xticks(x)
    ax.set_xticklabels(elements)
    plt.title("Predicted propabilities for individual sample")
    plt.ylabel("Propabilities")
    plt.xlabel("Classes")
    plt.show()

def main():
    data = []
    labels = []
    with open('data3_wine.csv') as csvfile: # Ladataan datajoukko .csv tiedostosta (vakiona wines datajoukko)
        reader = list(csv.reader(csvfile, delimiter=';'))
    for i in range(len(reader)):
        labels.append(int(reader[i][0]))
        data.append(reader[i][1:])
    data = np.asarray(data).astype(float)
    #-------TÄHÄN SINUN KOODI--------
    
    
    #--------------------------------
	
if __name__ == '__main__':
    main()