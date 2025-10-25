from pydantic import BaseModel, Field

class BookSchema(BaseModel):
    id: int = Field(..., description="Book identifier")
    title: str = Field(..., description="Book title")
    price: float = Field(..., description="Book price")
    rating: int = Field(..., description="Book rating")
    availability: str = Field(..., description="Book availability")
    category: str = Field(..., description="Book category")
    image_url: str = Field(..., description="Book image url")

    class Config:
        from_attributes = True