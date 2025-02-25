from pydantic import BaseModel

class CustomerReview(BaseModel):
    review: str
    rating: int
    reply: str
