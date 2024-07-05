class JobOfferURLMixin:
  
  def get_url(self, obj):
    return {
      'resume': [
        f"http://localhost:8000/web/documents/resume/{obj.id}.pdf",
        f"http://localhost:8000/web/documents/resume/{obj.id}.doc",
      ]
    }