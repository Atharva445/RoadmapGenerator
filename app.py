import streamlit as st
import joblib

# --- Load Artifacts ---
skill_to_col = joblib.load("skill_to_col.pkl")
col_to_skill = joblib.load("col_to_skill.pkl")
role_to_skills = joblib.load("role_to_skills_hybrid.pkl")
skill_salary = joblib.load("skill_salary.pkl")

# --- Blacklist of outdated/irrelevant skills ---
banned_skills = {"fortran", "cobol", "pascal", "vb.net", "assembly"}

# --- UI ---
st.title("🚀 AI-Powered Roadmap Generator")

# Dropdown for role
target_role = st.selectbox("🎯 Select your target role:", list(role_to_skills.keys()))

# Multi-select for known skills
user_skills = st.multiselect("🛠️ Select the skills you already know:", list(skill_to_col.keys()))

if st.button("Generate Roadmap"):
    if target_role:
        st.write(f"📌 Recommended Roadmap for **{target_role}**:")

        # ✅ Whitelist-defined priority order
        skills_list = role_to_skills.get(target_role, [])

        # 🔹 Remove duplicates & filter out banned + user-known
        seen = set()
        unique_skills = []
        for s in skills_list:
            s_lower = s.lower()
            if s not in seen and s_lower not in banned_skills and s not in user_skills:
                unique_skills.append(s)
                seen.add(s)

        # 🔹 Show roadmap in whitelist order but with salary impact
        for i, skill in enumerate(unique_skills, 1):
            avg_salary = skill_salary.get(skill, "N/A")
            st.markdown(
                f"**Step {i}:** Learn `{skill}` "
                f"(💰 Avg Salary in Current Market: {avg_salary if avg_salary=='N/A' else '$'+str(avg_salary)})"
            )
