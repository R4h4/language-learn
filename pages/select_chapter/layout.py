import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

layout = dbc.Container(
    [
        html.H1("Select chapter", className="mt-4"),
        html.Div(id='chapters_available')
    ]
)
