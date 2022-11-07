'''
Created on Nov 4, 2022

@author: kodel
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
        elif option == '2':
            subprocess.run(["java", "-jar", "../vMetrics.jar", "2"])
        elif option == '3':
            subprocess.run(["java", "-jar", "../vMetrics.jar", "3"])
        elif option == '4':
            toolActive = False
            
        print()
        
    print("\nGoodbye\n")
    

if __name__ == '__main__':
    MainMenu()
    
    