## Student Performance Prediction
This project aims to develop an accurate student performance prediction system using a Kaggle dataset. The system can help educators identify at-risk students early on and provide them with appropriate interventions to improve their academic outcomes.
## Dataset
The dataset contains information about 1,000 students. The data features include student demographics, social and school-related factors, and academic performance in math and other courses. 

## Requirements
The project is implemented in Python and requires the following libraries:

- Scikit-learn
- NumPy
-pandas
- Matplotlib
- Flask

 
 ## Methodology


**The project follows these steps:**

- Data cleaning: Remove missing values, outliers, and irrelevant features from the dataset.
- Data preprocessing: Encode categorical variables, normalize numerical variables, and split the data into training and testing sets.
- Feature engineering: Create new features from existing ones, such as average grades, total absences, and study time ratio.
- Model development: Train and evaluate different machine learning models, such as Random Forest, Linear Regression, Decision Tree, and Gradient Boosting, using cross-validation and grid search techniques.
- Model selection: Compare the performance of the models on the test set and select the best one based on the mean absolute error (MAE) metric.
- System deployment: Build a Flask web application that allows users to input student data and get predictions of their math scores.
- The project is also designed using modular programming, which means that the code is divided into smaller, reusable, and independent modules. This makes the code easier to read, maintain, and debug, as well as facilitates collaboration and testing.

## Results
The best model for predicting student math scores is the Gradient Boosting model, which achieves an an accuracy of 83% on the test set. This is 15% better than the baseline model, which is a simple mean predictor. The system also provides a user-friendly interface for real-time predictions and insights.

## Future Work
Some possible directions for future work are:

- Extend the system to predict student performance in other subjects
- Explore more advanced machine learning techniques, such as neural networks, to improve the accuracy and robustness of the system.
