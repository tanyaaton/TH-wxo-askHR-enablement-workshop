from ibm_watsonx_orchestrate.agent_builder.tools import tool
from ibm_watsonx_orchestrate.agent_builder.connections import ConnectionType
from ibm_watsonx_orchestrate.run import connections
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Employee Leave Balance API",
    description="API wrapper for LangFlow leave balance agent",
    version="1.0.0"
)

# ----- Request Model -----
class LeaveRequest(BaseModel):
    user_query: str


def get_employee_leave_balance(user_query: str) -> str:
    """This tool connect to langflow leave balance management flow to get employee leave balance info.
    
    Args:
        employee_id (str): The employee's unique ID.
        
    Returns:
        A JSON string containing the employee's information.
    """

    url = "https://aws-us-east-2.langflow.datastax.com/lf/1a574151-3fc5-448e-bf7e-d88fd4958c49/api/v1/run/1f6d3bed-ecf3-4f9a-9f67-154fbc68c2ba"  # The complete API endpoint URL for this flow

    # Request payload configuration
    payload = {
        "output_type": "chat",
        "input_type": "chat",
        "input_value": user_query
    }
    payload["session_id"] = str(uuid.uuid4())

    headers = { 
        "X-DataStax-Current-Org": os.getenv("ORG_ID"), 
        "Authorization": "Bearer "+ os.getenv("ASTRA_TOKEN"), 
        "Content-Type": "application/json", 
        "Accept": "application/json", 
    }
    response = requests.request("POST", url, json=payload, headers=headers)

    return response.text

# ----- API Endpoint -----
@app.post("/leavebalance")
def leavebalance_api(request: LeaveRequest):
    """
    API endpoint to query employee leave balance.
    """
    result = get_employee_leave_balance(request.user_query)
    return {"result": result}


# ----- Run the API -----
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
    


