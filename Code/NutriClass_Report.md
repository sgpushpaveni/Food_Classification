# NutriClass: Food Classification Using Nutritional Data

## Approach
- Loaded and inspected the food nutritional dataset.
- Visualized data distribution and class imbalance.
- Preprocessed data: handled missing values, capped outliers, removed duplicates, standardized features.
- Engineered features using PCA and SelectKBest.
- Encoded target labels for classification.

## Data Analysis
- Dataset contained `N` entries across several meal types and preparation methods.
- Observed some imbalance in class distributions (e.g., 'snack' is most frequent).
- Outliers detected in nutritional values; capped using IQR.


## Model Selection & Evaluation
- Compared multiple classifiers: Logistic Regression, Decision Tree, Random Forest, KNN, SVM, XGBoost, Gradient Boosting.
- Used accuracy, precision, recall, F1-score, and confusion matrix for evaluation.
- Tree-based models (Random Forest, Gradient Boosting, XGBoost) performed best overall.

## Insights & Recommendations
- Feature selection and PCA reduced dimensionality and improved model generalization.
- Random Forest and XGBoost showed highest F1-scores and robust confusion matrices.
- Recommend further hyperparameter tuning and cross-validation for production use.
- Visualizations provided clear trends in class distribution, model performance, and feature importance.

## Visualizations
- Class distribution bar plots.
- Sample entry previews.
- Model performance comparison (bar charts).
- Confusion matrices for each model.
- Feature importance for tree-based models.

---
