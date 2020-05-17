# README - Programming Project

## Content

1. [Introduction](#introduction)
   1.  [Problem](#problem)
   2.  [Objective](#objective)
   3.  [Methodology](#methodology)
2. [Installation](#installation)
   1.  [Get the Git repository](#get-the-git-repository)
   2.  [Setting the environment](#setting-the-environment)
3. [Pre-processing](#pre-processing)
   1.  [Kaggle API](#kaggle-api)
   2.  [Pre-processing algorithm](#pre-processing-algorithm)
4. [Structure](#structure)
   1.  [Main page](#main-page)
   2.  [Dashboard](#dashboard)
   3.  [Analysis per sector](#analysis-per-sector)
   4.  [VMB Model](#vmb-model)
5. [Maintenance and update](#maintenance-and-update)

## Introduction

### Problem

Like many other developing countries, our country, Bolivia, has a
flourishing startup industry with attractive growth potential and
adequate prospectives not only to fulfill the investors' financial
return requirements but the social and environmental returns as well.
Therefore, from a Triple Bottom Line perspective, a potential
investment in one of these markets could be a crucial step further
on sustainable  portfolio construction.

However, one of the main shortcomings of these developing markets
is the lack of adequate tools and networks to raise the required
resources and connect the investors with prospective investees.

### Objective

The project aims to provide investors with a comprehensive platform
for the startup ecosystem. Furthermore, be one step ahead by showing
the essential features when analyzing a potential investment in this
kind of company. This way, we expect to address the market's
shortcomings and help its development.

On the other hand, we are facing times of uncertainty that force
the different market agents to provide out-of-the-box solutions.
So, the adaptability and replicability of these solutions is a
paramount feature to generate a real change in the matter.

### Methodology

As master students at UNIL MSc. in Finance program, we have faced
this issue on a two-part project consisting of a Prediction model
and Investors' Platform.

#### Prediction Model

The first part is carried out under the scope of the Advanced Data
Analytics class. This project first aims to understand the features
that have the most significant influence on the success of startups.
Then, using these features construct a classification model that can
predict the potential outcome of a startup given its set of features.
This way, we can provide the market with a more in-depth insight into
the early stage of a startup. Therefore, investors can focus their
resources more intelligently, and the entrepreneurs can redirect
their efforts to reinforce these features.

#### Investors' Platform

The second part of the project is carried out under the scope of the
Programming class. This project aims to develop a Graphic User
Interface (GUI) (from now on referred as platform) that
displays the industry's most relevant facts and allows the investor
to search for specific information by sub-industry to make a more
informed investment decision. Furthermore, we included in the
platform the prediction model, developed in the first part of the
project, to enable investors and entrepreneurs to interact with the
model and improve their prospectives.

## Installation

### Get the Git repository

Our project is host in the following
[repository](https://github.com/CristhianBruno/pro_project/blob/master/README.md)
The steps required to clone the repository are the following:

1. On GitHub, navigate to the main page of the repository.
2. Under the repository name, click Clone or download.
3. Copy the repository's URL.
4. According to your operative system:
   * For Windows: Open Git Bash.
   * For Mac/Linux: Open Terminal.
5. Change the current working directory to the location where you
want the cloned directory.
6. Type `git clone`, and then paste the URL you copied earlier.
   `$ git clone 'HERE-COMES-THE-URL'`
7. Press **Enter** to create your local clone.

### Setting the environment

The program requires the installation of the environment
pro_project_env, set on the following file pro_project_env.yml.
The environment's file is already included in the Github repository.

####  Conda and PIP environment installation
To create and activate the environment using the `pro_project_env.yml`
file follow this steps:

Conda:
1. Create the environment: `conda env create —-file pro_project_env.yml`
2. Activate the environment: `conda activate pro_project_env`

PIP:
1. Create virtual environment: `virtualenv pro_project_env`
2. Activate the virtual environment: `pro_project\Scripts\activate`

However, it can be executed on any environment that has installed the
following packages:
  - Tkinter - version 8.6.8 (already included in Python)
  - Numpy - version 1.18.1
  - Pandas - version 1.0.3
  - Matplotlib - version 3.1.3
  - Scikit-Learn - version 0.23.0
  - Pillow - version 7.1.2
  - Pandastable - version 0.12.2

The program runs in Python - version 3.8.2.

## Pre-processing

The program is based on the CAX_startup data base uploaded by Ajay
Gorkar to Kaggle. To obtain this data we used the website's
API and worked it through our pre-processing process. In the next
section we will explain how to get the API and run the pre-processing
algorithm.

### Kaggle API
To use the Kaggle API please follow these steps:
1. Sign up or sign in for a Kaggle account at
[https://www.kaggle.com](https://www.kaggle.com/)
2. Go to the 'Account' tab of your user profile
`https://www.kaggle.com/<username>/account`
and select 'Create API Token'. This will trigger the download of
`kaggle.json`, a file containing your API credentials.
3. Place the downloaded file in the location `~/.kaggle/kaggle.json`.
4. Install the Kaggle package with `pip install kaggle` to run the
pre-processing algorithm.

This process will let you to obtain the database directly from Kaggle,
which is the main input for this project.

### Pre-processing algorithm

Pre-processing the database is an essential step for the structuration
of both the model and platform. Throughout this process, we have first
analyzed the data and then proceed to uniformized each feature to
clean misspelled words or out-of-range values, always considering
the variable's nature.

All this work was implemented through a pre-processing algorithm
written in the Jupyter Notebook named `Preprocessing_PROG.ipynb`.
To run this script, please verify the adequate installation of the
Kaggle API. Also, the algorithm requires the installation of the
Pandas library (already included in the environment
`pro_project_env.yml`).

The process first downloads the database using the API in a CSV file.
The database was uploaded by Ajay Gorkar in November 2019, and it
is currently available on Kaggle under a dataset called 'Startup
Analysis' which contains the file named 'CAX_Startup_Data.csv'.
You can review the repository
[here](https://www.kaggle.com/ajaygorkar/startup-analysis).

The raw database consists of 472 entries, each representing a
different startup with 116 features for each one.
After downloading the database, the program will uniformize the
empty entries and then delete all non-useful features. The next
step is to correct typo mistakes, capital missuses, space problems,
redefine industry categories, and rename all the headers for a
uniform presentation, to provide finally with a clean output
called `CAX_Preprocessed_PROG.csv`.
This processed database comprises 472 startups with 102 features,
which is the primary input for the platform construction.

## Implementation
Finally, to start the program, you need to run the main python file
called: `PRO_Final_Project_VMB.py` placed on the root directory of
the repository. This script runs the primary structure of the platform
that will be explained below. To run this script appropriately, we
rely on the following internal dependencies, hosted in the folder
`VMB_Generators/` present also on the repository. The dependencies
and their functions are:
1. `Button_Generator.py`:  designed to generate all the buttons that
connect every frame of the platform.
2. `Graph_Generator.py`: designed to create all the graphs.
3. `Industry_Selection.py`: designed to ease the selection of
sub-industry and economic activity for the VMB Model.
4. `KeyFacts_Sector_Generator.py`: designed to display the key
facts of each sector on the platform.
5. `Model_Generator.py`:  designed run the prediction algorithm
of the VMB Model.
6. `Pivot_Table_Generator.py`: designed to generate all the tables.

Each dependency host the required functions to structure the platform
and the widgets needed for the GUI. It is paramount to maintain the
folder structure as it was intended to keep the platform running.
Please keep this issue in mind.

## Structure
The user interface has the following structure:

1. Main page: Platforms main window.
2. Dashboard: Relevant information of the data base displayed
as graphs and tables.
3. Analysis per sector: Relevant information of the industries
in the data base.
4. VMB Model: Prediction model of the success of a startup
based on the algorithm we generated through the Advanced Data
Analytics project.

### Main page


### Dashboard
- Statistics
    - Table
- Graphs
    - Page 1
    - Page 2

### Analysis per sector
- Page 1
- Page 2
  - Sector Selector
!! Importance of SUBMIT!!

- Frame by sector
  - Profile
  - Statistics

### VMB Model
- Intro
  - VMB ADA Model
  - Feature explanations
- Model features:
  - Industry
  - Experience of the team
  - Market characteristics
  - Business model
  !! Importance of SUBMIT!!
- VMB Model Results
    - Inputs
    - Results

## Maintenance and update
### Github
- Repository
- Collaboration
