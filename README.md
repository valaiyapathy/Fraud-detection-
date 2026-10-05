# 🚨 Fraud Detection App

A machine learning-based **Fraud Detection Web Application** built using **Python, Pandas, Scikit-learn, Joblib, and Streamlit**.

The application allows users to enter transaction details and predicts whether the transaction is **fraudulent or legitimate**.

link: https://yxj5ew74cfajpj5frkwkfd.streamlit.app/
---


## 📌 Project Overview

Financial transaction fraud is a major problem in digital banking and payment systems. This project uses machine learning to identify potentially fraudulent transactions based on transaction details and account balance information.

The trained machine learning model is saved as `model.pkl` and integrated into a Streamlit web application.

### Key Features

* Enter transaction details through a simple web interface
* Supports multiple transaction types
* Performs feature engineering automatically
* Predicts **Fraud / Not Fraud**
* Displays the model's fraud confidence
* Shows the entered transaction data
* Uses a pre-trained machine learning model

---

## 🛠️ Technologies Used

| Technology                      | Purpose                              |
| ------------------------------- | ------------------------------------ |
| Python                          | Programming language                 |
| Pandas                          | Data processing                      |
| Scikit-learn                    | Machine learning                     |
| Joblib                          | Saving and loading the trained model |
| Streamlit                       | Web application                      |
| Jupyter Notebook / Google Colab | Model development                    |

---

## 📂 Project Structure

```text
Fraud-Detection/
│
├── app.py
├── model.pkl
├── README.md
└── requirements.txt
```

### Files

**`app.py`**

Contains the Streamlit application and prediction logic.

**`model.pkl`**

Contains the trained machine learning model.

**`README.md`**

Project documentation.

**`requirements.txt`**

Contains the Python libraries required to run the project.

---

## 📊 Input Features

The application uses the following transaction features:

| Feature             | Description                                        |
| ------------------- | -------------------------------------------------- |
| `step`              | Time step of the transaction                       |
| `type`              | Type of transaction                                |
| `amount`            | Transaction amount                                 |
| `oldbalanceOrg`     | Sender's balance before transaction                |
| `newbalanceOrig`    | Sender's balance after transaction                 |
| `oldbalanceDest`    | Receiver's balance before transaction              |
| `newbalanceDest`    | Receiver's balance after transaction               |
| `orig_balance_diff` | Difference between sender's old and new balance    |
| `dest_balance_diff` | Difference between receiver's old and new balance  |
| `orig_empited`      | Indicates whether the sender's account was emptied |
| `errorBalanceOrig`  | Sender balance consistency error                   |
| `errorBalanceDest`  | Receiver balance consistency error                 |

---

## 🔧 Feature Engineering

Additional features are calculated automatically before making the prediction.

### Sender Balance Difference

```python
orig_balance_diff = old_balance_org - new_balance_org
```

### Receiver Balance Difference

```python
dest_balance_diff = new_balance_dest - old_balance_dest
```

### Account Emptied

```python
orig_empited = int(amount == old_balance_org)
```

### Sender Balance Error

```python
errorBalanceOrig = (
    new_balance_org + amount - old_balance_org
)
```

### Receiver Balance Error

```python
errorBalanceDest = (
    old_balance_dest + amount - new_balance_dest
)
```

These features help the model identify unusual or inconsistent transaction patterns.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Fraud-Detection.git
```

Move into the project directory:

```bash
cd Fraud-Detection
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, install the main libraries:

```bash
pip install streamlit pandas scikit-learn joblib
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

After running the command, Streamlit will provide a local URL similar to:

```text
http://localhost:8501
```

Open the URL in your browser.

---

## 🔮 How the Application Works

```text
User
  │
  ▼
Enter Transaction Details
  │
  ▼
Feature Engineering
  │
  ▼
Load Trained Model
  │
  ▼
Machine Learning Prediction
  │
  ├───────────────┐
  ▼               ▼
Fraud          Not Fraud
  │               │
  ▼               ▼
Warning         Safe
Message         Message
```

---

## 🧪 Example

### Example Transaction

```text
Transaction Type: TRANSFER
Amount: 10000
Sender Balance Before: 10000
Sender Balance After: 0
Receiver Balance Before: 0
Receiver Balance After: 10000
```

The application processes these values, creates the required features, and sends them to the trained machine learning model.

### Possible Output

```text
Prediction Result

🚨 This transaction looks like FRAUD!

Model confidence it is fraud: 92%
```

or

```text
Prediction Result

✅ This transaction looks SAFE (Not Fraud).

Model confidence it is fraud: 8%
```

---

## 📈 Model Prediction

The application uses:

```python
model.predict(input_data)
```

to determine the predicted class.

For fraud probability, it uses:

```python
model.predict_proba(input_data)
```

Class interpretation:

```text
0 → Not Fraud
1 → Fraud
```

---

## ⚠️ Important Notes

The feature names in the Streamlit application must exactly match the feature names used while training the model.

For example:

```text
errorBalanceOrig
errorBalanceDest
```

must not be changed to:

```text
error_balance_orig
error_balance_dest
```

unless the model is retrained with those names.

Also make sure that `model.pkl` is located in the same directory as `app.py`.

---

## 🔒 Disclaimer

This project is intended for **educational and demonstration purposes**.

The prediction should not be considered a definitive determination of financial fraud. A production fraud detection system would require additional security controls, monitoring, model validation, real-time transaction data, and appropriate financial compliance processes.

---

## 👨‍💻 Author

**Valaiyapathy N**

Computer Science Engineering Graduate

### Skills Demonstrated

* Python
* Machine Learning
* Data Analysis
* Pandas
* Scikit-learn
* Streamlit
* Feature Engineering
* Model Deployment

---

## ⭐ Future Improvements

* Add real-time transaction monitoring
* Improve model performance with additional algorithms
* Add confusion matrix and performance metrics
* Add ROC-AUC evaluation
* Add transaction history
* Add interactive fraud analytics dashboard
* Deploy the application online
* Add database integration
* Implement model retraining pipeline

---

## 📜 License

This project is intended for educational and portfolio purposes.
