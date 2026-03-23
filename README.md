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

### 1️⃣ Clone Repo
```bash
git clone [https://github.com/AnkurSingh23/End-to-End-Movie-Recommendation-System.git](https://github.com/AnkurSingh23/End-to-End-Movie-Recommendation-System.git)
cd End-to-End-Movie-Recommendation-System
