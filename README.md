Machine Learning Model Selection and Pipeline


This project implements a machine learning pipeline that evaluates multiple models to select the best one based on accuracy and R² score. The project uses GridSearchCV for hyperparameter tuning to optimize model performance. The entire process is structured in Python using classes and methods to ensure scalability and flexibility.

Features
Implementation of multiple machine learning models.
Model evaluation based on R² score (for regression tasks).
Hyperparameter tuning using GridSearchCV.
Automatic model selection based on the highest R² score.
Modular design using Python classes and methods for easy pipeline execution and extension.


The project is built using the following components:

Data Ingestion: Reads and preprocesses the dataset.

Data Transformation: Applies transformations like scaling and encoding.

Model Training: Trains multiple machine learning models and uses GridSearchCV for hyperparameter tuning.

Model Evaluation: Selects the best model based on R² score and accuracy.

Pipeline Execution: The pipeline handles the end-to-end process from data ingestion to model evaluation.


Models Implemented
The project includes the following machine learning models:

Linear Regression
Random Forest Regressor
XGB Regressor
Support Vector Regressor (SVR)
Decision Tree Regressor
Each model is evaluated using GridSearchCV for hyperparameter tuning to find the best parameters.


Setup
Prerequisites
Python 3.x
Virtual environment (optional but recommended)
