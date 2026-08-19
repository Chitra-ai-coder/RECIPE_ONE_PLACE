<div align="center">

# ✦ Rasa | The Royal Indian Culinary Archive ✦

**A high-performance, elegant web application preserving the rich heritage of Indian cuisine.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Framework-red.svg)](https://flask.palletsprojects.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458.svg)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

## 📖 About The Project

**Rasa** (hosted in the `RECIPE_ONE_PLACE` repository) is a beautifully crafted digital archive designed to showcase over 6,000 traditional Indian recipes. Built with a robust **Python/Flask backend** and a **Pandas-powered search engine**, it delivers lightning-fast data processing. 

The frontend is meticulously designed as a "Royal Menu," featuring high-end editorial typography, a smooth curtain-reveal landing page, and a strictly enforced 5-column responsive grid. It solves common UX pitfalls by decoupling search queries from category filters, ensuring a frictionless browsing experience.

## ✨ Key Features

* **Royal Menu Interface:** A CSS-driven landing page with an embossed text effect, golden ornaments, and a smooth "curtain reveal" animation that transitions into the main dashboard.
* **High-Density Heritage Grid:** A custom responsive UI displaying exactly 5 recipe cards per row on desktop, gracefully scaling down for tablets and mobile devices.
* **Global Smart Search:** A robust backend search engine that scans the entire database instantly. It operates independently of category filters to prevent "filter traps."
* **Frictionless Navigation:** Features boxless typography-based pagination and utilizes JavaScript `sessionStorage` to remember the user's state, preventing jarring page reloads when returning to the menu.
* **Editorial Recipe Pages:** Individual recipe pages are styled like a high-end culinary magazine, complete with floating meta-data pills, authentic Indian typographic ornaments, and an elegant layout.

## 🛠️ Tech Stack

* **Backend Environment:** Python 3
* **Web Framework:** Flask
* **Data Processing:** Pandas, Regex (`re`), Difflib
* **Frontend Design:** HTML5, Custom CSS3 (Flexbox, CSS Grid, Custom Variables)
* **Frontend Logic:** Vanilla JavaScript (DOM manipulation, Session Storage)

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### 1. Prerequisites

Ensure you have Python installed on your local machine. You will need to install the required dependencies:

```bash
pip install flask pandas
```

### 2. Installation

Clone the repository to your local machine:

```bash
git clone [https://github.com/Chitra-ai-coder/RECIPE_ONE_PLACE.git](https://github.com/Chitra-ai-coder/RECIPE_ONE_PLACE.git)
cd RECIPE_ONE_PLACE
```

### 3. Add the Dataset

For the application to run, you must place the dataset in the root directory. 
* Ensure your dataset is named exactly: `Cleaned_Indian_Food_Dataset.csv`
* Place it in the exact same folder as `app.py`.

### 4. Run the Application

Start the Flask local development server:

```bash
python app.py
```

Open your preferred web browser and navigate to:

```text
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
```

---

## 📁 Project Structure

```text
RECIPE_ONE_PLACE/
│
├── app.py                                  # Core Flask application & search engine logic
├── Cleaned_Indian_Food_Dataset.csv         # The 6,000+ recipe database (User provided)
│
└── templates/
    ├── index.html                          # Royal Menu landing page and main dashboard grid
    └── recipe.html                         # Detailed editorial recipe view
```

---

## 🧠 Core Logic & Architecture

* **Self-Healing Data Mapper:** The Pandas backend uses a dynamic column detector in `load_and_clean_data()`. It automatically identifies target columns even if the CSV headers are slightly modified (e.g., detecting `TranslatedRecipeName` vs `RecipeName`).
* **Session Memory:** To prevent the landing page animation from firing every time a user navigates back from a recipe, `sessionStorage` logs the state (`rasa_menu_open`) to maintain an uninterrupted user experience.
* **Backend Pagination Tracking:** The total pages, remaining pages, and current boundaries are all calculated safely in the Python backend to prevent out-of-bounds rendering on the frontend.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 
Feel free to check the [issues page](https://github.com/Chitra-ai-coder/RECIPE_ONE_PLACE/issues) if you want to contribute.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📬 Contact

**Chitra-ai-coder** - [GitHub Profile](https://github.com/Chitra-ai-coder)

Project Link: [https://github.com/Chitra-ai-coder/RECIPE_ONE_PLACE](https://github.com/Chitra-ai-coder/RECIPE_ONE_PLACE)
