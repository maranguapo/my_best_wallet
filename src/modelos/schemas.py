from pydantic import BaseModel

class GetTicketsRequest(BaseModel):
    ticketType: str
