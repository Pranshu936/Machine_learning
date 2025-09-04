
# Amazon Bestsellers Data Analysis

This project analyzes the **Amazon Bestsellers Items (2025)** dataset using Python and Jupyter Notebook.  
It involves data cleaning, exploratory data analysis (EDA), and visualization to uncover insights into product pricing, ratings, and popularity.

---

## 📌 Project Overview

The notebook performs the following steps:

1. **Load the Data**
   - Reads `Amazon_bestsellers_items_2025.csv` into a Pandas DataFrame.

2. **Explore the Data**
   - Displays summary statistics, data types, and missing values.

3. **Clean the Data**
   - Removes unnecessary columns.
   - Handles missing values in key features (`product_price`, `product_star_rating`, `product_num_ratings`).
   - Cleans currency symbols and converts price to numeric.
   - Removes outliers using the Interquartile Range (IQR) method.

4. **Visualize the Data**
   - Scatter plots (Price vs Rating, Price vs Number of Ratings).
   - Histograms (Price, Ratings, Number of Ratings).
   - Count plots for categorical features (e.g., country).

---

## 📊 Dataset

**File**: `Amazon_bestsellers_items_2025.csv`

Typical columns include:

- `product_name` – Name of the product  
- `brand` – Brand of the product  
- `category` – Category the product belongs to  
- `product_price` – Price of the product  
- `product_star_rating` – Average star rating  
- `product_num_ratings` – Number of ratings  
- `country` – Country of listing  

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/amazon-bestsellers-analysis.git
cd amazon-bestsellers-analysis
````

### 2. Install Dependencies

Make sure you have Python 3.8+ installed. Then install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Run the Notebook

```bash
jupyter notebook Amazon.ipynb
```

---

## 🛠️ Technologies Used

* **Python** (pandas, numpy, matplotlib, seaborn)
* **Jupyter Notebook**

---

## 📈 Results & Insights

* Most products fall within a certain price range after removing outliers.
* Higher star ratings are not always correlated with higher prices.
* Some products have a disproportionately high number of ratings, showing bestseller bias.
* Categorical distributions (e.g., by country) reveal geographic product trends.


