from resume_parser import parse_resume
from job_matcher import match_resume_to_job

with open("sample_resume.txt", "r") as f:
    resume_text = f.read()


with open("sample_jobdesc.txt", "r") as f:
    job_text = f.read()

parsed = parse_resume(resume_text)
print("Name: ", parsed["name"])
print("Email: ", parsed["email"])
print("Skills: ", parsed["skills"])

match_score = match_resume_to_job(resume_text, job_text)
print("Match Score: ", match_score, "%")