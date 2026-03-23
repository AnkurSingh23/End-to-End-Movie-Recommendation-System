# <p align="center">🎬 MOVI<span style="color:#e50914">GENIUS</span></p>

<p align="center">
  <img src="https://img.shields.io/badge/Maintained-Yes-00c8ff?style=for-the-badge" alt="Maintained">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/UI_Design-Netflix_Style-e50914?style=for-the-badge&logo=netflix" alt="UI Style">
</p>

<p align="center">
  <strong>MoviGenius</strong> is a high-performance, full-stack Movie Recommendation Engine. It bridges the gap between <b>Mathematical NLP</b> and <b>Modern Web Design</b> to provide a seamless cinematic discovery experience.
</p>

---

## 📌 Project Overview
MoviGenius transforms raw TMDb metadata into intelligent recommendations. Unlike basic scripts, this is a **Complete End-to-End Pipeline** that processes thousands of data points (Cast, Director, Genres, Keywords) to predict user preferences using text vectorization.

> [!IMPORTANT]
> This system supports **Dual-Inference**: Toggle between high-speed **Cosine Similarity** or the spatial clustering logic of **K-Nearest Neighbors (KNN)**.

---

## 🚀 Key Features
* 🎭 **Dual Model Selection:** Choose between Cosine Similarity & KNN algorithms.
* 🔍 **Smart Search:** Interactive dropdown with autocomplete for 4800+ movies.
* 🌑 **Cinematic UI:** A dark-mode, Netflix-inspired interface with Glassmorphism effects.
* 🧪 **NLP-Powered:** Advanced feature engineering using `CountVectorizer`.
* ⚡ **Optimized Inference:** Millisecond response times using pre-computed similarity matrices.

---

## 🛠 Tech Stack

| Category | Technology |
| :--- | :--- |
| **Backend** | ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white) |
| **Machine Learning** | ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) |
| **Frontend** | ![Bootstrap 5](https://img.shields.io/badge/Bootstrap_5-7952B3?style=flat-square&logo=bootstrap&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) |
| **NLP** | ![CountVectorizer](https://img.shields.io/badge/NLP-CountVectorizer-blue?style=flat-square) |

---

## 🧠 Algorithms & Math

### 🔹 Cosine Similarity
Measures the cosine of the angle between two movie vectors. It focuses on the "direction" of the tags rather than the magnitude.
$$\text{similarity} = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$$

### 🔹 K-Nearest Neighbors (KNN)
Calculates the distance between movies in a 5000-dimensional space and identifies the 5 closest "neighbors."

---

## ⚙️ Setup Guide

---

## ⚙️ Setup Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/AnkurSingh23/End-to-End-Movie-Recommendation-System.git
cd End-to-End-Movie-Recommendation-System
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Generate ML Artifacts 🧪

> ⚠️ The model files (`.pkl`) are not included due to GitHub size limits.

#### 👉 Follow these steps:

1. Open the notebook:

```bash
Notebook/EDA_and_Model.ipynb
```

2. Run all cells

3. This will generate:

```
movies.pkl
similarity.pkl
knn.pkl
vectors.pkl
```

4. Create artifacts folder:

```bash
mkdir artifacts
```

5. Move files into:

```bash
artifacts/
```

---

### 4️⃣ Run the Application 🚀

```bash
python manage.py runserver
```

---

### 5️⃣ Open in Browser 🌐

👉 http://127.0.0.1:8000/

---

## 📂 Project Structure

```bash
├── artifacts/           # Generated ML models (.pkl)
├── movie_recommender/   # Django project configuration
├── recommender/         # Main app (views, utils, templates)
├── Notebook/            # Data processing & model building
├── manage.py
└── requirements.txt
```

---

## ⚠️ Model Files Notice

The `.pkl` files are excluded because:

* GitHub has a **100MB file size limit**
* These files are large (~150–180MB each)

👉 This is standard practice in ML projects
👉 Models can be regenerated using the notebook

---

## 🔮 Future Improvements

* 🎬 Movie Posters using TMDb API
* ⭐ Hybrid Recommendation System
* 🔍 Advanced Autocomplete Search
* ☁️ Deployment (Render / AWS)

---

<p align="center">
  <b>Developed by Ankur Singh 🚀</b>
</p>
