# musical

**With Docker:**

> - Requirements:

> 1. Install the Docker Apple chip(m1): https://docs.docker.com/desktop/mac/apple-silicon/
> 2. For windows or other environment: https://docs.docker.com/engine/install/
> - Install Docker-compose: https://docs.docker.com/compose/install/

**How to run the application**

> 1. Unzip the attachment 
> 2. Install docker
> 3. Run this command : docker-compose up –build 
>
**Note: I set the 8000 port for the local server.**
> 4. Open the Browser hit this endpoints: ```http://127.0.0.1:8000/musical```

**Without Docker:**
> 1. Unzip the attachment
> 2. Make a virtual environment(Installation )
   >> a. Use this command : virtualenv ‘file_name”
   >> >
   >> b. Activate the Virtual Environment: source “file_name”/bin/activate
 >
> 3. Run the requirements: ```pip install -r requirements.txt```
Note: requirements.txt file is already available in the attachment file.

> 4. Start the server:```python manage.py runserver```
> 5. Open the Browser hit this endpoints: ```http://127.0.0.1:8000/musical```

