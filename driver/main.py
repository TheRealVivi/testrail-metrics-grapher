'''
Created on Nov 4, 2022

@author: Kyle O'Dell
'''

from menus import MainMenu, Login
from testRailMetricsGraphingTool import LaunchDashApp

if __name__ == '__main__':
    
    (domain, email, password) = Login()
    figs = MainMenu(domain, email, password)
    LaunchDashApp(figs)
    