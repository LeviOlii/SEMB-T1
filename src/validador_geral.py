import os
import numpy as np
import networkx as nx
import subprocess
import matplotlib.pyplot as plt

# --- Parâmetros ---
n = 89
probs = [0.01, 0.02, 0.05, 0.07, 0.10, 0.15, 0.20, 0.25]
samples_per_prob = 15
binary_path = "grafo_conexo.exe"

# Caminho absoluto para a pasta "validation_data" na raiz
base_dir = os.path.dirname(os.path.abspath(__file__))  # diretório atual (onde está o .py)
output_dir = os.path.join(base_dir, "..", "validation_data")  # sobe um nível e entra em validation_data
os.makedirs(output_dir, exist_ok=True)

results = []

def save_matrix(G, filename):
    """Salva matriz de adjacência em arquivo .txt"""
    A = nx.to_numpy_array(G, dtype=int)
    np.savetxt(filename, A, fmt="%d")

def run_c_program(path):
    """Executa o binário C e retorna True (conexo) ou False (não conexo)."""
    out = subprocess.getoutput(f"{binary_path} {path}")
    if "CONEXO" in out and "NÃO" not in out:
        return True
    return False

# --- Loop principal de teste ---
for p in probs:
    acc = []
    for i in range(samples_per_prob):
        G = nx.erdos_renyi_graph(n, p)
        expected = nx.is_connected(G)

        file_path = os.path.join(output_dir, f"grafo_p{p:.2f}_{i+1}.txt")
        save_matrix(G, file_path)

        obtained = run_c_program(file_path)
        acc.append(int(obtained == expected))
        print(f"p={p:.2f} | {file_path} | esperado={expected} | obtido={obtained}")

    accuracy = sum(acc) / len(acc)
    results.append((p, accuracy))
    print(f">> Probabilidade {p:.2f} → Acurácia: {accuracy*100:.1f}%")

# --- Plot do gráfico de acurácia ---
probs_plot = [r[0] for r in results]
acc_plot = [r[1]*100 for r in results]

plt.figure(figsize=(12,5))
plt.plot(probs_plot, acc_plot, marker="o", linewidth=2, color="royalblue")
plt.title("Acurácia: Comparação entre C e Python (is_connected)")
plt.xlabel("Probabilidade de Aresta (p)")
plt.ylabel("Acurácia (%)")
plt.ylim(0, 110)
plt.xticks(probs_plot, [f"{p:.2f}" for p in probs_plot])
plt.grid(True)
plt.tight_layout()
plt.show()
