in this lab we are going to import leave management agent from langflow which connect to the Astra db

first, we will connect to the Langflow agent using OpenAPI


## STEPS
we will connect to the Langlfow agent using OpenAPI through python.
You can choose to Set up connection for the tool using UI or ADK.

#### set up connection through UI

1. Create new connection name `langflow_secret`, choose tye `Key value`

    ...


#### set up connection through ADK

1. Create .env file and add the following value to the file (You will recieve this through email)
    ```
    ASTRA_TOKEN=AstraCS:oCfnb.....
    ORG_ID=cfe0f....
    ```
2. run the following command in `LAB_3_LEAVE_MANAGEMENT_AGENT_3` folder
    ```
    bash set_connection.sh
    ```

#### Import agent and tool

After set up connection, use the following ADK command to import Langflow tools:
```
bash import-all.sh
```
the agent should pop up on your watsonx.Orchestrate Agent builder page.

use the following questions to test the agent
- give me leave balance of EMP001
- give me leave balance of EMP002
- give me leave balance of EMP003

## Langflow
Now, after we have already connect the tools to Langflow, let's have a look in side the flow on what happened inside
1. Open a hosted Langflow service provided by DataStax iwth the fllowing link: [DataStax Langflow](https://astra.datastax.com/signup?type=langflow)
![alt text](images/image-1.png)
2. Sign up and Sign in to Langflow, you will land on the following page
![alt text](images/image-2.png)
3. Drag and Drop file `Langflow/Leave_balance.json` to the page directly. You will now have Leave balance as one of your flow.
![alt text](images/image-3.png)
4. Click in the flow. Here, you can observe how this leave balance tool works.
![alt text](images/image-4.png)

Component of the flow includes:
- Groq AI model gateway
- AstraDB tool connecting to external database
- Agent with prompt instruction
- Chat input 
- Chat output

5. Add values to 3 global connection variables

6. Click on `Playground` on the top right to try running flow on Langflow


### Langlfow API
The API tool you used to connect to Watsonx Orchestrate agent is provided from the prebuilt Langflow flow on cloud. However, if you want to adjust the flow tool and use your own API, you can access them here:



