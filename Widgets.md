1. Select the ***Scope*** of the map: County or Congressional District
1. Select the ***Data Type***. This will change the available options in the dropdown menu for ***data***
   1. GEO inludes
      * total population of each county/congressional district<br> <font color = blue>The population data is obtained from the United States Census Bureau, American Community Survey (ACS) 5-year data.</font>
      * land area
      * water area<br> <font color = blue> The areas and geographic shapes are obtained from the GeoJSON data available on github by Logan Powell from the Census Bureau.</font>
      * population density<br> <font color = blue>Population density is the total population divided by land area.</font>
    1. COVID includes
       * The total cases, hospitalizations, and deaths from the beginning of the pandemic to the selected ***date***.
       * New daily, weekly, biweekly, and monthly cases, hospitalizations, and deaths at the selected ***date***.
       * Total, daily, weekly, biweekly, and monthly cases, hospitalizations, and deaths per population.
       * Hospitalization ratio (Total hospitalizations/Total cases), death ratio (Total deaths/Total cases), and deaths per hospitalizations (total deaths/total hospitalizations)
    1. Partisan Voting Index (PVI)<br>
    <font color = blue>The Partisan Voting Index measures the political leanings of a congressional district toward either of the two major US political parties. Data is obtained from the Cook Political Report.It is based on the 2008-2012 elections which are available for free. The more recent data are only available for paying members. Note that PVI data only applie to the congressional district ***scope***.</font>
       * PVI_R measures the political leanings of a congressional district toward the Republican party. A negative number implies it leans more toward the Democratic party.
       * PVI_D measures the political leanings of a congressional district toward the Democratic part. It is negative PVI_R.
    1. Demographics, Age
    1. Demographics, Race
    1. Demographics, Income
1. Select the ***date*** if the COVID Data Type is selected. It defaults to the most recent date. The other data types have only one possible value. All the demographic data types are based on the 2019 surveys. The geographic shapes in GEO are based on the 116th congress (CD116).
1. Check the ***Log Scale** if needed.
1. Click on ***Run*** to see the results