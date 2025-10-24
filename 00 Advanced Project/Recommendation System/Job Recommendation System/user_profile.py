import pandas as pd

# Create a list of 10 dummy user profiles
user_data = [
    {
        "user_id": 1,
        "name": "Faisal Zamir",
        "experience_level": "Mid",
        "job_title": "Machine Learning Engineer",
        "skills": "Python, Scikit-learn, TensorFlow, NLP",
        "preferred_industry": "Information Technology",
        "location": "Islamabad, PK",
        "years_experience": 3,
        "education_level": "Masters"
    },
    {
        "user_id": 2,
        "name": "Sara Ahmed",
        "experience_level": "Entry",
        "job_title": "Web Developer",
        "skills": "HTML, CSS, JavaScript, React, PHP",
        "preferred_industry": "Software Development",
        "location": "Lahore, PK",
        "years_experience": 1,
        "education_level": "Bachelors"
    },
    {
        "user_id": 3,
        "name": "Ali Khan",
        "experience_level": "Senior",
        "job_title": "Data Scientist",
        "skills": "Python, Pandas, SQL, ML, Statistics",
        "preferred_industry": "AI Research",
        "location": "Karachi, PK",
        "years_experience": 6,
        "education_level": "Masters"
    },
    {
        "user_id": 4,
        "name": "Ayesha Noor",
        "experience_level": "Mid",
        "job_title": "Android Developer",
        "skills": "Java, Kotlin, Android Studio, Firebase",
        "preferred_industry": "Mobile Development",
        "location": "Rawalpindi, PK",
        "years_experience": 4,
        "education_level": "Bachelors"
    },
    {
        "user_id": 5,
        "name": "Hassan Raza",
        "experience_level": "Entry",
        "job_title": "Data Analyst",
        "skills": "Excel, SQL, PowerBI, Python",
        "preferred_industry": "Business Analytics",
        "location": "Faisalabad, PK",
        "years_experience": 2,
        "education_level": "Bachelors"
    },
    {
        "user_id": 6,
        "name": "Maryam Khan",
        "experience_level": "Mid",
        "job_title": "Frontend Developer",
        "skills": "JavaScript, React, Vue, HTML, CSS",
        "preferred_industry": "Web Development",
        "location": "Multan, PK",
        "years_experience": 3,
        "education_level": "Bachelors"
    },
    {
        "user_id": 7,
        "name": "Bilal Ahmed",
        "experience_level": "Senior",
        "job_title": "DevOps Engineer",
        "skills": "AWS, Docker, Kubernetes, CI/CD, Linux",
        "preferred_industry": "Cloud Computing",
        "location": "Karachi, PK",
        "years_experience": 7,
        "education_level": "Masters"
    },
    {
        "user_id": 8,
        "name": "Zara Ali",
        "experience_level": "Entry",
        "job_title": "QA Tester",
        "skills": "Selenium, Python, Manual Testing, Automation",
        "preferred_industry": "Software Testing",
        "location": "Lahore, PK",
        "years_experience": 1,
        "education_level": "Bachelors"
    },
    {
        "user_id": 9,
        "name": "Usman Sheikh",
        "experience_level": "Mid",
        "job_title": "Backend Developer",
        "skills": "Python, Django, REST API, SQL",
        "preferred_industry": "Software Development",
        "location": "Islamabad, PK",
        "years_experience": 4,
        "education_level": "Bachelors"
    },
    {
        "user_id": 10,
        "name": "Sana Iqbal",
        "experience_level": "Entry",
        "job_title": "Business Analyst",
        "skills": "Excel, SQL, PowerBI, Data Analysis",
        "preferred_industry": "Business Analytics",
        "location": "Rawalpindi, PK",
        "years_experience": 2,
        "education_level": "Bachelors"
    }
]

# Convert to DataFrame
df_users = pd.DataFrame(user_data)

# Save to CSV
df_users.to_csv("user_profiles.csv", index=False)

print("CSV file 'user_profiles.csv' created successfully!")
