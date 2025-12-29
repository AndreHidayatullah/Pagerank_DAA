import networkx as nx
import pandas as pd

# Membaca data interaksi kreator
data = pd.read_csv("interaksi.csv")

# Membuat graf terarah
G = nx.DiGraph()

for _, row in data.iterrows():
    G.add_edge(row["Sumber"], row["Target"])

# Menghitung PageRank
pagerank = nx.pagerank(G, alpha=0.85)

# Menampilkan hasil
print("Hasil PageRank Kreator TikTok:\n")
for node, score in sorted(pagerank.items(), key=lambda x: x[1], reverse=True):
    print(f"{node} : {score:.4f}")
