from pydantic import BaseModel, EmailStr, ValidationError, Field
from typing import Optional
from datetime import date
import json

class UserInput(BaseModel):
    name: str
    email: EmailStr
    query: str
    order_id: Optional[int] = Field(
        None,
        description="5-digit order number (cannot start with 0)",
        ge=10000,
        le=99999
    )
    purchase_date: Optional[date] = None

def validate_user_input(input_data):
    try:
        user_input = UserInput(**input_data)
        print(f"✅ Valid user input created:")
        print(f"{user_input.model_dump_json(indent=2)}")
        return user_input
    except ValidationError as e:
        print(f"❌ Validation error occurred:")
        for error in e.errors():
            print(f"  - {error['loc'][0]}: {error['msg']}")
        return None
    
input_data = {
    "name": "Joe User",
    "email": "joe.user@example.com",
    "query": "I forgot my password."
}
user_input = validate_user_input(input_data=input_data)


# def execute():
#     print('test')

# if __name__ == "__main__":
#     execute()