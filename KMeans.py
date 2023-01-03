import matplotlib.pyplot as plt
import KMeans
from sklearn.cluster import KMeans

X = [4,5,10,4,3,11,14,6,10,12,2,4,5,10,12,13,9,8,7,11]
Y = [21,19,24,17,16,25,24,22,21,21,16,15,17,18,20,21,21,15,19,18]

data = list(zip(X,Y))
print(data)

inertias = []
for i in range(1,21):
    Kmeans = KMeans(n_clusters=i)
    Kmeans.fit(data)
    inertias.append(Kmeans.inertia_)
plt.plot(range(1,21),inertias, marker='o')
plt.title("Elbow Method")
plt.xlabel("No of clusters.")
plt.ylabel("Inertia")
plt.show()
Kmeans = KMeans(n_clusters=2)
Kmeans.fit(data)
plt.scatter(X,Y,c=Kmeans.labels_)
plt.show()






