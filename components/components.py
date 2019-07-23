import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from flask import current_app as server

from utils import get_url, component


def fa(className):
    """A convenience component for adding Font Awesome icons"""
    return html.I(className=className)


navbar_toggler = html.Button(
    className='navbar-toggler',
    type='button',
)


@component
def make_brand(**kwargs):
    return html.Header(
        className="brand",
        children=dcc.Link(
            href=get_url(""),
            children=html.H1([fa("far fa-chart-bar"), server.config["TITLE"]]),
        ),
        **kwargs,
    )


@component
def make_header(**kwargs):
    return dbc.Navbar(
        id="header",
        className="sticky-top",
        color="dark",
        dark=True,
        children=[
            make_brand(),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                children=html.Ul(
                    id=server.config["NAVBAR_CONTAINER_ID"], className="navbar-nav ml-auto"
                ),
                id="navbar-collapse",
                navbar=True),
        ],
        **kwargs,
    )


@component
def make_sidebar(**kwargs):
    return dbc.NavbarSimple(
        id=f"sidebar",
        className="nav navbar-dark bg-dark flex-column align-items-start",
        children=[make_brand(), html.Div(id=server.config["NAVBAR_CONTAINER_ID"])],
        **kwargs,
    )
