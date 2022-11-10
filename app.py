import dash
from dash import Dash, html, dcc, callback, Input, Output
import dash_daq as daq

app = Dash(__name__, update_title="Loading", use_pages=True, meta_tags=[
    {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, maximum-scale=1",
    }
],)

app.layout = html.Div(
    id="app",
    children=[
        html.Nav([
            html.Img(src="/assets/eevee_logo.png",
                 alt="Eevee Logo", className="navbar__logo"),
            html.Span(dcc.Link('COMPAREON', href="/"),
                      className="navbar__title"),
            html.Div([
                html.Img(src="/assets/solrock_logo.png",
                 alt="Solrock Light Mode", className="navbar__switch_img"),
                 daq.BooleanSwitch(
                    id='dark-mode-switch',
                    on=False,
                    color='goldenrod',
                    persistence=True),
                 # html.Div(id='boolean-switch-result')
                 html.Img(src="/assets/lunatone_logo.png",
                          alt="Lunatone Dark Mode", className="navbar__switch_img"),
                 ], className="navbar__switch"),
            html.Img(id="eeveelution", alt="Eeveelution Logo",
                     className="navbar__logo")
        ], className="navbar"),
        html.Div(
            dash.page_container,
            className="container"
        ),
        html.Footer([
            html.Div("Compareon v2.0"),
            html.Div("Created by Caffeine - 2021")
        ], className="footer")
    ])


@callback(Output('app', 'className'), Output('eeveelution', 'src'), Input('dark-mode-switch', 'on'))
def set_mode(on):
    if (on):
        return 'dark', "/assets/umbreon_logo.png"
    else:
        return 'light', "/assets/espeon_logo.png"


if __name__ == '__main__':
    app.run_server(debug=True)
