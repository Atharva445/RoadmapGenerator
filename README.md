

# **AI-Powered Career Roadmap Generator**

## 📘 Overview

The **AI-Powered Roadmap Generator** is an intelligent career guidance system that recommends personalized learning paths for users based on their target role and known skills.
It uses AI and ML concepts like **correlation mapping**, **hybrid reasoning**, and **salary-based prioritization** to generate dynamic roadmaps.
Additionally, it integrates **YouTube** and **Google Search APIs** to fetch top tutorials and certification courses in real time.

---

## 🧠 Key Features

* 🎯 Role-based AI skill recommendation
* 💰 Salary-based prioritization (suggests highest-paying skills first)
* 📺 Real-time YouTube tutorial fetching
* 🎓 Dynamic certification course suggestions using Google Search API
* 🤖 Hybrid AI approach combining rule-based + data-driven intelligence
* 🧹 Removes redundant or outdated skills
* 🧭 Interactive UI built with Streamlit

---

## ⚙️ How to Run the Project

### **Step 1: Clone this repository on your local device**

```bash
git clone https://github.com/yourusername/ai-roadmap-generator.git
cd ai-roadmap-generator
```

---

### **Step 2: Load StackOverflow dataset in `main.ipynb` and run this file**

This will generate the required `.pkl` model files used by the app.

---

### **Step 3: Create `.env` file and paste this**

```
YOUTUBE_API_KEY=your_youtube_api_key
GOOGLE_API_KEY=your_google_api_key
CSE_ID=your_custom_search_engine_id
```

---

### **Step 4: Run Streamlit app**

```bash
streamlit run app.py
```

---

✅ That’s it! Your **AI-Powered Career Roadmap Generator** is now ready to use.

---

