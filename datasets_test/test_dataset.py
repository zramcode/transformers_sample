from datasets import load_dataset
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
from fastapi import APIRouter
from pydantic import BaseModel
import ast

router = APIRouter()
ds = load_dataset("lukebarousse/data_jobs") #it has the none in job_skills
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_skillslist_fromdataset(row_data_dataset):
    skills = set()
    
    for row in row_data_dataset:
        text = row["job_skills"]
        if text is not None:
            for word in text.split(','):
                clean_word = word.strip().strip("'").strip('"').strip('[').strip(']').lower()
                if clean_word:  
                    skills.add(clean_word)
    return list(skills)


def get_mathchedkills_byuserinput(skill_list,user_input,threshold,top_k):
   
   user_embedding = model.encode(user_input.lower(), convert_to_tensor=True)
   skill_embeddings = model.encode(skill_list, convert_to_tensor=True)
   cosine_scores = util.cos_sim(user_embedding, skill_embeddings)[0]
   
   filtered_skills = [(skill, float(score)) for skill, score in zip(skill_list, cosine_scores) if score >= threshold]
   #filtered_skills = [s for s in scored_skills if s[1] >= threshold]

   #op_skills = [skill_list[i] for i, score in enumerate(cosine_scores[0]) if score > 0.5]

   #if top_k:
    #     filtered_skills = sorted(filtered_skills, key=lambda x: x[1], reverse=True)[:top_k]
   
   unique_skills = set(map(lambda s: s[0].strip().strip("'").lower(), filtered_skills))
   
   return unique_skills


def extract_skills_with_scores(text, skill_list, threshold=0.7):
    text_embedding = model.encode(text, convert_to_tensor=True)
    skill_embeddings = model.encode(skill_list, convert_to_tensor=True)

    cosine_scores = util.cos_sim(text_embedding, skill_embeddings)[0]

    skill_scores = []
    for i, score in enumerate(cosine_scores):
        skill_scores.append((skill_list[i], float(score)))  

    
    sorted_skills = sorted(skill_scores, key=lambda x: x[1], reverse=True)

    selected_skills = [s for s in sorted_skills if s[1] > threshold]

    return selected_skills, sorted_skills


def get_match_jobtilte(user_input : str):

    
    #ner = pipeline("token-classification", model="jjzha/jobbert_skill_extraction")   #false answer it returns null
    #ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")   false answer it returns only the skills with uppercase
    #print(type(ds["train"][1]['job_skills']))
    #print(extract_skills(user_input))

    #user_input = "I have worked with SQL and Tableau. I'm learning Python and love analyzing data."
    skill_list =  get_skillslist_fromdataset(ds["train"].select(range(100)))
    matched_skill_names = get_mathchedkills_byuserinput(skill_list, user_input,0.45,3)

    required_matches = 2
    matched_jobs = set()

    for item in ds["train"].select(range(100)):
        job_skills = item["job_skills"]
        if not job_skills:
          continue
    
        job_skills_list = ast.literal_eval(job_skills)
    
        common_skills = set(matched_skill_names).intersection(job_skills_list)
        if len(common_skills) >= required_matches:
            job_title = item["job_title_short"]
            matched_jobs.add(job_title)

    # if matched_skill_names.issubset(set(job_skills_list)):
    #     job_title = item["job_title_short"]
    #     if job_title not in matched_jobs:
    #        matched_jobs.add(job_title
    #            #{
    #          #"title": job_title
    #            #"company": item.get("company_name"),
    #            #"skills_matched": list(overlap)
    #     #}
    #        )

    #for job in matched_jobs:
    return matched_jobs


class myrequestmodel(BaseModel):
    input:str

@router.post("/sentenceTransformer")
def get_responce(request : myrequestmodel):
    match_jobtitle = get_match_jobtilte(request.input)
    return match_jobtitle








