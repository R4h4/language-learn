import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
import data


def get_chapters():
    return data.chapters


@app.callback(Output('chapters_available', 'children'),
              [Input('chapters_available', 'id')])
def load_available_chapters(_):
    chapter_data = get_chapters()
    chapters = dbc.Row(
        [
            dbc.Col(
                html.A(
                    href=f"./Chapter/{c_id}",
                    children=[
                        dbc.Card(
                            [
                                dbc.CardImg(src=c['image'], top=True),
                                dbc.CardBody(
                                    html.H4(c['name'], className="card-title")
                                ),
                            ],
                            color=c['color']
                        )
                    ],
                ),
                width=6,
                md=4,
                lg=4,
            ) for c_id, c in chapter_data.items()
        ]
    )
    return chapters
