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

# Cria caminho para pasta de imagens 
images_dir = os.path.join(base_dir, "..", "images")

results = []

def save_matrix(G, filename):
    """Salva matriz de adjacência em arquivo .txt"""
    A = nx.to_numpy_array(G, dtype=int)
    np.savetxt(filename, A, fmt="%d")

def run_c_program(path):
    """Executa o binário C e retorna True (conexo) ou False (não conexo)."""
    out = subprocess.getoutput(f"{binary_path} {path}")
    if "CONEXO" in out and "NAO" not in out:
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
    plt.savefig(os.path.join(images_dir, "acuracia_comparacao.png"))
    plt.show()

# --- Etapa 4: Geração de exemplos visuais de grafos (3D + animação) ---
imagens_existentes = any(fname.endswith(".gif") for fname in os.listdir(images_dir)) # Verifica se já existem gifs na pasta images

if not imagens_existentes:
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib.animation import FuncAnimation, PillowWriter  # ou use FFMpegWriter se quiser .mp4

    print("\n[+] Nenhuma animação encontrada. Gerando animações 3D dos grafos...")

    # Caminho para pasta de imagens (um diretório acima da pasta atual)
    images_dir = os.path.join(base_dir, "..", "images")
    os.makedirs(images_dir, exist_ok=True)

    # Exemplo de grafo não conexo (p=0.02) e conexo (p=0.10)
    for p, label in [(0.02, "nao_conexo"), (0.10, "conexo")]:
        file_path = os.path.join(output_dir, f"grafo_p{p:.2f}_1.txt")
        if not os.path.exists(file_path):
            print(f"[!] Arquivo não encontrado: {file_path}")
            continue

        archive_name = f"grafo_p{p:.2f}_1.txt"

        A = np.loadtxt(file_path, dtype=int)
        G = nx.from_numpy_array(A)

        # Identifica componentes conectadas
        components = list(nx.connected_components(G))
        largest_comp = max(components, key=len)

        # Define cores: azul para conectados, vermelho para isolados
        colors = ["royalblue" if node in largest_comp else "crimson" for node in G.nodes()]

        # Layout 3D
        pos = nx.spring_layout(G, dim=3, seed=42)

        # --- Configuração da figura 3D ---
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection="3d")
        ax.set_title(
            f"Grafo {label.upper()} (p={p:.2f})\nAzul: Conectado  Vermelho: Isolado\nArquivo: {archive_name}"
        )
        ax.set_axis_off()

        # Plot das arestas
        for u, v in G.edges():
            x = [pos[u][0], pos[v][0]]
            y = [pos[u][1], pos[v][1]]
            z = [pos[u][2], pos[v][2]]
            ax.plot(x, y, z, color="gray", alpha=0.5, linewidth=0.6)

        # Plot dos nós
        xs = [pos[node][0] for node in G.nodes()]
        ys = [pos[node][1] for node in G.nodes()]
        zs = [pos[node][2] for node in G.nodes()]
        sc = ax.scatter(xs, ys, zs, c=colors, s=25, depthshade=True)

        # --- Animação ---
        def update(angle):
            ax.view_init(elev=20, azim=angle)
            return fig,

        ani = FuncAnimation(fig, update, frames=np.linspace(0, 360, 120), interval=50, blit=False)

        # Caminho de saída do vídeo (agora dentro de ../images)
        video_path = os.path.join(images_dir, f"grafo_{label}_3d.gif")

        # Salva a animação como GIF 
        ani.save(video_path, writer=PillowWriter(fps=20))
        print(f"[+] Animação salva: {video_path}")

        plt.close(fig)
