# 🌍 Calculadora da Lei da Gravitação Universal

Uma calculadora interativa em Python para calcular a força gravitacional entre dois corpos usando a **Lei da Gravitação Universal de Newton**.

## 🚀 Fórmula Utilizada

```
Fg = G × M × m / d²
```

Onde:
- **Fg** = Força gravitacional (Newton)
- **G** = Constante gravitacional (6.67 × 10⁻¹¹ N⋅m²/kg²)
- **M** = Massa do corpo maior (kg)
- **m** = Massa do corpo menor (kg)
- **d** = Distância entre os centros dos corpos (m)

## ✨ Funcionalidades

- 🔢 **Entrada em notação científica**: Facilita trabalhar com valores astronômicos
- 🎨 **Interface colorida**: Usando colorama para melhor visualização
- ⌨️ **Efeito de digitação**: Apresentação dinâmica dos resultados
- 📊 **Cálculo detalhado**: Mostra todos os passos do cálculo
- 🌐 **Conversões automáticas**: Metros para quilômetros
- 📐 **Múltiplos formatos**: Notação científica e decimal

## 🛠️ Como usar

### Pré-requisitos
- Python 3.6 ou superior
- pip (gerenciador de pacotes)

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/calculadora-gravitacional.git
   cd calculadora-gravitacional
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a calculadora:**
   ```bash
   python calculadora_gravitacional.py
   ```

## 💫 Exemplos de uso

### Exemplo 1: Terra e Lua
```
Massa da Terra: 5.97 × 10²⁴ kg
Massa da Lua: 7.35 × 10²² kg
Distância: 384.400 km
Resultado: ~1.98 × 10²⁰ N
```

### Exemplo 2: Terra e Satélite
```
Massa da Terra: 5.97 × 10²⁴ kg
Massa do Satélite: 1000 kg
Altitude: 400 km (órbita baixa)
Resultado: ~8.688 × 10³ N
```

### Exemplo 3: Sol e Terra
```
Massa do Sol: 1.99 × 10³⁰ kg
Massa da Terra: 5.97 × 10²⁴ kg
Distância: 149.6 milhões de km
Resultado: ~3.52 × 10²² N
```

## 🎯 Como inserir os dados

A calculadora solicita os valores em **duas partes**:

1. **Número base**: Ex: 5.97 (para 5.97 × 10²⁴)
2. **Expoente**: Ex: 24 (para 10²⁴)

### Exemplo prático:
```
Para inserir 384.400.000 metros:
- Número base: 3.844
- Expoente: 8
- Resultado: 3.844 × 10⁸ m
```

## 📱 Interface do programa

```
=== CALCULADORA DA FORÇA GRAVITACIONAL ===
Fórmula: Fg = GMm / d²
(A constante G já está definida no sistema)

--- Massa do corpo maior (M) ---
Digite o número base (ex: 6.10): 5.97
Digite o expoente (ex: 24 ou -11): 24
Valor inserido: 5.97 × 10^24 kg = 5.97e+24 kg

...

RESULTADO FINAL:
Força gravitacional (Fg) = 1.982e+20 N
```

## 🔧 Funcionalidades técnicas

- **Precisão científica**: Usa notação científica para cálculos precisos
- **Validação automática**: Detecta e formata grandes números
- **Apresentação clara**: Mostra o passo a passo do cálculo
- **Conversões úteis**: Metros ↔ Quilômetros automaticamente

## 📚 Conceitos físicos abordados

- **Lei da Gravitação Universal**
- **Notação científica em física**
- **Forças gravitacionais**
- **Massas astronômicas**
- **Distâncias espaciais**

## 🎓 Casos de uso educacionais

- **Ensino de física**: Demonstração prática da gravitação
- **Astronomia**: Cálculo de forças entre corpos celestes
- **Engenharia espacial**: Planejamento de órbitas
- **Exercícios acadêmicos**: Resolução de problemas

## 🛠️ Estrutura do projeto

```
calculadora-gravitacional/
│
├── calculadora_gravitacional.py  # Código principal
├── README.md                     # Este arquivo
├── requirements.txt              # Dependências
└── examples/                     # Exemplos de uso (opcional)
    ├── terra_lua.md
    ├── planetas.md
    └── satelites.md
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Algumas ideias:

- [ ] Interface gráfica (GUI)
- [ ] Banco de dados de corpos celestes
- [ ] Calculadora de órbitas
- [ ] Gráficos de força vs distância
- [ ] Exportar resultados para arquivo
- [ ] Múltiplas unidades (kg, ton, etc.)
- [ ] Histórico de cálculos
- [ ] Validação de entrada aprimorada

## 📖 Recursos adicionais

- [Lei da Gravitação Universal - Wikipedia](https://pt.wikipedia.org/wiki/Lei_da_gravita%C3%A7%C3%A3o_universal)
- [Constante Gravitacional - NIST](https://physics.nist.gov/cgi-bin/cuu/Value?bg)
- [Massas Planetárias - NASA](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)

## 👨‍💻 Autor

Desenvolvido com 🌟 por O Rake

---

⭐ **Gostou do projeto? Deixe uma estrela!** ⭐

### 🔗 Links úteis
- [Documentação Python](https://docs.python.org/)
- [Física - Khan Academy](https://www.khanacademy.org/science/physics)
- [Colorama Docs](https://pypi.org/project/colorama/)
