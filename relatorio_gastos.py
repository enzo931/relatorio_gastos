import matplotlib.pyplot as plt

print("💰 === Relatório de Gastos Mensais ===")

gastos = []

# Coleta de dados de gastos
while True:
    nome = input("Digite o nome do gasto (ou 'sair' para finalizar): ")
    if nome.lower() == 'sair':
        break

    try:
        valor = float(input(f"Digite o valor de '{nome}': R$ "))
        gastos.append({'nome': nome, 'valor': valor})
    except ValueError:
        print("❌ Valor inválido! Digite um número.")

# Exibição do relatório
print("\n📊 --- Relatório Final ---")
total = 0
nomes = []
valores = []

for gasto in gastos:
    print(f"- {gasto['nome']}: R$ {gasto['valor']:.2f}")
    total += gasto['valor']
    nomes.append(gasto['nome'])
    valores.append(gasto['valor'])

print(f"\n🧾 Total de gastos: R$ {total:.2f}")

# Escolha do tipo de gráfico
print("\n📈 --- Escolha o tipo de gráfico ---")
print("1. Gráfico de Pizza")
print("2. Gráfico de Barras")
print("3. Gráfico de Setores")
escolha = input("Digite o número correspondente ao gráfico desejado: ")

# Função para salvar o gráfico
def salvar_grafico():
    salvar = input("Deseja salvar o gráfico como imagem? (s/n): ")
    if salvar.lower() == 's':
        nome_arquivo = input("Digite o nome do arquivo (sem extensão): ")
        plt.savefig(f"{nome_arquivo}.png")  # Salva como PNG
        print(f"✅ Gráfico salvo como {nome_arquivo}.png")

# Criação do gráfico com base na escolha
if escolha == '1':
    plt.figure(figsize=(6, 6))
    cores = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ffb3e6']  # Cores personalizadas
    plt.pie(valores, labels=nomes, autopct='%1.1f%%', startangle=90, colors=cores)
    plt.title('Distribuição dos Gastos Mensais')
    plt.axis('equal')  # Deixa o gráfico circular
    salvar_grafico()
    plt.show()

elif escolha == '2':
    plt.figure(figsize=(8, 6))
    cores = ['#ff6347', '#ff7f50', '#8a2be2', '#00fa9a', '#ff1493']  # Cores vibrantes para barras
    plt.bar(nomes, valores, color=cores)
    plt.title('Gastos Mensais por Categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Valor (R$)')
    salvar_grafico()
    plt.show()

elif escolha == '3':
    plt.figure(figsize=(8, 6))
    plt.fill_between(nomes, valores, color='skyblue', alpha=0.7)
    plt.plot(nomes, valores, color='darkblue', linewidth=2)  # Destaque na linha
    plt.title('Distribuição dos Gastos Mensais (Setores)')
    plt.xlabel('Categoria')
    plt.ylabel('Valor (R$)')
    salvar_grafico()
    plt.show()

else:
    print("❌ Opção inválida! Digite 1, 2 ou 3.")

