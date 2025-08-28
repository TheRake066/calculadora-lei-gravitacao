# Calculadora da Lei da Gravitação Universal
import time

from colorama import Fore, Style

print("=== CALCULADORA DA FORÇA GRAVITACIONAL ===")
print("Fórmula: Fg = GMm / d²")
print("(A constante G já está definida no sistema)\n")

G = 6.67e-11

def printd(texto, delay=0.03):
    for c in texto:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()

def capturar_valor_cientifico(nome_variavel, unidade):
    print(f"\n--- {nome_variavel} ---")
    numero = float(input(f"Digite o número base (ex: 6.10): "))
    expoente = int(input(f"Digite o expoente (ex: 24 ou -11): "))
    valor = numero * (10 ** expoente)
    print(f"Valor inserido: {numero} × 10^{expoente} {unidade} = {valor:.2e} {unidade}")
    return valor

printd("Digite os componentes em notação científica:")

M = capturar_valor_cientifico("Massa do corpo maior (M)", "kg")
m = capturar_valor_cientifico("Massa do corpo menor (m)", "kg")

printd(f"\n--- Distâncias ---")
printd("Para calcular a distância total:")
raio_num = float(input("Digite o número base do raio (ex: 6.4): "))
raio_exp = int(input("Digite o expoente do raio (ex: 6 para 10^6): "))
raio = raio_num * (10 ** raio_exp)
print(f"Raio: {raio_num} × 10^{raio_exp} m = {raio:.2e} m = {raio/1000:.0f} km")

altura_num = float(input("Digite o número base da altura/distância (ex: 1.6): "))
altura_exp = int(input("Digite o expoente da altura (ex: 6 para 10^6): "))
altura = altura_num * (10 ** altura_exp)
print(f"Altura: {altura_num} × 10^{altura_exp} m = {altura:.2e} m = {altura/1000:.0f} km")

printd("\n" + "="*60)
printd("DADOS INSERIDOS:")
print(f"G (constante gravitacional) = {G} N⋅m²/kg²")
print(f"M (massa maior) = {M:.2e} kg")
print(f"m (massa menor) = {m:.2e} kg")
print(f"Raio = {raio:.2e} m ({raio/1000:.0f} km)")
print(f"Altura = {altura:.2e} m ({altura/1000:.0f} km)")
print("="*60)

d = raio + altura
printd(f"\nCálculo da distância total (d):")
print(f"d = raio + altura")
print(f"d = {raio:.2e} + {altura:.2e} = {d:.2e} m")
print(f"d = {d/1000:.0f} km")

print(f"\nAplicando fórmula Fg = GMm / d²:")
print(f"Fg = ({G}) × ({M:.2e}) × ({m:.2e}) / ({d:.2e})²")

numerador = G * M * m
denominador = d**2
Fg = numerador / denominador

printd("\nCálculo passo a passo:")
print(f"Numerador (GMm) = {numerador:.3e}")
print(f"Denominador (d²) = {denominador:.3e}")
print(f"Fg = {numerador:.3e} / {denominador:.3e}")

printd("\n" + "="*60)
printd("RESULTADO FINAL:")
printd(f"{Fore.BLUE}Força gravitacional (Fg) = {Fg:.3e} N{Style.RESET_ALL}")
printd(f"{Fore.BLUE}Força gravitacional (Fg) = {Fg:.0f} N{Style.RESET_ALL}")

if Fg >= 1000:
    potencia = len(str(int(Fg))) - 1
    coeficiente = Fg / (10 ** potencia)
    print(f"Em notação científica: {coeficiente:.2f} × 10^{potencia} N")
print("="*60)