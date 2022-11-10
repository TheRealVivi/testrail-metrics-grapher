def MainMenu():
    import subprocess

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
            figs.append(ConsolidatedMetricsGraphOptionsMenu())
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

    return figs

# User options for type of desired graph
def ConsolidatedMetricsGraphOptionsMenu():
    from testRailMetricsGraphingTool import PieGraphConsolidatedMetrics
    from testRailMetricsGraphingTool import BarGraphConsolidatedMetrics

    option = input("Select chart type to plot metrics:\n"
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

    return fig