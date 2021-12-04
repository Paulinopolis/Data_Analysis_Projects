![This is an image](https://cm-messenger-blog-assets.s3.eu-west-1.amazonaws.com/53fda7d4-279c-4ebe-89ce-00216aad001b)


# Citymapper Mobility Index Analysis
This analysis aims analysis the impact of the lockdown measures in the Cities on the Citymapper Mobility Index. 

## Background Information

**Citymapper** is a public transit app and mapping service. It displays transport options, usually with live timing, between any two locations in a supported city. It also integrates data form all urban modes of transport. The app is supported by an Internet Website and a mobile App. 

During the COVID-19 situation, Citymapper created the **Citymapper mobility Index**. This index is calculated by comparing trips planned in the Citymapper app to a recent *typical usage period*.

A typical usage period is defined as the usage of the application from ***January 6th to February 2nd 2020***. 
Nevertheless, for some cities there were other specifics usage period defined: 
- Paris: February 3rd to March 1st
- Hong Kong and Singapore: Dec 2nd to 22nd. 

The index is calculated per day, meaning the time going from Midnight to Midnight UTC. 
For some cities (like Melbourne) the calendar day may not correspond. 

Mobilities taken into account for the index are: Public Transport, walking cycling, cabs and some micromobilities (ex. scooters).


## Data Limits
We draw your attention to the fact that there are some limits in thise data: 

- The Citymapper index takes only into account the trips planned using this application. This means that people traveled using other applications (like google maps) are not taken into account. 

- The index takes only into account the *formal public transport* and does not measure the mobility that could have been done via informal means. This is particulary important in countries with a limited public transport network. 

- As previously, the period of comparaison is not the same for all the cities. And there are some inconsistencies in the dates fue to the time difference between the cities (UTC is the referential). 


## Datesets used: 

### Citymapper Mobility Index
- Downloaded from KAGGLE (https://www.kaggle.com/andrewmvd/citymapper-mobility-index) 
- Total of 134 rows = 134 days (it goes from Janyary 20th to June 1st 2020). 
- 42 columns = 42 cities
    - 13 cities in America, mostly in the USA. 
    - 23 cities in Europe, mostly Western Europe.
    - 5 cities in Asia. 

### COVID-19 Lockdown dates by country 
- Downloaded from KAGGLE (https://www.kaggle.com/jcyzag/covid19-lockdown-dates-by-country)
- Data given in terms of Country and Regions. 
- 2 useful information for us: type of lockdown (full, partial or none) and the lockdown start date. 
- Manually cleaned in Excel. We needed to make coincide each city that we had in the Citymapper dataset with the correspondent Country/Region. 


## Going further
We consider that this analysis could be completed with the following points: 
- Comparaison Capital Cities vs. Secondary ones. 
- Add to the database some socioeconomic information: 
    - The mobile phone rate coverage of the population. 
    - The informal transport rate.
    - The level of income. 
    - The share of the population with a car. 
    - The percentage of the cities covered by the public transport. 
    - The predominant economic sector by city. 

**TRELLO Citymapper Mobility Index Analysis: ** https://trello.com/b/0IaWP3J8/data-viz-project
