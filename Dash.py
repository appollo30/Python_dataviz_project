#
# Imports
#
import dash
from dash import dcc
from dash import html
from dash import ctx
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc

import GestionCarte as GestionCarte

from file_manager import FileManager
from Charts import BarChart
from Charts import PieChart
from Charts import Histogram
from Charts import ScatterChart
from Charts import EmptyChart

def create_Bar_chart(DATA, column_Name, selectedYear=[]):
    bar_chart = BarChart(DATA, column=column_Name, chosedYear=selectedYear)  
    fig = bar_chart.render_chart()
    return fig

def create_scatter_chart(DATA,abscisse,ordonee):
    scatter_chart = ScatterChart(DATA, abscisse=abscisse, ordonne=ordonee)
    fig = scatter_chart.render_chart()
    return fig


def create_Histogram(DATA, x_name, nbins=20, max_value=199):
    histogram = Histogram(DATA, x=x_name, nbins=nbins, max_value=max_value,date=DATE)
    fig = histogram.render_chart()
    return fig


def create_Pie_chart(DATA, values_name, names):    
    pie_chart = PieChart(DATA.loc[DATA["an"] == DATE], values=values_name,
                         names=names)
    fig = pie_chart.render_chart(title=values_name)
    return fig

def create_Empty_chart():
    empty_chart = EmptyChart()
    fig = empty_chart.render_chart()
    return fig

def open_DATA():
    file_name = "accidentsVelo.csv"
    file_manager = FileManager(file_name)
    file_list = file_manager.open_file()
    DATA = file_list[0]
    DATA=DATA.dropna(subset=['long'])
    DATA=DATA.dropna(subset=['lat'])
    return DATA


def init_maps():
    DATA = open_DATA()
    GestionCarte.createAllMaps(DATA)


def init_pie_chart(DATA):
    global pie_chart_sexe
    DATA.loc[DATA.sexe == 2, "newSexe"] = "femme"
    DATA.loc[DATA.sexe == 1, "newSexe"] = "homme"
    pie_chart_sexe = create_Pie_chart(DATA, "sexe",
                                       'newSexe')
    
def pie_chart_div(DATA):
    init_pie_chart(DATA)
    div = [
        dcc.Tab(label="Repartitions des accidents hommes/femmes",
        children=[dcc.Graph(figure=pie_chart_sexe)]),
    ]
    return div

def init_dash(DATE):
    DATA = open_DATA()
    init_card(DATA,DATE)
    init_pie_chart(DATA)
    fig = create_Empty_chart()
    return DATA, fig


def init_card(DATA,DATE):
    global card_nb_accident_content
    global card_nb_accident_year_content
    
    nb_vehicule = str(len(DATA.loc[(DATA['an'] == DATE)]))
                            
    card_nb_accident_content = [       
                            dbc.CardBody(
                                [
                                    html.H4("Nombre d'accidents de 2005 à 2021", className="card_nb_accident",style={'textAlign' : 'center'}),
                                    html.H2(
                                        len(DATA.index),
                                        className="card-text",
                                        style={'textAlign' : 'center'},
                                    ),
                                ]
                            ),
                    ]
                
    card_nb_accident_year_content = [       
                            dbc.CardBody(
                                [
                                    html.H4("Nombre d'accidents en {}".format(DATE), className="card_nb_accident_year",style={'textAlign' : 'center'}),
                                    html.H2(
                                        nb_vehicule,
                                        className="card-text",
                                        style={'textAlign' : 'center'},
                                    ),
                                ]
                            ),
                        ]

def card_div(DATA):
    init_card(DATA,DATE)
    div = [
        html.Div(
            id='left_cards_div',
            style={'position': 'relative', 'width': '49%', 'float': 'rigth'},
            children=[
                        dbc.Card(card_nb_accident_content),
                    ]
            ),

            html.Div(
                    id="right_cards_div",
                    style={'position': 'relative', 'width': '49%', 'float': 'left'},
                    children=[
                                dbc.Card(card_nb_accident_year_content),
                            ]
                    ),
    ]
    return div
    
def manage_dash(YEARS_OPTIONS):
    global fig
    global change_DATE
    global DATA
    DATA , fig = init_dash(DATE)
    app = dash.Dash(__name__)
    app.layout = html.Div(
        children=[
            dcc.Location(id='url', refresh=False),
            html.H1(children=f'Accidents de Vélo de 2005 à 2021 en France',
                    style={'Position': 'relative', 'width': '100%', 'textAlign': 'center'}),
            html.H4(children=f'Noureddine BOUDALI, Léo LASNIER',
                    style={'Position': 'relative', 'width': '100%', 'textAlign': 'center'}),
            html.H5(children=f"DashBoard sur les données des accidents de vélos",
                    style={'Position': 'relative', 'width': '100%', 'textAlign': 'center'}),
            html.A(
                id = "change_year",
                children=[
                    html.Button('2021', id='button-2021', n_clicks=0),
                    html.Button('2020', id='button-2020', n_clicks=0),
                    html.Button('2019', id='button-2019', n_clicks=0),
                    html.Button('2018', id='button-2018', n_clicks=0),
                    html.Button('2017', id='button-2017', n_clicks=0),
                    html.Button('2016', id='button-2016', n_clicks=0),
                    html.Button('2015', id='button-2015', n_clicks=0),
                    html.Button('2014', id='button-2014', n_clicks=0),
                    html.Button('2013', id='button-2013', n_clicks=0),
                    html.Button('2012', id='button-2012', n_clicks=0),
                    html.Button('2011', id='button-2011', n_clicks=0),
                    html.Button('2010', id='button-2010', n_clicks=0),
                    html.Button('2009', id='button-2009', n_clicks=0),
                    html.Button('2008', id='button-2008', n_clicks=0),
                    html.Button('2007', id='button-2007', n_clicks=0),
                    html.Button('2006', id='button-2006', n_clicks=0),
                    html.Button('2005', id='button-2005', n_clicks=0),
                    html.Div(id='container-button')
                ]),
            html.Div(
                id = "main_body",
                children = [
                    html.Div(
                        id='Holder_Div_Graph',
                        hidden=False,
                        style={'position': 'relative', 'width': '100%', 'float': 'rigth'},
                        children=[
                            html.Div(
                                id='Div_Graph',
                                hidden=False,
                                children=[
                                    dcc.Slider(
                                        id="graph-slider",
                                        min=1,
                                        max=3,
                                        step=1,
                                        marks={
                                            1: 'Bar chart',
                                            2: 'Histogram',
                                            3: 'Scatter',
                                        },
                                        value=1,
                                    ),
                                    html.Div(
                                        id='Dropdown-bar_chart-holder',
                                        hidden=False,
                                        children=[
                                            html.H4(children=f'Sélection des années souhaitées', ),
                                            dcc.Dropdown(

                                                options=YEARS_OPTIONS,
                                                value=list(),
                                                id="Dropdown-bar_chart",
                                                multi=True),
                                            html.Br()
                                        ]
                                    ),
                                    dcc.Graph(
                                        id="graph",
                                        figure=fig
                                    ),
                                ]
                            )
                        ]
                    ),
                    
                    
                    
                    html.Div(
                        id="Right_column",
                        style={'position': 'relative', 'width': '45%', 'float': 'right'},
                        
                        children=[
                            
                            html.Div(
                                id="Cards_Div",
                                children=[
                                    html.Div(
                                        id='left_cards_div',
                                        style={'position': 'relative', 'width': '45%', 'float': 'left'},
                                        children=[
                                            dbc.Card(card_nb_accident_content),
                                        ]
                                    ),

                                    html.Div(
                                        id="right_cards_div",
                                        style={'position': 'relative', 'width': '45%', 'float': 'rigth'},
                                        children=[
                                            dbc.Card(card_nb_accident_year_content),
                                        ]
                                    ),
                                ]
                            ),
                            html.Div(
                                id="pie_chart",
                                style={'position': 'relative', 'width': '96%', 'float': 'left'},
                                children=[
                                    dcc.Tabs(
                                        id="tabs_pie_chart",
                                    ),
                                ]
                            )
                        ]
                    ),
                    
                    html.Div(
                        id="MapByYears",
                        hidden=False,
                        style={'position': 'relative', 'width': '49%', 'padding': 5, 'float': 'left'},
                        children=[

                            dcc.Dropdown(
                                id="Change",
                                options=[
                                    {'label': 'All', 'value': 'All'},
                                    {'label': '2005', 'value': '2005'},
                                    {'label': '2006', 'value': '2006'},
                                    {'label': "2007", 'value': "2007"},
                                    {'label': '2008', 'value': '2008'},
                                    {'label': "2009", 'value': "2009"},
                                    {'label': "2010", 'value': "2010"},
                                    {'label': '2011', 'value': '2011'},
                                    {'label': '2012', 'value': '2012'},
                                    {'label': '2013', 'value': '2013'},
                                    {'label': '2014', 'value': '2014'},
                                    {'label': '2015', 'value': '2015'},
                                    {'label': '2016', 'value': '2016'},
                                    {'label': '2017', 'value': '2017'},
                                    {'label': '2018', 'value': '2018'},
                                    {'label': '2019', 'value': '2019'},
                                    {'label': '2020', 'value': '2020'},
                                    {'label': "2021", 'value': "2021"}
                                ],
                                value='All'
                            ),

                            html.Iframe(
                                id='mapParAn',
                                srcDoc=open("templates/MapAllYears.html", 'r').read(),
                                width='100%',
                                height='650',
                            ),

                        ]   
                    )                    
                ]
            ),

            html.Span(id="ChangeClick", style={"verticalAlign": "middle"}),
        ]
    )

    #Permet de changer la carte
    @app.callback(
        Output("mapParAn", "srcDoc"), [Input("Change", "value")],
    )
    def choose_map(name):
        if name == "All":
            return open("templates/MapAllYears.html", 'r').read()
        return open("templates/MapYears{}.html".format(name), 'r').read()

    #Change le graphique
    @app.callback(
        Output(component_id='graph', component_property='figure'),  # (1)
        Output(component_id='Dropdown-bar_chart-holder', component_property='hidden'),
        [Input(component_id='graph-slider', component_property='value'), Input('Dropdown-bar_chart', 'value')]  # (2)
    )
    def updatefig(input_value, years):
        global fig
        global DATA
        years = [int(i) for i in years]
        if input_value == 1:                
            DATA.loc[DATA.sexe == 2, "newSexe"] = "femme"
            DATA.loc[DATA.sexe == 1, "newSexe"] = "homme"
            fig = create_Bar_chart(DATA, "newSexe", years)
            return fig, False
        elif input_value == 2:
            DATA = DATA[DATA["age"] < 100]
            fig = create_Histogram(DATA, "age")
            return fig, True
        elif input_value == 3:
            fig = create_scatter_chart(DATA, "age",'grav')
            return fig, True

    @app.callback(
    Output('container-button', 'children'),
    Output('Cards_Div','children'),
    Output('pie_chart','children'),
    Input('button-2021', 'n_clicks'),
    Input('button-2020', 'n_clicks'),
    Input('button-2019', 'n_clicks'),
    Input('button-2018', 'n_clicks'),
    Input('button-2017', 'n_clicks'),
    Input('button-2016', 'n_clicks'),
    Input('button-2015', 'n_clicks'),
    Input('button-2014', 'n_clicks'),
    Input('button-2013', 'n_clicks'),
    Input('button-2012', 'n_clicks'),
    Input('button-2011', 'n_clicks'),
    Input('button-2009', 'n_clicks'),
    Input('button-2008', 'n_clicks'),
    Input('button-2007', 'n_clicks'),
    Input('button-2006', 'n_clicks'),
    Input('button-2005', 'n_clicks'),
)
    def displayClick(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16):
        global DATE
        global fig
        global DATA
        global change_DATE
        msg = "Année choisie = 2021"
        if "button-2021" == ctx.triggered_id:
            DATE = 2021
            msg = "Année choisie = 2021"
        elif "button-2020" == ctx.triggered_id:
            DATE = 2020
            msg = "Année choisie = 2020"
        elif "button-2019" == ctx.triggered_id:
            DATE = 2019
            msg = "Année choisie = 2019"
        elif "button-2018" == ctx.triggered_id: 
            DATE = 2018
            msg = "Année choisie = 2018"
        elif "button-2017" == ctx.triggered_id: 
            DATE = 2017
            msg = "Année choisie = 2017"
        elif "button-2016" == ctx.triggered_id: 
            DATE = 2016
            msg = "Année choisie = 2016"
        elif "button-2015" == ctx.triggered_id: 
            DATE = 2015
            msg = "Année choisie = 2015"
        elif "button-2014" == ctx.triggered_id: 
            DATE = 2014
            msg = "Année choisie = 2014"
        elif "button-2013" == ctx.triggered_id: 
            DATE = 2013
            msg = "Année choisie = 2013"
        elif "button-2012" == ctx.triggered_id: 
            DATE = 2012
            msg = "Année choisie = 2012"
        elif "button-2011" == ctx.triggered_id: 
            DATE = 2011
            msg = "Année choisie = 2011"
        elif "button-2010" == ctx.triggered_id: 
            DATE = 2010
            msg = "Année choisie = 2010"
        elif "button-2009" == ctx.triggered_id: 
            DATE = 2009
            msg = "Année choisie = 2009"
        elif "button-2008" == ctx.triggered_id: 
            DATE = 2008
            msg = "Année choisie = 2008"
        elif "button-2007" == ctx.triggered_id: 
            DATE = 2007
            msg = "Année choisie = 2007"
        elif "button-2006" == ctx.triggered_id: 
            DATE = 2006
            msg = "Année choisie = 2006"
        elif "button-2005" == ctx.triggered_id: 
            DATE = 2005
            msg = "Année choisie = 2005"   
            
        DATA = open_DATA()
        div_card = card_div(DATA)
        init_pie_chart(DATA)
        div_pie_chart = pie_chart_div(DATA)
        return html.Div(msg),div_card,[dcc.Tabs(id="tabs_pie_chart",children=div_pie_chart),]


    
    #
    # RUN APP
    #

    app.run_server(debug=True)

def main_Dash(is_DATE_selected = False):
    # Dictionnaire des années possibles
    YEARS = dict(
        A2005 = "2005",
        A2006 = "2006",
        A2007 = "2007",
        A2008 = "2008",
        A2009 = "2009",
        A2010 = "2010",
        A2011 = "2011",
        A2012 = "2012",
        A2013 = "2013",
        A2014 = "2014",
        A2015 = "2015",
        A2016 = "2016",
        A2017 = "2017",
        A2018 = "2018",
        A2019 = "2019",
        A2020 = "2020",
        A2021 = "2021",
    )
    YEARS_OPTIONS = [
        {"label": str(YEARS[years]), "value": str(YEARS[years])}
        for years in YEARS
    ]
    global DATE
    global fig
    global DATA
    global change_DATE
    change_DATE = False
    DATE = 2021
    DATA , fig = init_dash(DATE)
    
    manage_dash(YEARS_OPTIONS)
    
