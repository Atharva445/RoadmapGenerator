# import streamlit as st
# import joblib

# skill_to_col = joblib.load("skill_to_col.pkl")
# col_to_skill = joblib.load("col_to_skill.pkl")
# role_to_skills = joblib.load("role_to_skills_hybrid.pkl")
# skill_salary = joblib.load("skill_salary.pkl")

# banned_skills = {"fortran", "cobol", "pascal", "vb.net", "assembly"}


# st.title("🚀 AI-Powered Roadmap Generator")

# # Dropdown for role
# target_role = st.selectbox("🎯 Select your target role:", list(role_to_skills.keys()))

# # Multi-select for known skills
# user_skills = st.multiselect("🛠️ Select the skills you already know:", list(skill_to_col.keys()))

# if st.button("Generate Roadmap"):
#     if target_role:
#         st.write(f"📌 Recommended Roadmap for **{target_role}**:")

#         skills_list = role_to_skills.get(target_role, [])

#         #  Remove duplicates & filter out banned + user-known
#         seen = set()
#         unique_skills = []
#         for s in skills_list:
#             s_lower = s.lower()
#             if s not in seen and s_lower not in banned_skills and s not in user_skills:
#                 unique_skills.append(s)
#                 seen.add(s)

#         #  Show roadmap in whitelist order but with salary impact
#         for i, skill in enumerate(unique_skills, 1):
#             avg_salary = skill_salary.get(skill, "N/A")
#             st.markdown(
#                 f"**Step {i}:** Learn `{skill}` "
#                 f"(💰 Avg Salary in Current Market: {avg_salary if avg_salary=='N/A' else '$'+str(avg_salary)})"
#             )
import streamlit as st
import joblib
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

# ------------------------------
# Load Artifacts
# ------------------------------
skill_to_col = joblib.load("skill_to_col.pkl")
col_to_skill = joblib.load("col_to_skill.pkl")
role_to_skills = joblib.load("role_to_skills_hybrid.pkl")
skill_salary = joblib.load("skill_salary.pkl")


load_dotenv()  # loads .env file
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
CSE_ID = os.getenv("CSE_ID")

def get_youtube_videos(skill, max_results=2):
    try:
        youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
        request = youtube.search().list(
            part="snippet",
            q=f"Learn {skill}",
            type="video",
            maxResults=max_results
        )
        response = request.execute()
        videos = []
        for item in response["items"]:
            title = item["snippet"]["title"]
            url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            videos.append({"title": title, "url": url})
        return videos
    except Exception as e:
        return [{"title": "Error fetching YouTube videos", "url": ""}]

# ------------------------------
# Google Search API (Certifications)
# ------------------------------
def get_certifications(skill, max_results=2):
    try:
        service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
        query = f"Best {skill} certification course"
        res = service.cse().list(q=query, cx=CSE_ID, num=max_results).execute()
        certs = []
        if "items" in res:
            for item in res["items"]:
                certs.append({"title": item["title"], "link": item["link"]})
        return certs
    except Exception as e:
        return [{"title": "Error fetching certifications", "link": ""}]

# ------------------------------
# UI
# ------------------------------
st.title("🚀 AI-Powered Roadmap Generator with Learning Resources")

target_role = st.selectbox("🎯 Select your target role:", list(role_to_skills.keys()))
user_skills = st.multiselect("🛠️ Select the skills you already know:", list(skill_to_col.keys()))

if st.button("Generate Roadmap"):
    if target_role:
        st.write(f"📌 Recommended Roadmap for **{target_role}**:")

        skills_list = role_to_skills.get(target_role, [])

        seen = set()
        unique_skills = []
        for s in skills_list:
            if s not in seen and s not in user_skills:
                unique_skills.append(s)
                seen.add(s)

        for i, skill in enumerate(unique_skills, 1):
            avg_salary = skill_salary.get(skill, "N/A")

            st.markdown(
                f"### Step {i}: Learn `{skill}` "
                f"(💰 Avg Salary: {avg_salary if avg_salary=='N/A' else '$'+str(avg_salary)})"
            )

            # 🎥 YouTube
            st.write("📺 YouTube Tutorials:")
            for vid in get_youtube_videos(skill):
                st.markdown(f"- [{vid['title']}]({vid['url']})")

            # 🎓 Certifications (Dynamic via Google Search)
            st.write("🎓 Certification Links:")
            for cert in get_certifications(skill):
                st.markdown(f"- [{cert['title']}]({cert['link']})")

            st.write("---")

