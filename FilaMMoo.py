import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da fila
taxa_chegada = 5  # Taxa média de chegada (clientes por unidade de tempo)
taxa_servico = 3  # Taxa média de serviço (clientes atendidos por unidade de tempo)
tempo_simulacao = 10  # Tempo total de simulação

def gerar_tempos_de_chegada(taxa_chegada, tempo_total):
    return np.cumsum(np.random.exponential(1 / taxa_chegada, int(taxa_chegada * tempo_total * 1.5)))

def gerar_tempos_de_servico(taxa_servico, n_clientes):
    return np.random.exponential(1 / taxa_servico, n_clientes)

def simular_fila_mm_inf(taxa_chegada, taxa_servico, tempo_simulacao):
    tempos_de_chegada = gerar_tempos_de_chegada(taxa_chegada, tempo_simulacao)
    tempos_de_chegada = tempos_de_chegada[tempos_de_chegada <= tempo_simulacao]
    n_clientes = len(tempos_de_chegada)
    tempos_de_servico = gerar_tempos_de_servico(taxa_servico, n_clientes)

    tempos_inicio_servico = tempos_de_chegada
    tempos_fim_servico = tempos_inicio_servico + tempos_de_servico

    return tempos_inicio_servico, tempos_fim_servico, n_clientes, tempos_de_chegada, tempos_de_servico

def plotar_simulacao(tempos_inicio_servico, tempos_fim_servico, n_clientes):
    plt.figure(figsize=(10, 6))
    for i in range(n_clientes):
        plt.plot([tempos_inicio_servico[i], tempos_fim_servico[i]], [i, i], 'bo-', markersize=5)
    plt.xlabel('Tempo')
    plt.ylabel('Clientes')
    plt.title('Simulação de uma Fila M/M/∞')
    plt.grid(True)
    plt.show()

def plotar_probabilidade_clientes(ρ):
    def Pn(n, ρ):
        return (np.exp(-ρ) * ρ**n) / np.math.factorial(n)
    
    n_values = np.arange(0, 20)
    Pn_values = [Pn(n, ρ) for n in n_values]

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, Pn_values, 'o-', label='Pn(ρ)')
    plt.xlabel('Número de Clientes (n)')
    plt.ylabel('Probabilidade (Pn)')
    plt.title('Probabilidade de Existirem n Clientes no Sistema (Pn) em Função da Taxa de Ocupação (ρ)')
    plt.legend()
    plt.grid(True)
    plt.show()

def plotar_numero_medio_clientes(ρ_values):
    Ls_values = [ρ for ρ in ρ_values]

    plt.figure(figsize=(10, 6))
    plt.plot(ρ_values, Ls_values, label='Ls(ρ)')
    plt.xlabel('Taxa de Ocupação (ρ)')
    plt.ylabel('Número Médio de Clientes no Sistema (Ls)')
    plt.title('Número Médio de Clientes no Sistema (Ls) em Função da Taxa de Ocupação (ρ)')
    plt.legend()
    plt.grid(True)
    plt.show()

def plotar_tempo_medio_espera(μ_values):
    Ws_values = [1 / μ for μ in μ_values]

    plt.figure(figsize=(10, 6))
    plt.plot(μ_values, Ws_values, label='Ws(μ)')
    plt.xlabel('Taxa de Serviço (μ)')
    plt.ylabel('Tempo Médio de Espera no Sistema (Ws)')
    plt.title('Tempo Médio de Espera no Sistema (Ws) em Função da Taxa de Serviço (μ)')
    plt.legend()
    plt.grid(True)
    plt.show()

tempos_inicio_servico, tempos_fim_servico, n_clientes, tempos_de_chegada, tempos_de_servico = simular_fila_mm_inf(taxa_chegada, taxa_servico, tempo_simulacao)
plotar_simulacao(tempos_inicio_servico, tempos_fim_servico, n_clientes)

print(f"Total de clientes atendidos: {n_clientes}")
print(f"Tempos de chegada dos clientes: {tempos_de_chegada}")
print(f"Tempos de serviço dos clientes: {tempos_de_servico}")

np.random.seed(42)

λ = np.random.uniform(10, 100)
μ = np.random.uniform(5, 20)
ρ = λ / μ

plotar_probabilidade_clientes(ρ)
ρ_values = np.linspace(0.1, 5, 100)
plotar_numero_medio_clientes(ρ_values)
μ_values = np.linspace(5, 50, 100)
plotar_tempo_medio_espera(μ_values)
