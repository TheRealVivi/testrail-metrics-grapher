'''
Created on Nov 4, 2022

@author: kodel
'''

def BarGraphConsolidatedMetrics():
    import plotly.express as px
    import pandas as pd

    df = pd.read_csv('../../../Documents/consolidatedMetrics.csv')
    df = df.drop(labels=[7], axis=0,)
    fig = px.bar(df, x='Test Case Status', y=' Test Count')
    
    return fig

# Adds pie chart to subplot
def PieGraphConsolidatedMetrics():
    import plotly.express as px
    import pandas as pd

    df = pd.read_csv('../../../Documents/consolidatedMetrics.csv')
    df = df.drop(labels=[7], axis=0,)
    fig = px.pie(df, values=' Test Count', names='Test Case Status')
    
    return fig


def LaunchDashApp(figs):
    if(len(figs) == 0):
        print("No figures generated during run time. Exiting application.")
        return

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
  