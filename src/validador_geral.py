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

# Caminho absoluto para a pasta "validation_data" na raiz do projeto
base_dir = os.path.dirname(os.path.abspath(__file__))  # diretório do script atual
output_dir = os.path.join(base_dir, "..", "validation_data")
os.makedirs(output_dir, exist_ok=True)

results = []

def save_matrix(G, filename):
    """Salva matriz de adjacência em arquivo .txt"""
    A = nx.to_numpy_array(G, dtype=int)
    np.savetxt(filename, A, fmt="%d")

def run_c_program(path):
    """Executa o binário C e retorna True (conexo) ou False (não conexo)."""
    out = subprocess.getoutput(f"{binary_path} {path}")
    if "CONEXO" in out and "NAO" not in out and "NÃO" not in out:
        return True
    return False

# --- Etapa 1: verificar se os grafos já existem ---
arquivos_existentes = any(fname.endswith(".txt") for fname in os.listdir(output_dir))

if not arquivos_existentes:
    print("[+] Nenhum grafo encontrado. Gerando novos arquivos .txt...")
    for p in probs:
        for i in range(samples_per_prob):
            G = nx.erdos_renyi_graph(n, p)
            file_path = os.path.join(output_dir, f"grafo_p{p:.2f}_{i+1}.txt")
            save_matrix(G, file_path)
    print("[+] Geração concluída!")
else:
    print("[-] Grafos já existentes encontrados. Nenhum novo arquivo será gerado.")

# --- Etapa 2: Teste e comparação C x Python ---
for p in probs:
    acc = []
    for i in range(samples_per_prob):
        file_path = os.path.join(output_dir, f"grafo_p{p:.2f}_{i+1}.txt")

        # Se o arquivo não existir (caso falte algum), pula esse teste
        if not os.path.exists(file_path):
            print(f"[!] Arquivo ausente: {file_path}")
            continue

        A = np.loadtxt(file_path, dtype=int)
        G_loaded = nx.from_numpy_array(A)
        expected = nx.is_connected(G_loaded)
        obtained = run_c_program(file_path)
        acc.append(int(obtained == expected))
        print(f"p={p:.2f} | esperado={expected} | obtido={obtained}")

    if acc:
        accuracy = sum(acc) / len(acc)
        results.append((p, accuracy))
        print(f">> Probabilidade {p:.2f} → Acurácia: {accuracy*100:.1f}%")

# --- Etapa 3: Plot do gráfico de acurácia ---
if results:
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
