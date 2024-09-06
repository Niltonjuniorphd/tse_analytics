from sklearn import cluster

df = pd.read_csv('data.csv')

X = df[['clumn1','column2']]

model = cluster.KMeans(n_clusters=3)
model.fit(X)

df['cluster_label'] = model.labels_