'''
Name of file: real_estate_analyzer.py
Date created: August 29, 2018
Date last updated: September 25, 2018
Created by: James Ingram
Purpose of Program: Create pandas dataframe from csv file (output of real_estate_scraper.py) and perform exploratory data analysis
'''
# imports necessary pacakges, libraries, and dependencies
import datetime
import logging
import os 
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm 
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from scipy import stats

# created date format for filename
now = datetime.datetime.today().strftime("%m%d%y")

# creates log file and sets logging parameters
logging.basicConfig(
	filename='real_estate.log',
	level=logging.DEBUG,
	format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s', 
	datefmt="%Y-%m-%d %H:%M:%S")

# function to show menu and run all other functions
def main_program():
    # function to display a menu of options linked to other functions
    def display_options():
        # clears console screen for Windows (cls) or Linux (clear)
        try:
            os.system('cls')
        except:
            os.system('clear')
        # Displays menu and prompts user for input
        print("Main Menu\n")
        def menu(list,question):
            for item in list:
                print(1 + list.index(item), item)
            return input(question)
        while True:
            items = ["Display Listings","Display Pricing Data", "Display Bedroom Data", "Display Bathroom Data", "Display Area Data", "Display Correlation Matrix", "Display Linear Regression Model(s)", "Predict House Price", "Exit"]
            choice = menu(items,"\nPlease make a selection from the list above:\n>")
            try:
                choice = int(choice)
                break
            except:
                print("Invalid selection, please try again\n")
                continue
        print("")
        # User makes a selection
        if choice == 1:
            display_listings()
        elif choice == 2:
            display_prices()
        elif choice == 3:
            display_beds()
        elif choice == 4:
            display_baths()
        elif choice == 5:
            display_area()
        elif choice == 6:
            display_comatrix()
        elif choice == 7:
            display_linear()
        elif choice == 8:
            predict_linear()
        elif choice == 9:
            exit_choice = input("Analyze another city?\n>")
            if exit_choice.lower().startswith('n'):
                compare = input("\nWould you like to compare all cities?\n>")
                if compare.lower().startswith('y'):
                    try:
                        os.system('python real_estate_compare.py')
                    except:
                        print("\nUnable to load program at this time")
                        print("Goodbye!")
                        quit()
                else:
                    try:
                        os.system('cls')
                    except:
                        os.system('clear')
                    print("Goodbye!")
                    quit()
            else:
                main_program()
        else:
            print("Invalid selection, please try again")
            display_options()
    # function to display real estate listings in pandas dataframe
    def display_listings():
        try:
            os.system('cls')
        except:
            os.system('clear')
        # prompts user to enter number of listings to display
        while True:
            list_num = input("How many listings would you like to display?\n>")
            try:
                list_num = int(list_num)
                break
            except:
                print("Error:",list_num,"is not a valid number")
                continue
        # displays listings
        print(df2[:list_num])
        # prompts user to return to menu screen
        input("\nPress <enter> to return to main menu:\n>")
        display_options()

    # function to display price data to user
    def display_prices():
        # clears console screen for Windows (cls) or Linux (clear)
        try:
            os.system('cls')
        except:
            os.system('clear')
        # Displays menu and prompts user for input
        print("Pricing Data\n")
        def menu(list,question):
            for item in list:
                print(1 + list.index(item), item)
            return input(question)
        while True:
            items = ["Descriptive Statistics","Display Pricing Boxplot", "Display Pricing Frequency Histogram", "Return to Main Menu"]
            choice = menu(items,"\nPlease make a selection from the list above:\n>")
            try:
                choice = int(choice)
                break
            except:
                print("Invalid selection, please try again\n")
                continue
        print("")
        # User makes a selection
        if choice == 1:
            try:
                os.system('cls')
            except:
                os.system('clear')
            #  calculates and displays min, mean, median, and max prices
            min_price = '{0:.2f}'.format(df2['price'].min())
            avg_price = '{0:.2f}'.format(df2['price'].mean())
            med_price = '{0:.2f}'.format(df2['price'].median())
            max_price = '{0:.2f}'.format(df2['price'].max())
            print("Housing Costs:\n")
            print("The minumum price is: $" + min_price)
            print("The average price is: $" + avg_price)
            print("The median price is: $" + med_price)
            print("The maximum price is: $" + max_price)
            print()
            input("Press <enter> to return to menu:\n>")
            display_prices()
        elif choice == 2:
            try:
                os.system('cls')
            except:
                os.system('clear')
            print("Displaying Housing Prices Boxplot...")
            # creates figure showing boxplot of housing prices
            fig1 = plt.figure(1, figsize=(10,8))
            ax1 = fig1.add_subplot(111)
            ax1.set_xlabel("Figure 1: Housing Prices (USD)")
            ax1.get_yaxis().tick_left()
            bp = ax1.boxplot(df2['price'])
            # displays figure to user
            plt.show()
            # saves figure to file
            try:
                fig1.savefig('fig1-' + fname + '.png', bbox_inches='tight')
                # displays file creation to user and appends log file
                print("Created file: fig1.png")    
                logging.info("Figure 1 successfully created")
            except:
                print("Unable to save file: fig1.png")
                logging.debug("Figure 1 not saved")
            input("\nPress <enter> to return to menu:\n>")
            display_prices()
        elif choice == 3:
            try:
                os.system('cls')
            except:
                os.system('clear')
            print("Displaying Housing Prices Frequency Histogram")
            # creates figure showing histogram of housing price distribution
            fig2 = plt.figure(2, figsize=(10,8))
            ax2 = fig2.add_subplot(111)
            ax2.set_xlabel("Figure 2: Housing Prices (USD)")
            ax2.set_ylabel("Frequency")
            ht = ax2.hist(df2['price'])
            # displays figure to user
            plt.show()
            # saves figure to file
            try:
                fig2.savefig('fig2-' + fname + '.png', bbox_inches='tight')
                print("Created file: fig2.png")
                logging.info("Figure 2 successfully created")
            except:
                print("Unable to save file: fig2.png")
                logging.debug("Figure 2 not saved")
            input("\nPress <enter> to return to menu:\n>")
            display_prices()
        elif choice == 4:
            display_options()
        else:
            print("Invalid selection, please try again")
            display_prices()

    # function to display bedroom data to user
    def display_beds():
        # clears console screen for Windows (cls) or Linux (clear)
        try:
            os.system('cls')
        except:
            os.system('clear')
        # Displays menu and prompts user for input
        print("Bedroom Data\n")
        def menu(list,question):
            for item in list:
                print(1 + list.index(item), item)
            return input(question)
        while True:
            items = ["Descriptive Statistics","Display Bedroom Boxplot", "Display Bedroom Frequency Histogram", "Display Relationship Between Bedrooms and Price", "Return to Main Menu"]
            choice = menu(items,"\nPlease make a selection from the list above:\n>")
            try:
                choice = int(choice)
                break
            except:
                print("Invalid selection, please try again\n")
                continue
        print("")
        # User makes a selection
        if choice == 1:
            try:
                os.system('cls')
            except:
                os.system('clear')
            # calculates and displays min, mean, median, and max bedrroms
            min_beds = int(df2['beds'].min())
            avg_beds = int(df2['beds'].mean())
            med_beds = int(df2['beds'].median())
            max_beds = int(df2['beds'].max())
            print("Bedrooms:\n")
            print("The minimum number of bedrooms is:",min_beds)
            print("The average number of bedrooms is:",avg_beds)
            print("The median number of bedrooms is:",med_beds)
            print("The maximum number of bedrooms is:",max_beds)
            print()
            # displays average price for min, mean, median, and max bedrooms
            print("The average price for a", min_beds, "bedroom home is: $",'{0:.2f}'.format(df2[df2['beds']==min_beds]['price'].mean()))
            print("The average price for a", avg_beds, "bedroom home is: $",'{0:.2f}'.format(df2[df2['beds']==avg_beds]['price'].mean()))
            print("The average price for a", med_beds, "bedroom home is: $",'{0:.2f}'.format(df2[df2['beds']==med_beds]['price'].mean()))
            print("The average price for a", max_beds, "bedroom home is: $",'{0:.2f}'.format(df2[df2['beds']==max_beds]['price'].mean()))
            print()
            input("Press <enter> to return to menu:\n>")
            display_beds()
        elif choice == 2:
            try:
                os.system('cls')
            except:
                os.system('clear')
            print("Displaying Bedrooms Boxplot...")
            # creates figure displaying boxplot of bedrooms
            fig3 = plt.figure(3, figsize=(10,8))
            ax3 = fig3.add_subplot(111)
            ax3.set_xlabel("Figure 3: Number of Bedrooms")
            ax3.get_yaxis().tick_left()
            bp2 = ax3.boxplot(df2['beds'])
            # displays figure to user
            plt.show()
            # saves figure to file
            try:
                fig3.savefig('fig3-' + fname + '.png', bbox_inches='tight')
                print("Created file: fig3.png")
                logging.info("Figure 3 successfully created")
            except:
                print("Unable to save file: fig3.png")
                logging.debug("Figure 3 not saved")
            input("\nPress <enter> to return to menu:\n>")
            display_beds()
        elif choice == 3:
            try:
                os.system('cls')
            except:
                os.system('clear')
            print("Displaying Bedrooms Frequency Histogram...")  
            # creates figure displaying histogram of bedroom frequency distribution
            fig4 = plt.figure(4, figsize=(10,8))
            ax4 = fig4.add_subplot(111)
            ax4.set_xlabel("Figure 4: Number of Bedrooms")
            ax4.set_ylabel("Frequency")
            ht2 = ax4.hist(df2['beds'])
            # displays figure to suer
            plt.show()
            # saves figure to file
            try:
                fig4.savefig('fig4-' + fname + '.png', bbox_inches='tight')
                print("Created file: fig4.png")
                logging.info("Figure 4 successfully created")
            except:
                print("Unable to save file: fig4.png")
                logging.debug("Figure 4 not saved")
            input("\nPress <enter> to return to menu:\n>")
            display_beds()
        elif choice == 4:
            try:
                os.system('cls')
            except:
                os.system('clear')
            print("Displaying Relationship Between Bedrooms and Price...")     
            # creates figure displaying relationship between number of bedrooms and price
            fig5 = plt.figure(5, figsize=(10,8))
            X = df2['beds']
            Y = df2['price']
            plt.scatter(X,Y)
            # displays figure to user
            plt.show()
            # saves figure to file
            try:
                fig5.savefig('fig5-' + fname + '.png', bbox_inches='tight')  
                print("Created file: fig5.png")
                logging.info("Figure 5 successfully created")
            except:
                print("Unable to save file: fig5.png")
                logging.debug("Figure 5 not saved")
            input("\nPress <enter to return to menu:\n>")
            display_beds()
        elif choice == 5:
            display_options()
        else:
            print("Invalid selection, please try again")
            display_beds()    

    # function to display bathroom data to user
    def display_baths():
        # clears console screen for Windows (cls) or Linux (clear)
        try:
            os.system('cls')
        except:
            os.system('clear')
        # Displays menu and prompts user for input
        print("Bathroom Data\n")
        def menu(list,question):
            for item in list:
                print(1 + list.index(item), item)
            return input(question)
        while True:
            items = ["Descriptive Statistics","Display Bathroom Boxplot", "Display Bathroom Frequency Histogram", "Display Relationship Between Bathrooms and Price", "Return to Main Menu"]
            choice = menu(items,"\nPlease make a selection from the list above:\n>")
            try:
                choice = int(choice)
                break
            except:
                print("Invalid selection, please try again\n")
                continue
        print("")
        # User makes a selection
        if choice == 1:
            try:
                os.system('cls')
            except:
                os.system('clear')
            # calculates and displays min, mean, median, and max number of bathrooms
            min_baths = int(df2['baths'].min())
            avg_baths = int(df2['baths'].mean())
            med_baths = int(df2['baths'].median())
            max_baths = int(df2['baths'].max())
            print("Bathrooms:\n")
            print("The minimum number of bathrooms is:",min_baths)
            print("The average number of bathrooms is:",avg_baths)
            print("The median number of bathrooms is:",med_baths)
            print("The maximum number of bathrooms is:",max_baths)
            print()
            # displays average price for properties with min, mean, median, and max number of bathrooms
            print("The average price for a", min_baths, "bathroom home is: $",'{0:.2f}'.format(df2[df2['baths']==min_baths]['price'].mean()))
            print("The average price for a", avg_baths, "bathroom home is: $",'{0:.2f}'.format(df2[df2['baths']==avg_baths]['price'].mean()))
            print("The average price for a", med_baths, "bathroom home is: $",'{0:.2f}'.format(df2[df2['baths']==med_baths]['price'].mean()))
            print("The average price for a", max_baths, "bathroom home is: $",'{0:.2f}'.format(df2[df2['baths']==max_baths]['price'].mean()))
            print()
            input("Press <enter> to return to menu:\n>")
            display_baths()
        elif choice == 2:
            try:
                os.system('cls')
            except:
                os.system('clear')
            print("Displaying Bathrooms Boxplot...")
            # creates figure displaying boxplot of bathroom data
            fig6 = plt.figure(6, figsize=(10,8))
            ax6 = fig6.add_subplot(111)
            ax6.set_xlabel("Figure 6: Number of Bathrooms")
            ax6.get_yaxis().tick_left()
            bp3 = ax6.boxplot(df2['baths'])
            # displays figure to user
            plt.show()
            # saves figure to file
            try:
                fig6.savefig('fig6-' + fname + '.png', bbox_inches='tight')
                print("Created file: fig6.png")
                logging.info("Figure 6 successfully created")
            except:
                print("Unable to save file: fig6.png")
                logging.debug("Figure 6 not saved")
            input("\nPress <enter> to return to menu:\n>")
            display_baths()
        elif choice == 3:
            try:
                os.system('cls')
            except:
                os.system('clear')
            print("Displaying Bathrooms Frequency Histogram...")
            # creates figure displaying histogram of bathroom frequency distribution
            fig7 = plt.figure(7, figsize=(10,8))
            ax7 = fig7.add_subplot(111)
            ax7.set_xlabel("Figure 7: Number of Bathrooms")
            ax7.set_ylabel("Frequency")
            ht3 = ax7.hist(df2['baths'])
            # displays plot to user
            plt.show()
            # saves figure to file
            try:
                fig7.savefig('fig7-' + fname + '.png', bbox_inches='tight')
                print("Created file: fig7.png")
                logging.info("Figure 7 successfully created")
            except:
                print("Unable to save file: fig7.png")
                logging.debug("Figure 7 not saved")
            input("\nPress <enter> to return to menu:\n>")
            display_baths()
        elif choice == 4:
            try:
                os.system('cls')
            except:
                os.system('clear')
            print("Displaying Relationship Between Bathrooms and Price...")
            # create figure displaying relationship between number of bathrooms and price
            fig8 = plt.figure(8, figsize=(10,8))
            X = df2['baths']
            Y = df2['price']
            plt.scatter(X,Y)
            # displays figure to user
            plt.show()
            # saves figure to file
            try:
                fig8.savefig('fig8-' + fname + '.png', bbox_inches='tight')
                print("Created file: fig8.png")
                logging.info("Figure 8 successfully created")
            except:
                print("Unable to save file: fig8.png")
                logging.debug("Figure 8 not saved")  
            input("\nPress <enter> to return to menu:\n>")
            display_baths()   
        elif choice == 5:
            display_options()
        else:
            print("Invalid selection, please try again")
            display_baths()    

    # function to display property area data
    def display_area():
        # clears console screen for Windows (cls) or Linux (clear)
        try:
            os.system('cls')
        except:
            os.system('clear')
        # Displays menu and prompts user for input
        print("Area Data\n")
        def menu(list,question):
            for item in list:
                print(1 + list.index(item), item)
            return input(question)
        while True:
            items = ["Descriptive Statistics","Display Area Boxplot", "Display Area Frequency Histogram", "Display Relationship Between Area and Price", "Return to Main Menu"]
            choice = menu(items,"\nPlease make a selection from the list above:\n>")
            try:
                choice = int(choice)
                break
            except:
                print("Invalid selection, please try again\n")
                continue
        print("")
        # User makes a selection
        if choice == 1:
            try:
                os.system('cls')
            except:
                os.system('clear')
            # calculates and displays min, mean, median, and max areas (in sqft)
            min_area = int(df2['area'].min())
            avg_area = int(df2['area'].mean())
            med_area = int(df2['area'].median())
            max_area = int(df2['area'].max())
            print("Area:\n")
            print("The minimum area is:",min_area,"sq ft")
            print("The average area is:",avg_area,"sq ft")
            print("The median area is:",med_area,"sq ft")
            print("The maximum area is:",max_area, "sq ft")
            print()
            # displays average price for properties with min, mean, median, and max number of bathrooms
            print("The average price for a", min_area, "square foot home is: $",'{0:.2f}'.format(df2[df2['area']==min_area]['price'].mean()))
            print("The average price for a 2000 square foot home is: $",'{0:.2f}'.format(df2[df2['area']==2000]['price'].mean()))
            print("The average price for a", max_area, "square foot home is: $",'{0:.2f}'.format(df2[df2['area']==max_area]['price'].mean()))
            print()
            input("Press <enter> to return to menu:\n>")
            display_area()
        elif choice == 2:
            try:
                os.system('cls')
            except:
                os.system('clear')
            print("Displaying Area Boxplot...")   
            # creates figure displaying boxplot of area data
            fig9 = plt.figure(9, figsize=(10,8))
            ax9 = fig9.add_subplot(111)
            ax9.set_xlabel("Figure 9: Area (sq ft)")
            ax9.get_yaxis().tick_left()
            bp4 = ax9.boxplot(df2['area'])
            # displays figure to user
            plt.show()
            # saves figure to file
            try:
                fig9.savefig('fig9-' + fname + '.png', bbox_inches='tight')
                print("Created file: fig9.png")
                logging.info("Figure 9 successfully created")
            except:
                print("Unable to save file: fig9.png")
                logging.debug("Figure 9 not saved")
            input("\nPress <enter> to return to menu:\n>")
            display_area()
        elif choice == 3:
            try:
                os.system('cls')
            except:
                os.system('clear')
            print("Displaying Area Frequency Histogram...")    
            # creates figure displaying histogram of area frequency
            fig10 = plt.figure(10, figsize=(10,8))
            ax10 = fig10.add_subplot(111)
            ax10.set_xlabel("Figure 10: Area (sq ft)")
            ax10.set_ylabel("Frequency")
            ht4 = ax10.hist(df2['area'])
            # displays figure to user
            plt.show()
            # saves figure to file
            try:
                fig10.savefig('fig10-' + fname + '.png', bbox_inches='tight')
                print("Created file: fig10.png")
                logging.info("Figure 10 successfully created")
            except:
                print("Unable to save file: fig10.png")
                logging.debug("Figure 10 not saved")
            input("\nPress <enter> to return to menu:\n>")
            display_area()
        elif choice == 4:
            try:
                os.system('cls')
            except:
                os.system('clear')
            print("Displaying Relationship Between Area and Price...") 
            # creates figure displaying relationship between area and price
            fig11 = plt.figure(11, figsize=(10,8))
            X = df2['area']
            Y = df2['price']
            plt.scatter(X,Y)
            # displays figure to user
            plt.show()
            # saves figure to file
            try:
                fig11.savefig('fig11-' + fname + '.png', bbox_inches='tight')
                print("Created file: fig11.png")
                logging.info("Figure 11 successfully created")
            except:
                print("Unable to save file: fig11.png")
                logging.debug("Figure 11 not saved")
            input("\nPress <enter> to return to menu:\n>")
            display_area()
        elif choice == 5:
            display_options()
        else:
            print("Invalid selection, please try again")
            display_area()  

    # function to create and display correlation matrix
    def display_comatrix():
        try:
            os.system('cls')
        except:
            os.system('clear')

        # create and display correlation matrix text values
        print("Correlation Matrix:\n")
        print(df2.corr())

        # display heatmap correlation matrix
        f, ax = plt.subplots(figsize=(10,8))
        corr= df2.corr()
        sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220,10, as_cmap=True), square=True, ax=ax)
        plt.show()
        logging.info("Correlation matrix created")
        f.savefig('fig12-' + fname + '.png', bbox_inches='tight')
        # prompts user to return to main menu
        input("\nPress <enter> to return to main menu:\n>")
        display_options()

    # function to create and display linear regression models
    def display_linear():
        try:
            os.system('cls')
        except:
            os.system('clear')
        print("Display Linear Regression Model:\n")

        def linear_all():
            try:
                os.system('cls')
            except:
                os.system('clear')
            # sets "price" as dependent variable
            target = pd.DataFrame(df2, columns=["price"])
            # sets "beds", "baths", and "area" as independent variables
            X = df2[["beds", "baths", "area"]]
            y = target["price"]
            # fits the model
            model = sm.OLS(y,X).fit()
            # displays model summary table
            print(model.summary())
            logging.info("Linear regression model with beds, baths, and area vs. price created")
            # return to menu
            input("\nPress <enter> to return to model menu:\n>")
            display_linear()

        def linear_beds():
            try:
                os.system('cls')
            except:
                os.system('clear')
            # sets "price" as dependent variable
            target = pd.DataFrame(df2, columns=["price"])
            # sets "beds" as independent variables
            X = df2[["beds"]]
            y = target["price"]
            # fits the model
            model = sm.OLS(y,X).fit()
            # displays model summary table
            print(model.summary())
            logging.info("Linear regression model with beds vs. price created")
            # return to menu
            input("\nPress <enter> to return to model menu:\n>")
            display_linear()

        def linear_baths():
            try:
                os.system('cls')
            except:
                os.system('clear')
            # sets "price" as dependent variable
            target = pd.DataFrame(df2, columns=["price"])
            # sets "baths" as independent variables
            X = df2[["baths"]]
            y = target["price"]
            # fits the model
            model = sm.OLS(y,X).fit()
            # displays model summary table
            print(model.summary())
            logging.info("Linear regression model with baths vs. price created")
            # return to menu
            input("\nPress <enter> to return to model menu:\n>")
            display_linear()

        def linear_area():
            try:
                os.system('cls')
            except:
                os.system('clear')
            # sets "price" as dependent variable
            target = pd.DataFrame(df2, columns=["price"])
            # sets "area" as independent variables
            X = df2[["area"]]
            y = target["price"]
            # fits the model
            model = sm.OLS(y,X).fit()
            # displays model summary table
            print(model.summary())
            logging.info("Linear regression model with area vs. price created")
            # return to menu
            input("\nPress <enter> to return to model menu:\n>")
            display_linear()

        def menu(list,question):
            for item in list:
                print(1 + list.index(item), item)
            return input(question)
        while True:
            items = ["Beds, Baths, and Area vs. Price", "Beds vs. Price", "Baths vs. Price", "Area vs. Price", "Return to Main Menu" ]
            choice = menu(items,"\nPlease make a selection from the list above:\n>")
            try:
                choice = int(choice)
                break
            except:
                print("Invalid selection, please try again\n")
                continue
        print()

        # User makes a selection
        if choice == 1:
            linear_all()
        elif choice == 2:
            linear_beds()
        elif choice == 3:
            linear_baths()
        elif choice == 4:
            linear_area()
        elif choice == 5:
            display_options()
        else:
            display_linear()

    # function to predict housing price from user input (based on linear regression model)
    def predict_linear():
        try:
            os.system('cls')
        except:
            os.system('clear')
        print("Home Price Prediction\n")
        print("Choose independent variable:")
        def menu(list,question):
            for item in list:
                print(1 + list.index(item), item)
            return input(question)
        while True:
            items = ["Beds", "Baths", "Area"]
            choice = menu(items,"\nPlease make a selection from the list above:\n>")
            try:
                choice = int(choice)
                break
            except:
                print("Invalid selection, please try again\n")
                continue
        print()

        # User makes a selection
        if choice == 1:
            X = df2[["beds"]]
            pred_text = "Enter number of bedrooms:\n>"
        elif choice == 2:
            X = df2[["baths"]]
            pred_text = "Enter number of bathrooms:\n>"
        elif choice == 3:
            X = df2[["area"]]
            pred_text = "Enter area (sqft):\n>"
        else:
            predict_linear()

        target = pd.DataFrame(df2, columns=["price"])
        y = target["price"]
        model = sm.OLS(y,X).fit()
        X2 = []

        while True:
            pred_var = input(pred_text)
            try:
                X2.append(int(pred_var))
                pred2 = model.predict(X2)
                for i in pred2:
                    print("\nEstimated Price: $"+"{:.2f}".format(i))
                break
            except:
                print("Invalid entry\n")
                continue
        again = input("\nMake another prediction? (y/n)\n>")
        if again.lower().startswith("y"):
            predict_linear()
        else:
            input("\nPress <enter> to return to main menu:\n>")
            display_options()
    try:
        os.system('cls')
    except:
        os.system('clear')

    print("Real Estate Data Analysis")
    print("Choose city:\n")
    def menu(list,question):
        for item in list:
            print(1 + list.index(item), item)
        return input(question)
    while True:
        items = ["Albany, NY", "Binghamton, NY", "Buffalo, NY", "Syracuse, NY"]
        choice = menu(items,"\nPlease make a selection from the list above:\n>")
        try:
            choice = int(choice)
            break
        except:
            print("Invalid selection, please try again\n")
            continue
    print()

    # User makes a selection
    if choice == 1:
        fname = "albany"
    elif choice == 2:
        fname = "binghamton"
    elif choice == 3:
        fname = "buffalo"
    elif choice == 4:
        fname = "syracuse"
    else:
        menu()

    try:
        os.system('cls')
    except:
        os.system('clear')

    # reads .csv file created by real_estate_scraper.py and creates Pandas dataframe
    try:
        df = pd.read_csv("properties-" + fname + "-" + now + ".csv")
        # displays number of records retrieved from file
        print("Retrieved",len(df),"records from 'properties-" + fname + "-" + now + ".csv'")
        logging.info("Records successfully retrieved from file")
    except:
        print("Unable to load files")
        logging.debug("Records not retrieved from file")
        quit()

    # extracts data where title is "House For Sale"
    df = df[df['title']=="House For Sale"]
    # gets count of "House For Sale" records
    house_count = len(df)
    # displays count to user
    print(house_count, "records contain data on houses for sale")
    # sets column names, removes null values, and stores as new dataframe
    df2 = df[['title', 'address','city','state','zip_code','beds','baths','area','price']].dropna()
    # calculates number of null values based on difference between both dataframes
    na_count = abs(len(df) - len(df2))
    # displays number of null values to user
    print(na_count,"records contain null values")
    # prompts user to delete rows with null values or replace them with average values
    del_null = input("Delete or Replace null values?\n>")
    if del_null.lower().startswith('r'):
        # replaces null values with average values
        df2 = df.fillna(df.mean())
        # finds outliers (values with z-score >= 3) and excludes them from dataframe
        df2 = df2[(np.abs(stats.zscore(df2["price"])) < 2)]
        df2 = df2[(np.abs(stats.zscore(df2["beds"])) < 2)]
        df2 = df2[(np.abs(stats.zscore(df2["baths"])) < 2)]
        df2 = df2[(np.abs(stats.zscore(df2["area"])) < 2)]
        new_count = len(df2)
        print("\nReplacing", na_count,"null values with average values...")
        outlier_count = len(df) - len(df2)
        print("Removing",outlier_count, "records containing outiers...")
        print("..."+ str(new_count) + " records remaining")
        logging.info("Records containing null values replaced")
        input("Press <enter> to continue:\n>")
        display_options()
    elif del_null.lower().startswith('d'):
        # uses dataframe where null values have been deleted
        # deletes outliers based on z-score
        df2 = df2[(np.abs(stats.zscore(df2["price"])) < 3)]
        df2 = df2[(np.abs(stats.zscore(df2["beds"])) < 3)]
        df2 = df2[(np.abs(stats.zscore(df2["baths"])) < 3)]
        df2 = df2[(np.abs(stats.zscore(df2["area"])) < 3)]
        new_count = len(df) - na_count
        outlier_count = new_count - len(df2)
        print("\nRemoving",na_count,"records containing null values...")
        print("Removing",outlier_count,"records containing outliers...")
        print("..."+ str(len(df2)) + " records remaining")
        logging.info("Records containing null values removed")
        input("Press <enter> to continue:\n>")
        display_options()
    else: 
        print("Invalid input")
        input("Press <enter> to continue:\n>")
        main_program()

###############################
# Program execution begins here
###############################
main_program()
