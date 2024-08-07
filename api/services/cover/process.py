from datetime import datetime

from common.models.job_offer_model import JobOfferModel
from common.models.personal_info_model import PersonalInfoModel


class CoverProcess:
  def __init__(self, job_offer: JobOfferModel):
    self.prompt = self.__base_prompt()
    self.job_offer = job_offer
  
  def build_job_offer(self):
    
    self.prompt += (
      "Job Offer:\n"
      f"Company:\n{self.job_offer['company']} ({self.job_offer['description']}).\n"
      f"Position:\n{self.job_offer['position']}\n"
      f"Responsibilities:\n{"\n".join(self.job_offer['responsibilities'])}\n"
      f"Requirements:\n{"\n".join(self.job_offer['requirements'])}\n"
    )

    return self
  
  def build_total_years_of_experience(self):
    first_job = self.job_offer['job_experiences'][0]['start_at']
    last_job = self.job_offer['job_experiences'][-1]['end_at'] if self.job_offer['job_experiences'][-1]['end_at'] else datetime.now()

    diff_days = (last_job - first_job).days

    self.prompt += (
      f"Total years of experience: {diff_days // 365}.\n"
    )

    return self

  def build_job_experience(self):
    job_experiences = []
    for job in self.job_offer['job_experiences']:
      responsibilities = "\n".join(job['responsibilities'])
      tags = ", ".join(job['tags'])
      
      job_experiences.append((
        f"In {job['company']} ({job['description']})"
        f"as a {job['role']}, I've worked with {tags}."
        f"Responsibilities included: {responsibilities}."
      ))
    
    self.prompt += (
      "Job experience:\n"
      f"{'\n'.join(job_experiences)}"
    )

    return self

  def __base_prompt(self) -> tuple:
    prompt = (
      "You are a recruitment coach."
      "You will be provided with the job offer as well as the user's experience."
      "Your task is to help create an attractive and relevant professional cover letter in english that highlights the user's qualities in relation to the job offer."
      "Explain why why the user is interested in the job position and in the company."
      "Divide the motivations into technical and soft competencies."
      "Provide a professional summary in plain text format, without any additional explanations or instructions."
      "Only highlight the technologies and skills requested in the job offer that relate to the user's experience."
      "Ignore any technologies or skills in the user's experience that are not mentioned in the job offer."
      "Do not include any greeting or closing phrases."
      "Use the provided data directly without placeholders.\n"
    )
    return prompt