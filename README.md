# **<font color = 'DarkBlue'> <p align="center"> United States COVID-19 Outcome on County and Congressional District Levels with Related Demographics</p> </font>** 
In this project I create maps and graphs to visualize COVID-19 data and related Demographics. My aim is to create visulizations in a way that informs analysis. The demographics data I include are factors that are known to or can possibly (indirectly) affect COVID-19 outcome. For example, age, race, and income are known factors that affect the outcome. On the other hand, I hypothesize that political leanings might indirectly affect the outcome as they could affect attitude toward vaccinations and other preventive measures to slow the spread of the virus.<br>
I chose to use congressional districts for two reasons: 1) congressional districts are in theory drawn to have approximately equal population allowing for a better data comparison; and 2) It allows me to use a simple quantitave measure of the political leanings of each district, the Partisan Voting Index (PVI).<br>
## **<font color = 'DarkBlue'> Prerequisites </font>**
### **<font color = 'DarkBlue'> Software prerequisites </font>**
* Jupyter notebook/IPython
* Pandas
* Sodapy
* Plotly and Plotly Express
* Termcolor
### **<font color = 'DarkBlue'> Data prerequisites </font>**
- Download the Partisan Voting Index data from The Cook Political Report website https://www.cookpolitical.com/pvi-map-and-district-list. Click ‘Get the data’ at the end of the table in the link above. This should download a file named ‘data-5vPn3.csv’.
- Obtain a key from the Virginia Department of Health to be able to pull out the updated COVID data. Go to https://dev.socrata.com/foundry/data.virginia.gov/bre9-aqqr and sign up for an App Token. Insert your given App Token, Key ID, and Key Secret in the indicated places in the “MyAppToken.txt” file. These are your PERSONAL identifiers.
## **<font color = 'DarkBlue'> Usage </font>**
To run the code, open Main.ipynb and run all cells. 
### **<font color = 'DarkBlue'> Note </font>**
While demographics data can be obtained for all US states, COVID-19 data is currently only available for the state of Virginia. <br> The first cell in the Main file runs all the necessary functions. The second cell obtains all the necessary DataFrames to plot the data. The third cell displays the selected visualization. Currently, only [map plots](Widgets.md) are available.<br>
Most data are pulled directly from the source and saved to local directory in json format for quicker future access. So, the first run will take few minutes but will be much faster once the data are available locally.

## **<font color = 'DarkBlue'> Future Additions </font>**
* When the ‘Partisan Voting Index’ option for Data Type is selected, the Log Scale button will either disappear or be fixed to False (i.e., cannot be checked).
* When the ‘County’ option for Level is selected, the ‘Partisan Voting Index’ option for Data Type will no longer be available.
* Time series plots, correlation matrices, and other analysis will be added.
* Cumulative cases, hospitalizations, and deaths within a particular group in the different counties or districts will be added.
* Vaccination data will be added.
* PCR tests encountered and percent positivity data will be added.
* Variant of concern data might be added.
* Data on outbreaks in different settings might be added.
* A date range for the total cases, hospitalizations, and deaths, and their corresponding ratios will be added.
* COVID-19 data for more US states will be added, not just for Virginia.
* Widgets to select the state and type of visualization will be added.
* Demographic data beyond 2019 will be added.
* Health districts might be added to the Level option of the state map.
* Ability to display two maps simultaneously might be added.


