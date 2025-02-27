# Analysis-and-Prediction-of-Anxiety-Levels-Using-Machine-Learning-Techniques

This project aims to analyze and predict anxiety levels in individuals using a dataset containing information on psychological traits, demographic factors, and anxiety scores. The main objective is to classify anxiety levels based on responses to a Generalized Anxiety Disorder (GAD) questionnaire and to explore the relationships between demographic factors and anxiety levels.

## Table of Contents

- [Project Overview](#project-overview)
- [Dependencies](#dependencies)
- [Running the Project](#running-the-project)
- [Flask Backend](#flask-backend)
- [User Interface](#user-interface)
- [Model Deployment](#model-deployment)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project involves the following steps:

1. **Importing Dependencies**: Loading necessary libraries for data analysis, visualization, and machine learning.
2. **Data Collection**: Loading the dataset from a CSV file and displaying the first and last rows for an overview.
3. **Data Analysis**: Describing the columns of the dataset and identifying relevant columns for anxiety analysis.
4. **Data Preprocessing**: Removing irrelevant columns, classifying anxiety levels based on GAD scores, handling missing values, and simplifying categories.
5. **Data Visualization**: Creating graphs to visualize the distribution of ages and categorical columns.
6. **Label Encoding**: Transforming categorical columns into numeric values using `LabelEncoder`.
7. **Data Splitting**: Separating the data into features (X) and target (y).
8. **Model Selection**: Evaluating several machine learning models (Random Forest, SVM, Gradient Boosting, etc.) using cross-validation to determine their accuracy.
9. **Hyperparameter Tuning**: Using `GridSearchCV` to optimize the hyperparameters of the best models.
10. **Model Training**: Splitting the data into training and testing sets, then training the SVM model with the best hyperparameters.
11. **Model Evaluation**: Evaluating the model's performance on the training and testing sets using the confusion matrix and classification report.
12. **Predictive System**: Developing a function to predict anxiety levels from new input data.
13. **ModelPipeline Class for Future Deployment**: Creating a class to encapsulate the model and preprocessing steps, facilitating the deployment and use of the model in production environments.


## Dependencies

To run this project, you need the following dependencies:

- Python 3.x
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- Flask

You can install these dependencies using pip:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn flask
```

## Running the Project

To run the project, navigate to the project directory and execute the following command:

```bash
python app.py
```

This will start the Flask server, and you can access the application at `http://127.0.0.1:5000`.

## Flask Backend

The Flask backend handles user input and predictions. The `app.py` file contains the necessary routes and logic to collect user data, preprocess it, and predict anxiety levels using the trained model.

## User Interface

The user interface is built using HTML and Bootstrap. It collects user input through a series of questionnaires and displays the predicted anxiety level along with personalized recommendations.

## Model Deployment

The model and preprocessing steps are encapsulated in a `ModelPipeline` class, which is saved using `joblib`. This allows for easy deployment and reuse of the model in production environments.

## Contributing

Contributions to this project are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.
