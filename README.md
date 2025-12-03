# Diabetes Predictor

- Author: Shi Fan Jin, Amanpreet Binepal, Ian Gault, Vy Phan

This is a data analysis project for DSCI 522 (Data Science workflows); a course in the Master of Data Science program at the University of British Columbia.

## About

Here we attempt to build classification models using logistic regression and support vector machine (SVM) algorithms to predict whether an individual has diabetes based on health indicators and lifestyle factors. Specifically, we aim to evaluate the predictive performance of these models and compare their accuracy and efficiency for potential use in public health screening.

We use the diabetes_binary_health_indicators_BRFSS2015.csv dataset containing 253,680 survey responses from the CDC's BRFSS 2015. The target variable Diabetes_binary is binary with two classes: 0 for no diabetes and 1 for prediabetes or diabetes. The dataset includes 21 health and lifestyle features such as high blood pressure, high cholesterol, BMI, smoking status, physical activity, fruit and vegetable consumption, healthcare access, age, education, and income. Each row represents an individual survey respondent, with diabetes status determined through self-reported physician diagnosis.

The data set used in this project is from the Behavioral Risk Factor Surveillance System (BRFSS) 2015, an annual health-related telephone survey conducted by the Centers for Disease Control and Prevention (CDC). The original dataset was cleaned and prepared by Alex Teboul and is available on Kaggle https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset/data

Date was sourced from: https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators

## Report

The final report can be found in src folder.

## Usage

### Method 1 - Running Analysis with Docker (Preferred)

1. Clone this GitHub repository

``` bash
https://github.com/amanbinepal/diabetes-classification.git
```

2. Navigate to the project root in the terminal and run the following command:

``` bash
docker compose up -d
```

3. Open the JupyterLab URL displayed in the terminal (starts with http://127.0.0.1:8888/lab...)

4. To run the analysis, navigate to src/ and open diabetest_analysis.ipynb in the JupyterLab launched from previous step. In the Kernel tab, click Restart Kernel and Run All Cells....

5. To stop the container, press Ctrl + C in the terminal and run:

``` bash
docker compose stop
```
#### For Returning User:

To get the latest image after updates:
``` bash
docker compose pull
docker compose up
```

### Method 2 - Running Analysis using Environment File

1. Clone this GitHub repository & navigate to the project root directory

``` bash
https://github.com/amanbinepal/diabetes-classification.git
```

2. Create the conda environment

``` bash
conda env create --file environment.yml
```
Alternatively, use conda-lock for a faster installation (must have conda-lock installed):
``` bash
conda-lock install --name 522-project conda-lock.yml
```

3. Activate the environment by using the environment name defined in YAML file

``` bash
conda activate 522-project
```

4. Launch JupyterLab from the root of this repository:

``` bash
jupyter lab
```

5. Open src/diabetes_analysis.ipynb in Jupyter Lab

6. Under Switch Kernel, make sure that Python [conda env:522-project] is selected.

7. Under the Kernel menu click Restart Kernel and Run All Cells... to execute analysis and generate the final report.
## Dependencies

conda 

conda-lock

jupyterlab

nb_conda_kernels

Python and all packages listed in environment.yml

## License

The original diabetes health indicators dataset used in this project is licensed under the Creative Commons CC0 1.0 Universal (CC0 1.0) Public Domain Dedication by Alex Teboul. This means the data is free to use for any purpose without restriction.

The Diabetes Health Predictor report and analysis contained herein are licensed under the Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License. See the LICENSE.md file for more information. If re-using or re-mixing please provide attribution and link to this repository.

The software code contained within this repository is licensed under the MIT License. See the LICENSE.md file for more information.

## References

CDC Diabetes Health Indicators [Dataset]. (2017). UCI Machine Learning Repository. Retrieved from https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators

Centers for Disease Control and Prevention (CDC). 2015. "Behavioral Risk Factor Surveillance System Survey Data." Atlanta, Georgia: U.S. Department of Health and Human Services, Centers for Disease Control and Prevention. https://www.cdc.gov/brfss/annual_data/annual_2015.html

Teboul, Alex. 2020. "Diabetes Health Indicators Dataset." Kaggle. https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset

Xie, Zidian, Oanh Kieu Nguyen, Ethan A. Halm, and Ruili Wang. 2019. "Building Risk Prediction Models for Type 2 Diabetes Using Machine Learning Techniques." Preventing Chronic Disease 16:E130. https://doi.org/10.5888/pcd16.190109

Note: This project structure and workflow are adapted from the Breast Cancer Predictor project by Tiffany Timbers, Melissa Lee, and Joel Ostblom. This is a demonstration project for educational purposes. The models developed should not be used for clinical decision-making without further validation and regulatory approval.