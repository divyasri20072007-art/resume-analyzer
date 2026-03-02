# Resume Analyzer

## About This Project

I built this project to understand how resumes can be compared with job descriptions using Python.

The goal of this project is to check how well a resume matches a job requirement by calculating a match percentage and identifying missing skills.

---

## What This Project Does

- Reads a resume file
- Reads a job description file
- Compares skills
- Shows matching and missing skills
- Calculates overall match percentage
- Uses TF-IDF and cosine similarity to measure text similarity

---

## Technologies Used

- Python
- File Handling
- Basic String Matching
- scikit-learn (TF-IDF, Cosine Similarity)

---

## How It Works

1. The program reads both resume and job description.
2. It checks for required skills in both.
3. It calculates the percentage of matching skills.
4. It also uses TF-IDF vectorization and cosine similarity to measure overall similarity between texts.

---

## How to Run

1. Install Python
2. Install required library:

   python -m pip install scikit-learn

3. Run:

   python analyzer.py

---

## Future Improvements

- Add PDF resume support
- Improve skill extraction
- Create a web interface
- Make skill list dynamic

---

## Author

Divya
