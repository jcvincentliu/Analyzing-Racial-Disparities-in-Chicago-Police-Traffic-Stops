# Analyzing Police Traffic Stops in Chicago

## Project Information and Objectives

The repository contains a series of works done for BPI (Business and Professional People for Public Interest), a non-profit organization, in the Data Classic Clinc class, a practicum course organized and hosted by DSI (Data Science Institute) at the University of Chicago. As an ongoing collaborative with BPI, the poject has two objectives: analyzing racial disparaties in Chicago traffic stops and investigating potential associations between the use of traffic stop practice and the crime rates of an area. The two goals are achieved through conducting explorative analysis, benchmark analysis, and poisson logistic regressions. Wholistically, the project tries to see if Chicago Police Officers stopped drivers differently based on their race and if such differences were driven by extrinstic reasons, such as high crime activies or intrinstic reasons, such as officers' own biases. Some parts of the work replicated established literature, for example, [*Wood et al., 2018*](https://www.semanticscholar.org/paper/An-Analysis-of-the-Metropolitan-Nashville-Police-%E2%80%99-Chohlas-Wood-Goel/ea1e629021ab3e4f6b548b7d11f9ae12b07df83e).   

***NOTE***: The branch contains ONLY my part of the project. 


## Participants
**Mentor**: Amanda Kube

**Students**: Vincent Liu, Yu-Hsuan Chou, Justin Kim, Gabrielle Meyers, Emily Yeh

## Repository Structure 

* IDOT Explorative Data Analysis: Any files related to my explorative analysis of Chicago traffic Stops using IDOT (Illinois Department of Transportation) data
  * figs: Exported figures (created using Python *Altair* library)
  * `Chicago_Traffic_Stop_EDA.ipynb`: Explorative analysis jupter notebook file
* Chicago Crime Analysis
  * `crime_cleaning.ipynb`: Explorative analysis jupter notebook file
  * output_data_and_graphs: Outputted data and figuers (produced using *matplotlib* and *pandas* libraries) 
* Age-adjusted Probability Calculation by Race in Chicago:
  * `Probability_calculation.ipynb`: Jupyter notebook file in which I cleaned the Census and ACS data and plotted a splined scatter plot about the probaility of being in each age group, given the person's race
    *  `probability.py`: Python file to calculate the probability using IDOT data <br/>
     To see the output: First clone the repository, locate to this folder, type `Python3 probability.py` in the terminal, and press enter
* `cleaning_idot.py`: Helper functions from Emily to do some basic cleanings of the IDOT data 
* `README.md`: This file

## Appreciation

I want to give special appreciation to Ms. Amanda Kube for her support and helps on this project
