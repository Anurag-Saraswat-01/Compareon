import dash
from dash import html, dcc, dash_table, callback, Input, Output
import plotly.express as px
import pandas as pd
import plotly.io as pio

from . import theme

pio.templates.default = 'custom'


dash.register_page(__name__, path='/compare')

print('\nLoading dex')
df = pd.read_csv("data/pokedex_markdown.csv")
print('Dex loaded')

# name: value pair list for dropdown
names = [{'label': name, 'value': name} for name in df['Name']]

eeveelutions = ['Eevee', 'Umbreon', 'Espeon']

# df for stats
stat_df = pd.melt(df, id_vars='Name', value_vars=[
                  'Speed', 'Sp. Defense', 'Sp. Attack', 'Defense', 'Attack', 'HP'], var_name='stat')
stat_df.set_index("Name", inplace=True)

# df for Stat Total
bst_df = pd.melt(df, id_vars='Name', value_vars='Stat Total',
                 var_name='Stat Total')
bst_df.set_index("Name", inplace=True)

# df for img src
src_df = df[['Name', 'Image', 'Type', 'Ability', 'Hidden Ability']].copy()
src_headers = pd.DataFrame(columns=src_df.columns)
src_headers.loc[0] = src_headers.columns
src_df.set_index("Name", inplace=True)


def transform(df):
    df = df.set_index('Name')
    df = df[['Image', 'Type', 'Ability', 'Hidden Ability']].transpose()
    # df = df.reset_index()
    return df


layout = html.Div([
    # dcc.Loading([
    html.Div([
        dcc.Dropdown(
            id="dropdown",
            options=names,
            multi=True,
            # value=eeveelutions
        )
    ], className="compare__dropdown_wrapper"),
    html.Div([
        dcc.Loading([
            dash_table.DataTable(
                    id="data_table",
                    css=[{'selector': 'table', 'rule': 'table-layout: fixed'}],
                    style_table={'borderRadius': '0.5rem'},
                    style_header={'whiteSpace': 'normal', 'height': 'auto',
                                  'padding': '0.5rem 0.25rem',
                                  },
                    style_cell={'background': 'transparent',
                                'border': 'none',
                                'color': 'black',
                                'whiteSpace': 'normal', 'height': 'auto', 'padding': '0.5rem 1rem',
                                'overflow': 'None'
                                },
                    style_cell_conditional=[
                        {'if': {'column_id': 'Name'},
                         'width': '150px'}
                    ],
                    style_data_conditional=[
                        {'if': {'state': 'active'},
                         'backgroundColor': 'transparent !important',
                         'border': 'inherit !important', },
                    ]
                    ),
            dcc.Graph(
                id="stat_fig",
                config={'displayModeBar': False}
            ),
            dcc.Graph(
                id="bst_fig",
                config={'displayModeBar': False}
            )
        ], color="goldenrod", type="circle")
    ], className="compare__content")
    # ], type="circle")
], className="compare")


@ callback(Output("data_table", "data"), Output("data_table", "columns"), Output("stat_fig", "figure"), Output("bst_fig", "figure"),
           Input("dropdown", "value"))
def update_graph(dropdown_value):
    print('Dropdown value:', dropdown_value)
    if dropdown_value is None or len(dropdown_value) == 0:
        # dropdown_value = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander',
        #                   'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', ]
        dropdown_value = eeveelutions
    # dropdown_value = dropdown_value[:10]

    # df for base stats
    stat_callback_df = stat_df.loc[dropdown_value]
    stat_callback_df.reset_index(inplace=True)
    # df for base stat total
    bst_callback_df = bst_df.loc[dropdown_value]
    bst_callback_df.reset_index(inplace=True)
    # df for data table
    src_callback_df = src_df.loc[dropdown_value]
    src_callback_df.reset_index(inplace=True)
    src_callback_df = pd.concat(
        [src_headers, src_callback_df]).set_index('Name').reset_index()

    stat_fig = px.bar(
        stat_callback_df,
        x='value',
        y='stat',
        color='value',
        facet_col='Name',
        facet_col_spacing=0.001,
        height=300,
        text='value',
        title='Base Stat Distribution',
        color_continuous_scale=[[0, 'hsla(0, 100, 50, 0.75)'], [0.35, 'hsla(60, 100%, 50%, 0.75)'],
                                [0.55, 'hsla(120, 100%, 50%, 0.75)'], [1, 'hsla(180, 100%, 50%, 0.75)']],
        range_color=[40, 200],
    )
    for a in stat_fig.layout.annotations:
        a.text = ''
    stat_fig.update_layout(margin=dict(l=150, t=60, b=0),
                           title_xref='paper', autosize=True, clickmode=None, dragmode=False)
    stat_fig.update_yaxes(title='')
    stat_fig.update_traces(textfont_color='black', textfont_size=14,)

    bst_fig = px.bar(
        bst_callback_df,
        y='Stat Total',
        x='value',
        color='value',
        color_continuous_scale=[[0, 'hsla(0, 100, 50, 0.75)'], [0.35, 'hsla(60, 100%, 50%, 0.75)'],
                                [0.55, 'hsla(120, 100%, 50%, 0.75)'], [1, 'hsla(180, 100%, 50%, 0.75)']],
        range_color=[300, 720],
        facet_col='Name',
        facet_col_spacing=0.001,
        height=120,
        text='value',
        title='Base Stat Total'
    )
    for a in bst_fig.layout.annotations:
        a.text = ''
    bst_fig.update_layout(margin=dict(l=150, t=60, b=20),
                          title_xref='paper', autosize=True, clickmode=None, dragmode=False)
    bst_fig.update_yaxes(title='')
    bst_fig.update_traces(textfont_color='black', textfont_size=14)

    table_data = transform(src_callback_df).to_dict('records')
    table_columns = [dict(name=i, id=i, presentation='markdown')
                     for i in transform(src_callback_df).columns]

    return table_data, table_columns, stat_fig, bst_fig
