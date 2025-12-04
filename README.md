# 🎬 **Movie Recommendation System (Flask + ML)**

A simple, dynamic, modern movie recommendation system built using **Flask**, **Python**, **Machine Learning**, and an attractive **front-end UI** with animated movie cards and gradient placeholders.

This system recommends similar movies based on content similarity using TF-IDF vectors and cosine similarity.

---

# 🚀 **Features**

### ✔ **ML-Based Movie Recommendations**

* Uses TF-IDF + Cosine Similarity
* Preprocessed into pickle files
* Fast, accurate recommendations

### ✔ **Modern Dynamic Frontend**

* Animated gradient backgrounds
* Dynamic color patterns based on movie titles
* Smooth hover animations
* Minimalistic and aesthetic UI
* Responsive design (mobile/tablet/desktop)

### ✔ **Live Search + Autocomplete**

* Search movies instantly
* Smart filtering
* Instant recommendation results

### ✔ **Poster-Free Dynamic Visuals**

Because we are using **free APIs**, movie cards show:

* Dynamic gradients
* Movie title overlays
* Smooth animated highlights

No API key required — works fully offline.

---

# 📂 **Project Structure**

```
Movie-Recommendation-System/
│── app.py
│── movie recommendation system.py
│── generate_pickle_files.py
│── requirements.txt
│── list_of_movies.pkl
│── similarities.pkl
│── templates/
│     └── index.html
│── static/
      ├── style.css
      └── script.js
```

---

# 🛠️ **Installation & Setup**

### **1️⃣ Clone or Download the Project**

```
git clone https://github.com/your-repo/movie-recommendation-system.git
cd movie-recommendation-system
```

### **2️⃣ Install Dependencies**

```
pip install -r requirements.txt
```

### **3️⃣ Generate ML Model Files (Only first time)**

```
python generate_pickle_files.py
```

This will create:

* `list_of_movies.pkl`
* `similarities.pkl`

### **4️⃣ Run the Flask App**

```
python app.py
```

### **5️⃣ Open in Browser:**

[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

# 🎨 **UI Overview**

### 🔹 Dynamic Movie Cards

Each recommended movie displays:

* Gradient background
* Smooth hover animation
* Responsive scaling

### 🔹 Live Search Bar

* Type any movie
* Autocomplete dropdown
* Click to get instant recommendations

### 🔹 Fully Responsive

* Works on mobile, tablet, and desktop
* Auto-adjusts card layout

---

# 💡 **How Recommendations Work**

1. Dataset is loaded from movies.csv
2. Text fields (overview, genres, keywords) are combined
3. TF-IDF Vectorization converts text → numbers
4. Cosine similarity finds closest movies
5. Results returned to frontend

Fast, lightweight, accurate.

---

# 🔧 Troubleshooting

### ❌ Flask not found

```
pip install flask
```

### ❌ Numpy / Pandas Compatibility Error

```
pip install --upgrade numpy pandas
```

### ❌ Pickle loading error

Run:

```
python generate_pickle_files.py
```

### ❌ Server not starting

Make sure you're in the project folder:

```
cd Movie-Recommendation-System
python app.py
```

---

# 📌 Notes

* No paid APIs required
* No TMDB API key needed
* Works fully offline
* Posters replaced with dynamic gradient movie cards

If you want real posters later, API integration is optional.

---

# 📷 Screenshots (Add yours)

> ❗ Replace these with actual screenshots later.

```
/screenshots/homepage.png
/screenshots/recommendations.png
/screenshots/mobile-view.png
```

---

# 🤝 Contributing

Pull requests welcome!
Improve the UI, add movie posters, enhance ML, or optimize search performance.

---

# 🧑‍💻 Author

**Bhanu Prakash**
Movie Recommendation System – Flask + ML + Modern UI

---

# ⭐ If you upload this project to GitHub

Include this README.md — it makes your project look professional.

---

