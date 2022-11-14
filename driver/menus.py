'''
Created on Nov 4, 2022

@author: Kyle O'Dell
'''

# Console UI to provide login credentials for TestRail
def Login() -> str:
    import getpass
    print("Please login to TestRail:")
    domain:str = input("TestRail domain: ")
    email:str = input("TestRail email: ")
    password:str = getpass.getpass("TestRail password: ")

    return (domain, email, password)

# Console UI for main menu
def MainMenu(runningOS:str, domain:str, email:str, password:str):
    toolActive:bool = True
    consolidatedMetricsPulledRecently = [False, False, False]

    jarArgs = ["java", "-jar", "../vMetrics.jar", runningOS, "", domain, email, password]

    figs = []
    while toolActive:
        (figs, toolActive, consolidatedMetricsPulledRecently) = MainMenuOptions(jarArgs, figs, toolActive, consolidatedMetricsPulledRecently)

    return figs

# Main menu options for user to select from
def MainMenuOptions(jarArgs, figs, toolActive:bool, consolidatedMetricsPulledRecently):
    import subprocess

    CONSOLIDATED_SUITE_METRICS = '1'
    SECTION_SUITE_METRICS = '2'
    CONSOLIDATE_RUN_METRICS = '3'
    QUIT_PROGRAM = '4'
    OPTION = 4
    
    jarArgs[OPTION] = input("\nWelcome to the TestRail Metrics Generator Tool!\n"
                     + "Please select an option:\n"
                     + "1. Provide consolidated section metrics\n"
                     + "2. Provide metrics per section\n"
                     + "3. Provide test run metrics\n"
                     + "4. Quit\n"
                     + "Input option (1-4) >> ")
        
    if jarArgs[OPTION] == CONSOLIDATED_SUITE_METRICS:
        if not consolidatedMetricsPulledRecently[int(CONSOLIDATED_SUITE_METRICS)]:
            subprocess.run(jarArgs)
            consolidatedMetricsPulledRecently[int(CONSOLIDATED_SUITE_METRICS)] = True
            
        figs.append(ConsolidatedMetricsGraphOptionsMenu())
    elif jarArgs[OPTION] == SECTION_SUITE_METRICS:
        subprocess.run(jarArgs)
    elif jarArgs[OPTION] == CONSOLIDATE_RUN_METRICS:
        subprocess.run(jarArgs)
    elif jarArgs[OPTION] == QUIT_PROGRAM:
        toolActive = False
        print("\nGoodbye\n")
    else:
        print("\nInvalid input! Please try again.\n")
            
    print()

    return (figs, toolActive, consolidatedMetricsPulledRecently)

# User options for type of desired graph
def ConsolidatedMetricsGraphOptionsMenu():
    from testRailMetricsGraphingTool import PieGraphConsolidatedMetrics
    from testRailMetricsGraphingTool import BarGraphConsolidatedMetrics

    option:str = input("\nSelect chart type to plot metrics:\n"
                 + "1. Pie chart\n"
                 + "2. Bar graph\n"
                 + "Input option >> ")
    
    if option == '1':
        fig = PieGraphConsolidatedMetrics()
    elif option == '2':
        fig = BarGraphConsolidatedMetrics()
    else:
        print("No valid option selected; defaulting to pie chart")
        fig = PieGraphConsolidatedMetrics()

    print("\nCreated and appended graph.\n")
    return fig