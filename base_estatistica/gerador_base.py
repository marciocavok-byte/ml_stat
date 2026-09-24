import random
from datetime import datetime, timedelta
import pandas as pd
from faker import Faker
import numpy as np

# Inicializa o Faker configurado para o Brasil
fake = Faker('pt_BR')

# 1. MAPEAMENTO DE LOCALIDADES (DF E ENTORNO)
# Separamos o Plano Piloto em Asa Sul e Asa Norte e renomeamos o conceito para LOCALIDADES
LOCALIDADES_DF = {
    # --- DISTRITO FEDERAL (37 RAs / Bairros Desmembrados) ---
    # Altíssimo Padrão / Luxo
    "Asa Sul": {"preco_m2": 11200, "tipo_predominante": "Apartamento"},
    "Asa Norte": {"preco_m2": 11000, "tipo_predominante": "Apartamento"},
    "Lago Sul": {"preco_m2": 12000, "tipo_predominante": "Casa"},
    "Lago Norte": {"preco_m2": 10500, "tipo_predominante": "Casa"},
    "Sudoeste / Octogonal": {"preco_m2": 12500, "tipo_predominante": "Apartamento"},
    "Noroeste": {"preco_m2": 13500, "tipo_predominante": "Apartamento"},
    "Park Way": {"preco_m2": 8500, "tipo_predominante": "Casa"},
    
    # Médio-Alto Padrão e Expansão Urbana
    "Águas Claras": {"preco_m2": 8500, "tipo_predominante": "Apartamento"},
    "Guará": {"preco_m2": 7200, "tipo_predominante": "Misto"},
    "Jardim Botânico": {"preco_m2": 6500, "tipo_predominante": "Casa"},
    "Vicente Pires": {"preco_m2": 4500, "tipo_predominante": "Casa"},
    "Arniqueira": {"preco_m2": 4800, "tipo_predominante": "Casa"},
    "Cruzeiro": {"preco_m2": 7500, "tipo_predominante": "Apartamento"},
    "Sobradinho": {"preco_m2": 4500, "tipo_predominante": "Casa"},
    "Sobradinho II": {"preco_m2": 3800, "tipo_predominante": "Casa"},
    "Taguatinga": {"preco_m2": 5200, "tipo_predominante": "Misto"},
    
    # Médio e Médio-Baixo Padrão
    "Gama": {"preco_m2": 4200, "tipo_predominante": "Misto"},
    "Ceilândia": {"preco_m2": 3800, "tipo_predominante": "Misto"},
    "Samambaia": {"preco_m2": 4100, "tipo_predominante": "Apartamento"},
    "Santa Maria": {"preco_m2": 3500, "tipo_predominante": "Misto"},
    "São Sebastião": {"preco_m2": 3600, "tipo_predominante": "Misto"},
    "Recanto das Emas": {"preco_m2": 3200, "tipo_predominante": "Misto"},
    "Riacho Fundo": {"preco_m2": 4000, "tipo_predominante": "Misto"},
    "Riacho Fundo II": {"preco_m2": 3400, "tipo_predominante": "Misto"},
    "Núcleo Bandeirante": {"preco_m2": 4900, "tipo_predominante": "Misto"},
    "Candangolândia": {"preco_m2": 4400, "tipo_predominante": "Misto"},
    "Paranoá": {"preco_m2": 3300, "tipo_predominante": "Misto"},
    "Itapoã": {"preco_m2": 3100, "tipo_predominante": "Misto"},
    
    # Áreas Industriais, Periféricas ou Recentes do DF
    "SIA": {"preco_m2": 5500, "tipo_predominante": "Apartamento"}, 
    "SCIA / Estrutural": {"preco_m2": 2600, "tipo_predominante": "Misto"},
    "Varjão": {"preco_m2": 3500, "tipo_predominante": "Misto"},
    "Brazlândia": {"preco_m2": 3000, "tipo_predominante": "Casa"},
    "Planaltina": {"preco_m2": 3200, "tipo_predominante": "Misto"},
    "Fercal": {"preco_m2": 2200, "tipo_predominante": "Casa"},
    "Sol Nascente / Pôr do Sol": {"preco_m2": 2400, "tipo_predominante": "Misto"},
    "Água Quente": {"preco_m2": 2100, "tipo_predominante": "Casa"},
    "Arapoangas": {"preco_m2": 2700, "tipo_predominante": "Casa"},
    "26 de Setembro": {"preco_m2": 2500, "tipo_predominante": "Casa"},
    "Ponte Alta": {"preco_m2": 2800, "tipo_predominante": "Casa"},

    # --- ENTORNO EM GOIÁS (29 Municípios da RIDE) ---
    "Valparaíso de Goiás": {"preco_m2": 3200, "tipo_predominante": "Apartamento"},
    "Águas Lindas de Goiás": {"preco_m2": 2600, "tipo_predominante": "Misto"},
    "Cidade Ocidental": {"preco_m2": 2800, "tipo_predominante": "Casa"},
    "Novo Gama": {"preco_m2": 2500, "tipo_predominante": "Casa"},
    "Formosa": {"preco_m2": 3400, "tipo_predominante": "Casa"},
    "Luziânia": {"preco_m2": 2700, "tipo_predominante": "Casa"},
    "Planaltina (GO)": {"preco_m2": 2400, "tipo_predominante": "Casa"},
    "Santo Antônio do Descoberto": {"preco_m2": 2300, "tipo_predominante": "Casa"},
    "Cristalina": {"preco_m2": 3100, "tipo_predominante": "Casa"},
    "Padre Bernardo": {"preco_m2": 2200, "tipo_predominante": "Casa"},
    "Cocalzinho de Goiás": {"preco_m2": 2400, "tipo_predominante": "Casa"},
    "Pirenópolis": {"preco_m2": 4500, "tipo_predominante": "Casa"}, 
    "Alexânia": {"preco_m2": 2800, "tipo_predominante": "Casa"},     
    "Abadiânia": {"preco_m2": 2300, "tipo_predominante": "Casa"},
    "Alto Paraíso de Goiás": {"preco_m2": 4200, "tipo_predominante": "Casa"}, 
    "Goianésia": {"preco_m2": 2600, "tipo_predominante": "Casa"},
    "Niquelândia": {"preco_m2": 1900, "tipo_predominante": "Casa"},
    "São João d’Aliança": {"preco_m2": 2100, "tipo_predominante": "Casa"},
    "Água Fria de Goiás": {"preco_m2": 1800, "tipo_predominante": "Casa"},
    "Alvorada do Norte": {"preco_m2": 1700, "tipo_predominante": "Casa"},
    "Barro Alto": {"preco_m2": 1900, "tipo_predominante": "Casa"},
    "Cabeceiras": {"preco_m2": 1800, "tipo_predominante": "Casa"},
    "Cavalcante": {"preco_m2": 2300, "tipo_predominante": "Casa"},
    "Flores de Goiás": {"preco_m2": 1600, "tipo_predominante": "Casa"},
    "Mimoso de Goiás": {"preco_m2": 1500, "tipo_predominante": "Casa"},
    "Simolândia": {"preco_m2": 1600, "tipo_predominante": "Casa"},
    "Vila Boa": {"preco_m2": 1500, "tipo_predominante": "Casa"},
    "Vila Propício": {"preco_m2": 1600, "tipo_predominante": "Casa"},
    "Cabeceira Grande": {"preco_m2": 1700, "tipo_predominante": "Casa"}
}

QTD_IMOVEIS = 5500
QTD_CLIENTES = 1300

# ==========================================
# FUNÇÃO PARA INJETAR RUÍDO (DADOS AUSENTES)
# ==========================================
def injetar_dados_ausentes(df, colunas_alvo):
    df_mascarado = df.copy()
    for coluna in colunas_alvo:
        if coluna in df_mascarado.columns:
            percentual_nulo = random.uniform(0.05, 0.07)
            total_nulos = int(len(df_mascarado) * percentual_nulo)
            indices_para_apagar = random.sample(range(len(df_mascarado)), total_nulos)
            df_mascarado.iloc[indices_para_apagar, df_mascarado.columns.get_loc(coluna)] = np.nan
    return df_mascarado

# ==========================================
# GERAÇÃO DA BASE DE IMÓVEIS
# ==========================================
print("Gerando base limpa de imóveis...")
dados_imoveis = []

for i in range(QTD_IMOVEIS):
    id_imovel = f"IMV-{10000 + i}"
    localidade = random.choice(list(LOCALIDADES_DF.keys()))
    info_loc = LOCALIDADES_DF[localidade]
    
    if info_loc["tipo_predominante"] == "Misto":
        tipo = random.choice(["Apartamento", "Casa"])
    else:
        tipo = info_loc["tipo_predominante"]
        
    if tipo == "Casa":
        area = random.randint(120, 600)
        quartos = random.randint(3, 5)
        banheiros = quartos + random.randint(0, 2)
        vagas = random.randint(2, 4)
    else:
        area = random.randint(40, 180)
        quartos = random.randint(1, 4)
        banheiros = random.randint(1, quartos)
        vagas = random.randint(1, 2) if area > 70 else random.randint(0, 1)

    idade_imovel = random.randint(0, 40)
    
    fator_idade = max(0.7, 1 - (idade_imovel * 0.01)) 
    preco_base = area * info_loc["preco_m2"] * fator_idade
    preco_final = int(preco_base * random.uniform(0.85, 1.15))
    
    dados_imoveis.append({
        "id_imovel": id_imovel,
        "localidade": localidade,  # Mudança de nome da coluna
        "tipo": tipo,
        "area_m2": area,
        "quartos": quartos,
        "banheiros": banheiros,
        "vagas_garagem": vagas,
        "idade_anos": idade_imovel,
        "preco_venda": preco_final
    })

df_imoveis_limpo = pd.DataFrame(dados_imoveis)
colunas_imoveis = ["localidade", "tipo", "area_m2", "quartos", "banheiros", "vagas_garagem", "idade_anos", "preco_venda"]
df_imoveis_final = injetar_dados_ausentes(df_imoveis_limpo, colunas_imoveis)

# ==========================================
# GERAÇÃO DA BASE DE CLIENTES (CRM)
# ==========================================
print("Gerando base limpa de clientes do CRM...")
dados_clientes = []

for i in range(QTD_CLIENTES):
    id_cliente = f"CLI-{50000 + i}"
    renda_mensal = random.choices(
        [random.randint(3000, 7000), random.randint(7001, 15000), random.randint(15001, 45000)],
        weights=[0.5, 0.35, 0.15], k=1
    )[0]
    
    # Define a localidade de interesse preferencial com base na renda
    if renda_mensal > 15000:
        localidade_interesse = random.choice(["Lago Sul", "Lago Norte", "Noroeste", "Sudoeste / Octogonal", "Asa Sul", "Asa Norte"])
    elif renda_mensal > 7000:
        localidade_interesse = random.choice(["Águas Claras", "Guará", "Jardim Botânico"])
    else:
        localidade_interesse = random.choice(["Taguatinga", "Ceilândia", "Samambaia", "Valparaíso de Goiás", "Águas Lindas de Goiás"])

    score_credito = random.randint(300, 1000)
    
    if score_credito < 500:
        historico_inadimplente = random.choices([1, 0], weights=[0.7, 0.3])[0]
    else:
        historico_inadimplente = random.choices([1, 0], weights=[0.05, 0.95])[0]

    data_cadastro = datetime.now() - timedelta(days=random.randint(0, 365))

    dados_clientes.append({
        "id_cliente": id_cliente,
        "nome": fake.name(),
        "email": fake.email(),
        "telefone": fake.phone_number(),
        "renda_mensal": renda_mensal,
        "score_credito": score_credito,
        "historico_inadimplente": historico_inadimplente,
        "localidade_interesse": localidade_interesse,  # Mudança de nome da coluna
        "tipo_imovel_interesse": random.choice(["Apartamento", "Casa"]),
        "data_cadastro": data_cadastro.strftime("%Y-%m-%d")
    })

df_clientes_limpo = pd.DataFrame(dados_clientes)
colunas_clientes = ["nome", "email", "telefone", "renda_mensal", "score_credito", "historico_inadimplente", "localidade_interesse", "tipo_imovel_interesse", "data_cadastro"]
df_clientes_final = injetar_dados_ausentes(df_clientes_limpo, colunas_clientes)

# ==========================================
# EXPORTAÇÃO DAS BASES PARA CSV
# ==========================================
print("Exportando bases para CSV...")
df_imoveis_final.to_csv("base_imoveis.csv", index=False, encoding='utf-8')
df_clientes_final.to_csv("base_clientes.csv", index=False, encoding='utf-8')

