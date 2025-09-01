📌 Fraud Detection using Machine Learning
📖 Introduction

Financial frauds cause significant monetary losses every year. Detecting fraudulent transactions is challenging because the data is highly imbalanced – fraudulent cases are very rare compared to genuine ones.

In this project, I built machine learning models to classify transactions as fraudulent or genuine. The goal was to achieve high recall for fraud cases without compromising too much on overall accuracy.

📊 Dataset

Dataset used: Credit Card Fraud Detection Dataset (Kaggle)

Total transactions: 284,807

Fraudulent transactions: 492 (~0.17%)

Genuine transactions: 284,315 (~99.83%)

Highly imbalanced dataset

⚙️ Technologies & Libraries

Python 🐍

NumPy

Pandas

Matplotlib & Seaborn

Scikit-learn

XGBoost

📂 Project Structure
fraud-detection-project/
│-- fraud_detection.ipynb       # Jupyter notebook with implementation
│-- Fraud_Detection_Report.pdf   # Final project report
│-- requirements.txt             # Dependencies
│-- README.md                    # Project documentation

✅ Results

ROC-AUC Score: 0.83

Accuracy: 99%

Precision (Fraud class): 0.96

Recall (Fraud class): 0.22

F1-score (Fraud class): 0.36

📌 Confusion Matrix

[[347871    24]
 [  2277   659]]

 ⚡ Model performs well overall, but recall for fraud cases needs improvement.

🔮 Future Improvements

Handle class imbalance using SMOTE / ADASYN

Try ensemble methods and deep learning models

Deploy model using Flask/Streamlit for real-time fraud detection

Improve fraud recall while keeping false positives low

👩 Author

Mona Prajapati
📌 Unified Mentor Fellowship Projoject