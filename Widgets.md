## **<font color = 'DarkBlue'> Cell #3 </font>**
1. Select the ***Scope*** of the map: County or Congressional District
1. Select the ***Data Type***. This will change the available options in the dropdown menu for ***data***
   1. GEO inludes
      * total population of each county/congressional district<br> <font color = blue>The population data is obtained from the United States Census Bureau, American Community Survey (ACS) 5-year data.</font>
      * land area
      * water area<br> <font color = blue> The areas and geographic shapes are obtained from the GeoJSON data available on github by Logan Powell from the Census Bureau.</font>
      * population density<br> <font color = blue>Population density is the total population divided by land area.</font>
    1. COVID includes
       * The total cases, hospitalizations, and deaths from the beginning of the pandemic to the selected ***date***.
       * New daily cases, hospitalizations, and deaths at the selected ***date***.
       * Total and new daily cases, hospitalizations, and deaths per population.
       * Hospitalization ratio (Total hospitalizations/Total cases), death ratio (Total deaths/Total cases), and deaths per hospitalizations (total deaths/total hospitalizations)<br>
   <font color = blue>Note that the congressional districts numbers for COVID cases, hospitalizations, and deaths are estimated from the available counties data </font>
    1. Partisan Voting Index (PVI)<br>
    <font color = blue>The Partisan Voting Index measures the political leanings of a congressional district toward either of the two major US political parties. Data is obtained from the Cook Political Report.It is based on either the 2012-2016 or 2016-2020 elections.</font>
       * PVI_R measures the political leanings of a congressional district toward the Republican party. A negative number implies it leans more toward the Democratic party.
       * PVI_D measures the political leanings of a congressional district toward the Democratic part. It is negative PVI_R.
    1. Demographics, Age
    1. Demographics, Race
    1. Demographics, Income
1. Select the ***date*** if the COVID Data Type is selected. It defaults to the most recent date. The ***Demographics*** data types have only one possible value and are based on the 2019 surveys. The geographic shapes in GEO are based on the 116th congress (CD116).
1. Check the ***Log Scale*** if needed.
1. Click on ***Run*** to see the results
## **<font color = 'DarkBlue'> Cell #4 </font>**
1. Use the slider to select the date range for the ***Animated Map*** and/or ***Time Series Plot***. The latter can both be selected and the resulting visualizations will open on seperate browsers.
1. Select the ***Scope***: County or Congressional District
1. Select the ***Measure***: Cases, Hospitalizations, or Deaths
1. Check ***Per Population*** to see the selected ***Measure*** per population
1. Check ***Log Scale*** to see the log of the selected ***Measure*** or ***Measure*** per population
1. Select the ***Count*** (Total or Average) and ***Window Size***
   1. From March 17 2020
      * Running total or average since the start of the pandemic. The data will be shown within the selected date range only
   1. From *selected Start Date*
      * Running total or average since the selected start date. So, the count will start at the selected date such that the first data point will be equal to the number of new cases, hospitalizations, or deaths at the selected start date.
   1. 1 day
      * New Daily cases, hospitalizations, or deaths. It would be the same regardless of the choice of ***Count***.
   1. 7 days
      * Total in the last 7 days (***Count*** = Total) or 7-day rolling average (***Count*** = Average)
   1. 14 days
      * Total in the last 14 days (***Count*** = Total) or 14-day rolling average (***Count*** = Average)
   1. 21 days
      * Total in the last 21 days (***Count*** = Total) or 21-day rolling average (***Count*** = Average)
   1. 28 days
      * Total in the last 28 days (***Count*** = Total) or 28-day rolling average (***Count*** = Average)
1. Check ***Animated Map*** to see an animation of the selected ***Measure***/***Count*** in each county or congressional district (depending on the selected ***scope***), and select the animation frequency (this only applies to the animated map, and not the time series plot). This will determine the number of animation frames. The higher the number of frames, the longer it takes for the results to show.
1. Check ***Time Series Plot*** and select ***Plot Type*** to see the time series of the selected choices above. If ***Normalized*** is checked, then each county or congressional district will be normalized such that their corresponding max number (within the selected date range) will be equal to 1. If ***Compare to State-wide Values*** is checked, then additional plots will be shown to compare the time series to that of the state-wide time series.
## **<font color = 'DarkBlue'> Cell #5 </font>**
Total Cases, Hospitalizations, or Deaths for each month
## **<font color = 'DarkBlue'> Cell #6 </font>**
Shows the number of people vaccinated by vaccination status (At Least One Dose, Fully Vaccinated, First Booster, Second Booster) or number vaccines administered by status (Monovalent Booster, Bivalent Booster, Immunocompromised Dose). The first and most of the second boosters are monovalent boosters. So, the reported numbers for monovalent and bivalent boosters refer to the total number of boosters given. I.E., if one person had the first and second boosters and both boosters were monovalent then the count will be 2 not 1.
1. Check ***Animated Map*** for an animation of the selected ***Measure*** or ***Measure***/population (if ***Per Population*** is checked) with the selected ***Animation Frequency***. If ***Animation Frequency*** = Latest, then only the most current numbers will be shown on the map, with no animation
1. Check ***Time Series Plot*** for a time series plot of the selected choices.
## **<font color = 'DarkBlue'> Cell #7 </font>**
Estimate the number of waves and their corresponding start and end dates based on overall number of peaks.<br>
***show_plots*** is set to False by default. To see the plots showing the start, end, and peak of each wave, set show_plots to True
## **<font color = 'DarkBlue'> Cell #8 </font>**
1. Check ***Correlation Matrix***, ***Scatter Matrix***, and/or ***Partial Correlation Matrix*** for heatmaps and/or scatter plots of the corresponding matrices. <br> It is possible to check all options and each will open in a different browser.
1. Select ***Scope*** to specify if using County or Congressional District data to calculate the correlations.
1. The ***Covariates*** options only apply if ***Partial Correlation Matrix*** is selected
1. Each Variable/Covariate has a corresponding ***Measure*** to be selected from the dropdown menu
1. The ***Wave*** selection will only affect the ***COVID Outcome*** and ***Vaccination Status*** Variables. Options are: Overall, Wave 1, Wave 2, ...Wave n, where n is the total number of waves calculated above.
   1. ***COVID Outcome*** is the total number only within the selected ***Wave***
   1. ***Vaccination Satus*** options depend on the available vaccines at the beginning of the selected ***Wave***. Except if ***Wave*** = 'Overall', then the options include all vaccination statuses.
