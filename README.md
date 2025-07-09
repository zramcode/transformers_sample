# transformers_sample

🔍 Job Skill Matcher using Sentence Embeddings
This project extracts and matches job skills from real-world job postings using HuggingFace datasets and Sentence Transformers.

🧠 What it does
✅ Loads a dataset of real job postings from HuggingFace: lukebarousse/data_jobs

✅ Extracts clean skill keywords from the job_skills field

✅ Takes a user input text (like a CV summary or sentence)

✅ Matches the input to the most semantically relevant skills using cosine similarity

✅ Filters job titles based on overlapping skills with the input

🧰 Tech Stack
datasets by HuggingFace

sentence-transformers with model: all-MiniLM-L6-v2

Optional: NER pipelines (commented out, currently not used)

📌 Example
User Input:

text
Copy
Edit
I have worked with SQL and Tableau. I'm learning Python and love analyzing data.
Output:

python
Copy
Edit
{'Data Analyst', 'Business Intelligence Analyst', 'Analytics Engineer'}
These are job titles that match at least 2 skills from the user input.

🧼 Notes
job_skills field may contain None values or malformed strings. The script handles this with ast.literal_eval and data cleaning.

Matching is done using cosine similarity and thresholding.

The project is focused on matching semantics, not just exact words.

🚀 To Do
 Add front-end interface (e.g. Gradio or Streamlit)

 Improve NER skill extraction with a more reliable model

 Support dynamic top-k filtering of results

📁 File Structure
bash
Copy
Edit
.
├── main.py             # Main script with skill extraction and job matching
├── README.md           # Project overview and usage
└── requirements.txt    # Libraries needed
✅ Installation
bash
Copy
Edit
pip install datasets sentence-transformers
