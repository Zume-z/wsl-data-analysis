<div align="center">

# Machine Learning Approaches to Forecasting Surf Competitions.

This project investigates the use of machine learning to predict the winners of surf competition heats. 
Three machine learning models, Artificial Neural Networks (ANNs), Random Forests, and XGBoost, are employed to analyse historical competition data, surfer statistics, and wave conditions. 
The project aims to determine the feasibility and effectiveness of machine learning in forecasting surf competition outcomes.
</div>

**Important:** The dataset used in this project is private, mock data has been provided for testing. The full dataset is avaliable upon request.

The project uses a dataset consisting of more than 19,000 Championship Tour heats conducted by the World Surfing League from 2012 to 2024. The dataset contains three primary sources of information:
* Historical Competition Data: This segment encompasses details such as outcomes of heats, locations of competitions, among other relevant metrics.
* Surfer Statistics: This category provides detailed information regarding the competitors. It includes metrics such as the surfers' rankings, stances, average heat totals, and historical performance at various competition venues.
* Wave Conditions: The dataset also includes quantifiable metrics related to the surfing environment, covering aspects like wave height, wind direction, and the type of waves encountered.

Before training the models, the data underwent a preprocessing stage involving feature scaling and encoding categorical features. For each model a training-validation split was employed and hyperparameter tuning was performed to optimise the performance on the validation set.

Each model (ANN, Random Forest, XGBoost) was trained on the training set and evaluated on the validation set using the following classification metrics:
* Accuracy: Measures the overall proportion of correctly predicted heat winners.
* Precision: Indicates the ratio of true positives (correctly predicted winners) to all positive predictions by the model.
* Recall: Represents the ratio of true positives (correctly predicted winners) to all actual winners in the validation set.
* F1-Score: A harmonic mean of precision and recall, providing a balanced view of model performance.

The ANN model achieved 0.70 overall accuracy, with an F1-score of 0.73 for class 0 (surfer losing the heat) and 0.66 for class 1 (surfer winning the heat). 
The Random Forest model also reached 0.70 accuracy, with F1-scores of 0.73 for class 0 and 0.67 for class 1. 
XGBoost performed slightly better, with 0.71 accuracy and F1-scores of 0.74 for class 0 and 0.68 for class 1.

<div align="center">
  <img width="750" alt="fig1" src="https://github.com/Zume-z/wsl-data-analysis/assets/36926781/368bb646-11d4-4883-a632-7a79ad0627ec"/>
  <img width="750" alt="fig2" src="https://github.com/Zume-z/wsl-data-analysis/assets/36926781/1d6e29a7-91be-4a42-b7f1-6700e63440e9"/>
  <img width="750" alt="fig4" src="https://github.com/Zume-z/wsl-data-analysis/assets/36926781/67317cdf-d2dd-4d40-9d88-d9a0d9eb6a43"/>
  <img width="750" alt="fig5" src="https://github.com/Zume-z/wsl-data-analysis/assets/36926781/a6cbe63b-e16b-499c-b6ba-cbb20e1cf5bb"/>
  <img width="750" alt="fig3" src="https://github.com/Zume-z/wsl-data-analysis/assets/36926781/c0171f39-940c-4fda-941e-605e57a51625"/>
</div>

