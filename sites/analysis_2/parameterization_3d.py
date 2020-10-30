import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

def parameterization_3d():
    functions = {
        "a": lambda x, a, b: a * np.ones_like(x),
        "b*t + a": lambda x, a, b: b*x + a,
        "a*sin(b*t)": lambda x, a, b: a*np.sin(b*x),
        "a*cos(b*t)": lambda x, a, b: a*np.cos(b*x),
    }
    functions_latex = {
        "a": " %1.2f %0.0f",
        "b*t + a": " %1.2f t + %1.2f ",
        "a*sin(b*t)": " %1.2f \sin(%1.2f t) ",
        "a*cos(b*t)": " %1.2f \cos(%1.2f t) ",
    }

    use_parameter_slider = st.checkbox(
        "Parameter Slider hinzuschalten"
    )

    column_x, column_y, column_z = st.beta_columns((1, 1, 1))

    column_x.subheader("Parameter in x")
    function_x_key = column_x.radio(
        label="Funktion in x",
        options=list(functions.keys()),
        index=2,
    )
    if use_parameter_slider:
        x_a = column_x.slider(
            "Parameter a für x",
            min_value=-5.0,
            max_value=5.0,
            value=1.0,
            step=0.1,
        )
        x_b = column_x.slider(
            "Parameter b für x",
            min_value=-5.0,
            max_value=5.0,
            value=1.0,
            step=0.1,
        )
    else:
        x_a = 1.0
        x_b = 1.0

    column_y.subheader("Parameter in y")
    function_y_key = column_y.radio(
        label="Funktion in y",
        options=list(functions.keys()),
        index=3
    )
    if use_parameter_slider:
        y_a = column_y.slider(
            "Parameter a für y",
            min_value=-5.0,
            max_value=5.0,
            value=1.0,
            step=0.1,
        )
        y_b = column_y.slider(
            "Parameter b für y",
            min_value=-5.0,
            max_value=5.0,
            value=1.0,
            step=0.1,
        )
    else:
        y_a = 1.0
        y_b = 1.0

    column_z.subheader("Parameter in z")
    function_z_key = column_z.radio(
        label="Funktion in z",
        options=list(functions.keys()),
        index=1
    )
    if use_parameter_slider:
        z_a = column_z.slider(
            "Parameter a für z",
            min_value=-5.0,
            max_value=5.0,
            value=1.0,
            step=0.1,
        )
        z_b = column_z.slider(
            "Parameter b für z",
            min_value=-5.0,
            max_value=5.0,
            value=1.0,
            step=0.1,
        )
    else:
        z_a = 1.0
        z_b = 1.0

    column_start, column_end = st.beta_columns((1, 1))
    t_start = column_start.slider(
        label="Startpunkt der Parametrisierung",
        min_value=-10.0,
        max_value=10.0,
        value=0.0,
        step=0.1,
    )
    t_end = column_end.slider(
        label="Endpunkt der Parametrisierung",
        min_value=-10.0,
        max_value=10.0,
        value=10.0,
        step=0.1,
    )

    t = np.linspace(t_start, t_end, 50)

    x = functions[function_x_key](t, x_a, x_b)
    y = functions[function_y_key](t, y_a, y_b)
    z = functions[function_z_key](t, z_a, z_b)

    fig = go.Figure(data=go.Scatter3d(
        x=x,
        y=y,
        z=z,
        line_width=8,
        mode="lines"
    ))

    fig.update_layout(
        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0,
        ),
        scene=dict(
            xaxis=dict(
                range=(-10, 10)
            ),
            yaxis=dict(
                range=(-10, 10)
            ),
            zaxis=dict(
                range=(-10, 10)
            )
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    # Display a latex version
    x_latex = functions_latex[function_x_key] % (x_a, x_b)
    y_latex = functions_latex[function_y_key] % (y_a, y_b)
    z_latex = functions_latex[function_z_key] % (z_a, z_b)
    st.latex(r"""
        \vec{\gamma}(t)
        =
        \begin{pmatrix}
        %s\\
        %s\\
        %s\\
        \end{pmatrix}
        \quad
        \text{for}
        t
        \in
        (%1.2f, %1.2f)
    """  % (x_latex, y_latex, z_latex, t_start, t_end))

details = {
    "german": {
        "title": "Kurven Parametrisierung in 3D",
        "introduction": "Some filthy words",
        "theory": [],
        "plot": parameterization_3d,
        "questions": [],
    }
}

if __name__ == "__main__":
    parameterization_3d()