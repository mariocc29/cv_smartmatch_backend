from common.models.job_offer_model import JobOfferModel


class JobOfferURLMixin:
  
  def get_url(self, obj: JobOfferModel):
    return {
      'resume': [
        f"http://localhost:8000/web/documents/resume/{obj.id}.pdf",
        f"http://localhost:8000/web/documents/resume/{obj.id}.doc",
      ],
      'cover': [
        f"http://localhost:8000/web/documents/cover/{obj.id}.pdf",
        f"http://localhost:8000/web/documents/cover/{obj.id}.doc",
      ]
    }