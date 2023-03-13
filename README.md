# **<font color = 'DarkBlue'> <p align="center"> Welcome to my COVID19 Playground</p> </font>** 
In this project I create maps and graphs to visualize COVID-19 data and related Demographics. My aim is to create visualizations in a way that informs analysis. The demographics data I include are factors that are known to or can possibly (indirectly) affect COVID-19 outcome. For example, age, race, and income are known factors that affect the outcome. On the other hand, I hypothesize that political leanings might indirectly affect the outcome as they could affect attitude toward vaccinations and other preventive measures to slow the spread of the virus.<br>
I chose to use congressional districts for two reasons: 1) congressional districts are in theory drawn to have approximately equal population allowing for a better data comparison; and 2) It allows me to use a simple quantitative measure of the political leanings of each district, the Partisan Voting Index (PVI).<br>
## **<font color = 'DarkBlue'> Prerequisites </font>**
### **<font color = 'DarkBlue'> Software prerequisites </font>**
* jupyter notebook/IPython
* pandas
* sodapy
* plotly and plotly express
* termcolor
* ipywidgets
* scikit-learn
* scipy
* pingouin
* All requirements can also be imported from the environment file, <font color = 'DarkGreen'>Pandemic_env.yml </font>
### **<font color = 'DarkBlue'> Data prerequisites </font>**
- Download the Partisan Voting Index data from The Cook Political Report website https://www.cookpolitical.com/pvi-map-and-district-list. Click ‘Get the data’ at the end of the table in the link above. This should download a file named <font color = 'DarkGreen'>‘data-5vPn3.csv’</font>. This provides the 2017 PVI's. For the 2020/2022 PVI's, I manually copied and stored the data in filenames <font color = 'DarkGreen'>'PVIs_2022.csv'</font> for the Districts and <font color = 'DarkGreen'>'PVI_VA_Counties_2020.csv'</font> for the VA counties.
- Obtain a key from the Virginia Department of Health to be able to pull out the updated COVID data. Go to https://dev.socrata.com/foundry/data.virginia.gov/bre9-aqqr and sign up for an App Token. Insert your given App Token, Key ID, and Key Secret in the indicated places in the <font color = 'DarkGreen'>“MyAppToken.txt”</font> file. These are your PERSONAL identifiers.
## **<font color = 'DarkBlue'> Usage </font>**
To run the code, open Main.ipynb in jupyter notebook and run all cells. 
### **<font color = 'DarkBlue'> Note </font>**
While demographics data can be obtained for all US states, COVID-19 data is currently only available for the state of Virginia. <br> The first cell in the Main file runs all the necessary functions. The second cell obtains all the necessary DataFrames to plot the data. The rest of the cells display the selected [visualizations](Widgets.md).<br>
Most data are pulled directly from the source and saved to local directory in json format for quicker future access. So, the first run will take few minutes but will be much faster once the data are available locally.


