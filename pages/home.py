import dash
from dash import html, dcc

dash.register_page(__name__, title="Compareon", path='/')

layout = html.Div([
    html.Div([
        html.Img(src="/assets/Eevee_LG.png",
                 alt="Hero Eevee", className="home__hero"),
    ], className="home__hero_wrapper"),
    html.Div([
        html.H1("Welcome to Compareon!", className="home__text_title"),
        html.Div([
            html.P(
                "Compareon is a Web Application built using Python Dash Framework, Plotly and CSS3."),
            html.P('''
            The purpose of this application is to allow users to compare the stats viz. Hit Points, Attack,
            Defense, Special Attack, Special Defense and Speed along with Types, Abilities and Hidden Abilities of various Pokémon.
            '''),
            html.P('''
            The Compare Page allows users to compare the different Pokémon. Users can select the Pokémon
            they want using the Dropdown menu. As such, there is no limit to the number of Pokémon that can be selected
            simultaneously, however the results are clipped to a maximum of 10 Pokémon.
            '''),
            html.P(
                "The Pokémon species data is upto date with Generation 8 - Pokémon Legends: Arceus.")
        ], className="home__text"),
        dcc.Link(html.Button("Proceed to Compare",
                 className="home__button"), href="/compare"),
    ], className="home__text_wrapper")
], className="home")
