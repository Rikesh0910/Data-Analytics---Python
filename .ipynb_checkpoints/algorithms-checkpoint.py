"""
lis1 = [4,8,2,9,1,17,3]
lis1.sort()
def binary_search(lis, tar):
    left = 0
    right = len(lis) - 1
    while left <= right:
        mid = (left + right) // 2
        if lis[mid] == tar:
            return mid
        elif lis[mid] < tar:
            left = mid + 1
        elif lis[mid] > tar:
            right = mid - 1
    return -1

print(lis1)
print(binary_search(lis1, 9))


job_details = [
    {"job_role": "Software Developer", "job_skills": ["Python", "Django", "SQL"], "job_hire_date": "2023-11-01"},
    {"job_role": "Data Analyst", "job_skills": ["Excel", "Power BI", "Python"], "job_hire_date": "2024-01-15"},
    {"job_role": "Frontend Developer", "job_skills": ["HTML", "CSS", "JavaScript", "React"], "job_hire_date": "2023-12-05"}
]

from datetime import datetime

for job in job_details:
    date_jobs = datetime.strptime(job["job_hire_date"], "%Y-%m-%d")
    print(date_jobs)


import pandas as pd

read_pd = pd.read_csv("samp_data.csv")

data_view = pd.DataFrame(read_pd)


for index, value in data_view.iterrows():
    if value["department"] == "Marketing":
        print(value["name"])



import numpy as np

base_salary = np.array([20000, 40000, 50000, 80000])
bonus_rate = np.array([0.4, 0.8, 1.0, 5])

total_salary = base_salary * (1 + bonus_rate)
print(total_salary)
print(np.mean(total_salary))

"""
import pandas as pd
from datasets import load_dataset

dataset = load_dataset('lukebarousse/data_jobs')

df = dataset['train'].to_pandas()

#print(pd[(pd.job_title_short == "Data Analyst") & (pd.salary_year_avg > 150000)])

#df['job_posted_date'] = pd.to_datetime(df.job_posted_date)
#df['job_posted_month'] = pd.to_datetime(df.job_posted_date.dt.month)
print(df)
#df.sort_values(df["job_posted_date"])