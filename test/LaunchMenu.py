'''
Created on Nov 4, 2022

@author: Kyle O'Dell
'''
import subprocess


def MainMenu():
    from dash import Dash, html, dcc
    app = Dash(__name__)

    toolActive = True
    figs = []
    while toolActive:
        option = input("Welcome to the TestRail Metrics Generator Tool!\n"
                     + "Please select an option:\n"
                     + "1. Print consolidated section metrics\n"
                     + "2. Print metrics per section\n"
                     + "3. Print test run metrics\n"
                     + "4. Quit\n"
                     + "Input option (1-4) >> ")
        
        if option == '1':
            subprocess.run(["java", "-jar", "../vMetrics.jar", "1"])
            figs.append(PieGraphConsolidatedMetrics())
        elif option == '2':
            subprocess.run(["java", "-jar", "../vMetrics.jar", "2"])
        elif option == '3':
            subprocess.run(["java", "-jar", "../vMetrics.jar", "3"])
        elif option == '4':
            toolActive = False
        else:
            print("\nInvalid input! Please try again.\n")
            
        print()

    print("\nGoodbye\n")

    graphs = []
    for i in range(0, len(figs)):
        graphs.append(html.Div(dcc.Graph(
            id='graph-{}'.format(i),
            figure=figs[i]
        )))

    if(len(graphs) != 0):
        app.layout = html.Div(children=[
            html.H1(children='Hello Dash'),

            html.Div(children='''
                Dash: A web app framework for your data.
            '''),


            *graphs
            
        ])
        
        app.run_server(debug=False)
    

# Adds pie chart to subplot
def PieGraphConsolidatedMetrics():
    import plotly.express as px
    import pandas as pd

    df = pd.read_csv('../../../Documents/consolidatedMetrics.csv')
    df = df.drop(labels=[7], axis=0,)
    fig = px.pie(df, values=' Test Count', names='Test Case Status')
    
    return fig
    

if __name__ == '__main__':
    MainMenu()
    
    
    