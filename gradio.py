import gradio as gr
import numpy as np
import pandas as pd
import plotly.express as px

def calcular_probabilidades(input_text):
    # Gerando probabilidades aleatórias
    probabilidades = np.random.rand(5)
    eventos = ['P1', 'P2', 'P3', 'P4', 'P5']
    
    # Criando um DataFrame para ordenar as probabilidades
    df = pd.DataFrame({
        'Evento': eventos,
        'Probabilidade': probabilidades
    })
    
    # Ordenando as probabilidades
    df_sorted = df.sort_values('Probabilidade', ascending=False)
    
    # Criando um gráfico de barras com Plotly
    fig = px.bar(df_sorted, x='Evento', y='Probabilidade', title='Probabilidades Ordenadas', 
                 labels={'Probabilidade': 'Probabilidade', 'Evento': 'Eventos'})
    
    return fig

# Criando a interface
iface = gr.Interface(
    fn=calcular_probabilidades,
    inputs="text",
    outputs="plot",
    title="Calculador de Probabilidades",
    description="Insira qualquer texto para gerar e visualizar as probabilidades ordenadas de P1 a P5."
)

# Executando a interface
iface.launch()
