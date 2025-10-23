import pandas as pd 

cores = ['a','a','a','b','b','c','c','c','c','d','d','d','d']

serieCores = pd.Series(cores)
nPandas = len(serieCores)

freqAbsNi = serieCores.value_counts()
fredRelFi = serieCores.value_counts(normalize=True)

df = pd.DataFrame({
    "ni": freqAbsNi,
    'fi': fredRelFi,
})

# renomeia o índice par 'xi' (variavel)
df.index.name = "xi (Cor)"

# Frequencia relativa percentual (pi)
df['pi (%)'] = df['fi'] *100
df['Ni'] = df['ni'].cumsum()
df['Pi'] = df['pi (%)'].cumsum()

print(f"amostra total N : {nPandas}\n")
print("Tabela de Frequencias (Pandas)")
print(df)
print("\n Verificação de totais:")
print(f"Somas 'ni' (Total de Elementos): {df['ni'].sum()}")
print(f"Somas 'pi' :{df['pi (%)'].sum():.2f}")
