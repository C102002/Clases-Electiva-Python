from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: str = Field(...,min_length=5)
    is_active: bool

try:
    Blog(title="hi",is_active=False)
except Exception as e:
    # Deberia de dar error porque el titulo es menor a 5
    print(f"errores:{e.errors()}")
    print(f"error:{e.json()}")

blog2=Blog(title="My Second Blog",is_active=True)
print(f"blog2: {blog2}")
# Deberia de no dar error porque el titulo es mayor a 5