# 🧠 Logistic Regression Explained

## 📖 Definition

**Logistic Regression** is a **supervised machine learning algorithm** used for **binary classification** problems. Despite the name "regression", it is used to classify input data into two discrete classes — typically labeled as 0 or 1.

---

## 📊 Key Differences from Linear Regression

| Feature               | Linear Regression                      | Logistic Regression                     |
|-----------------------|----------------------------------------|------------------------------------------|
| Output                | Continuous (e.g., any real number)     | Discrete (0 or 1)                        |
| Equation              | \( y = wx + b \)                       | \( p = \sigma(wx + b) \)                |
| Use Case              | Predict numeric values                 | Predict binary class labels             |
| Activation Function   | None                                   | Sigmoid                                  |
| Loss Function         | Mean Squared Error (MSE)               | Binary Crossentropy                      |

---

## 🧠 How Logistic Regression Works

### Step 1: Linear Combination

Just like linear regression, logistic regression starts with a weighted sum of inputs:
\[
z = w \cdot x + b
\]

### Step 2: Apply the Sigmoid Activation

To turn the linear output into a probability between 0 and 1, the **sigmoid function** is applied:
\[
\sigma(z) = \frac{1}{1 + e^{-z}}
\]

This function "squashes" the result so that:
- Values close to 0 mean low probability
- Values close to 1 mean high probability

### Step 3: Make Predictions

Predictions are made by setting a threshold (usually 0.5):
- If \( \sigma(z) \geq 0.5 \), predict **1**
- If \( \sigma(z) < 0.5 \), predict **0**

---

## 📉 Loss Function: Binary Crossentropy

To measure how well the model is performing, logistic regression uses **binary crossentropy**:
\[
\text{Loss} = - \left( y \cdot \log(p) + (1 - y) \cdot \log(1 - p) \right)
\]

This loss function penalizes incorrect predictions more harshly when the model is confident but wrong.

---

## 🏁 Training the Model

1. Initialize weights and bias randomly.
2. Compute the output \( p = \sigma(wx + b) \).
3. Calculate the binary crossentropy loss.
4. Use **gradient descent** to update the weights and bias to minimize the loss.
5. Repeat for several **epochs** until convergence.

---

## 🧪 Simple Example

| Input (x) | Label (y) |
|-----------|-----------|
| 1.0       | 0         |
| 2.0       | 0         |
| 3.0       | 0         |
| 6.0       | 1         |
| 7.0       | 1         |

The model will learn to classify low values of `x` as **0** and high values as **1**.

---

## ✅ When to Use Logistic Regression

- When your output is **binary** (yes/no, true/false).
- When you need a **probabilistic interpretation**.
- When the data is linearly separable or close to it.

---

## 📌 Summary

- Logistic Regression is a powerful yet simple classification algorithm.
- It turns linear regression into classification using the **sigmoid function**.
- It is optimized using **binary crossentropy loss** and **gradient descent**.

---

