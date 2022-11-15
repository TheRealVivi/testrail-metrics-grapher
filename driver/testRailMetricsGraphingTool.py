'''
Created on Nov 4, 2022

@author: Kyle O'Dell
'''
import plotly.express as px
import pandas as pd

# Returns bar chart based on provided csv
def BarGraphConsolidatedMetrics() -> object:
    df: type[pd.DataFrame] = pd.read_csv('../../../Documents/consolidatedMetrics.csv')
    #df = df.drop(labels=[7], axis=0,)
    fig: object = px.bar(df, x='Test Case Status', y=' Test Count')
    
    return fig

# Returns pie chart based on provided csv
def PieGraphConsolidatedMetrics() -> object:
    df: type[pd.DataFrame] = pd.read_csv('../../../Documents/consolidatedMetrics.csv')
    #df = df.drop(labels=[7], axis=0,)
    fig: object = px.pie(df, values=' Test Count', names='Test Case Status')
    
    return fig

# If provided figures are not empty, prepares a Dash App and launches it with the provided figures
def LaunchDashApp(figs: list[object]) -> None:
    if(len(figs) == 0):
        print("No figures generated during run time. Exiting application.")
        return

    print("Creating Dash app...")

    from dash import Dash, html, dcc

    app = Dash(__name__)

    graphs = []
    for i in range(0, len(figs)):
        graphs.append(html.Div(dcc.Graph(
            id='graph-{}'.format(i),
            figure=figs[i]
        )))

    
    app.layout = html.Div(children=[
        html.H1(children='TestRail Metrics'),

        html.Div(children='''
            Test Suite Test Case Statuses
        '''),

        *graphs
    ])
        
    app.run_server(debug=False)