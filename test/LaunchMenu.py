'''
Created on Nov 4, 2022

@author: Kyle O'Dell
'''
import subprocess


def MainMenu():
    toolActive = True
    
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
            PieGraphConsolidatedMetrics()
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
    
def PieGraphConsolidatedMetrics():
    import plotly.express as px
    import pandas as pd
    df = pd.read_csv('../../../Documents/consolidatedMetrics.csv')
    df = df.drop(labels=[7], axis=0,)
    fig = px.pie(df, values=' Test Count', names='Test Case Status')
    fig.write_html('TestCaseStatus_PieFigure.html', auto_open=True)

if __name__ == '__main__':
    MainMenu()
    
    
    