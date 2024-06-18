from datetime import datetime
import google.generativeai as genai

from common.models.job_offer_model import JobOfferModel
from common.models.personal_info_model import PersonalInfoModel


class SummaryProcess:
  def __init__(self):
    self.prompt = self.__base_prompt()
  
  def build_job_offer(self, job_offer: JobOfferModel):
    
    self.prompt += (
      "Job Offer:\n"
      f"{job_offer.description}\n"
      f"Responsibilities:\n{"\n".join(job_offer.responsibilities)}\n"
      f"Requirements:\n{"\n".join(job_offer.requirements)}\n"
    )

    return self
  
  def build_job_experience(self, account_id: str):
    job_experiences = []
    jobs = list(PersonalInfoModel.objects.aggregate(self.__job_experience_pipeline(account_id)))
    total_years = self.__job_years_experience(jobs)
    
    for job in jobs:
      responsibilities = "\n".join(job['responsibilities'])
      tags = ", ".join(job['tags'])
      
      job_experiences.append((
        f"In {job['company']} "
        f"as a {job['role']}, I've worked with {tags}."
        f"Responsibilities included: {responsibilities}."
      ))
    
    self.prompt += (
      "Job experience:\n"
      f"Total years of experience: {total_years}\n"
      f"{'\n'.join(job_experiences)}"
    )

    return self

  def __base_prompt(self) -> tuple:
    prompt = (
      "You are a recruitment coach."
      "You will be provided with the job offer as well as the user's experience and skills."
      "Your task is to help create an attractive and relevant professional summary that highlights the user's qualities in relation to the job offer."
      "Provide a professional summary in plain text format, without any additional explanations or instructions."
      "Only mention the technologies requested in the job offer that relate to the user's background.\n"
    )
    return prompt
  
  def __job_years_experience(self, jobs) -> int:
    first_job = jobs[-1]['start_at']
    last_job = jobs[0]['end_at'] if jobs[0]['end_at'] else datetime.now()

    diff_days = (last_job - first_job).days
    return diff_days // 365

  def __job_experience_pipeline(self, account_id: str) -> list:
    return [
      {
        '$match': { 'account_id': account_id }
      }, {
        '$lookup': {
          'from': 'job_experiences', 
          'localField': '_id', 
          'foreignField': 'personal_info', 
          'as': 'job_experiences'
        }
      }, {
        '$unwind': '$job_experiences'
      }, {
        '$sort': { 'job_experiences.start_at': -1 }
      }, {
        '$replaceRoot': { 'newRoot': '$job_experiences' }
      }, {
        '$project': {
          '_id': False, 
          'company': True, 
          'role': True, 
          'start_at': True, 
          'end_at': True, 
          'tags': True, 
          'responsibilities': True
        }
      }
    ]