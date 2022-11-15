'''
Created on Nov 4, 2022

@author: Kyle O'Dell
'''

from menus import MainMenu, Login
from testRailMetricsGraphingTool import LaunchDashApp
import platform

if __name__ == '__main__':
    runningOS: str = platform.system()
    (domain, email, password) = Login()
    figs: list[object] = MainMenu(runningOS, domain, email, password)
    LaunchDashApp(figs)
    