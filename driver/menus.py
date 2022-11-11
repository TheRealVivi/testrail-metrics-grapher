def Login() -> str:
    print("Please login to TestRail:")
    domain:str = input("TestRail domain: ")
    email:str = input("TestRail email: ")
    password:str = input("TestRail password: ")

    return (domain, email, password)

def MainMenu(domain:str, email:str, password:str):
    import subprocess

    toolActive:bool = True
    consolidatedMetricsPulledRecently:bool = False

    figs = []
    while toolActive:
        option:str = input("\nWelcome to the TestRail Metrics Generator Tool!\n"
                     + "Please select an option:\n"
                     + "1. Provide consolidated section metrics\n"
                     + "2. Provide metrics per section\n"
                     + "3. Provide test run metrics\n"
                     + "4. Quit\n"
                     + "Input option (1-4) >> ")
        
        if option == '1':
            if not consolidatedMetricsPulledRecently:
                subprocess.run(["java", "-jar", "../vMetrics.jar", option, domain, email, password])
                consolidatedMetricsPulledRecently = True
            
            figs.append(ConsolidatedMetricsGraphOptionsMenu())
        elif option == '2':
            subprocess.run(["java", "-jar", "../vMetrics.jar", option, domain, email, password])
        elif option == '3':
            subprocess.run(["java", "-jar", "../vMetrics.jar", option, domain, email, password])
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