from urllib.parse import parse_qsl

from flask import current_app as server
from dash import no_update
from dash.dependencies import Output, Input, State
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from app import app


@app.callback(Output('page_content', 'children'),
              [Input('page_content', 'page_content')],
              [State(server.config["LOCATION_COMPONENT_ID"], 'search')])
def load_learning_page(_, url_search):
    url_params = dict(parse_qsl(url_search))
    book = url_params['book']
    chapter = url_params['chapter']
    page = url_params['page']

    

    pass
