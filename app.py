import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Calculadora de Descuento", page_icon="💵")

# Título y Descripción
st.title("💵 Calculadora de Descuento")
st.markdown("Bienvenido. Introduce el costo del producto original para calcular su descuento.")
st.write("---")

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
precio_original = st.sidebar.number_input(
    "Costo del producto ($)", min_value=0.0, value=60.0
)
descuento = st.sidebar.slider(
    "Descuento (%)", 1.00, 99.99, 1.65
)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora"):
    
    # Fórmula Matemática
    precio_final = precio_original * (1 - descuento / 100)

    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Precio final del producto",
            value=f"${precio_final:.2f}"
        )

    # Mostrar la fórmula usada
    st.write("---")
    st.info("Fórmula matemática utilizada:")
    st.latex(r'''
    \text{Precio final} = P_{\text{original}} \times \left(1 - \frac{\text{descuento}}{100}\right)
    ''')

