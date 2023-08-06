# gym-trackin
Track physical actitivies every day. 

This API is developed using flask

Use of the api:
The following usage is for linux only
- run setup.sh (if you run into problem with permisson issues, need to run `chmod +x setup.sh` to make it executable)
The setup script will run the gunicorn server
- can send GET or POST requests to the api to view logs each day and add more logs
- GET requests can be done via browser or cmd, but at this point POST requests can only be made via cmd.

Next steps.
Importance is marked by *. The more *, the more important a feature/step is. 
- Add authentication page. *****
- Need to create a database to store data (user data, logs etc). This is to ensure persistent storage. *****
- Add user class for user profiles. *****
- Add try-catch structure to catch errors for unexpected inputs or routes. ***
- Add tests (with pytests maybe?). ****
- Add CIs to automate tests in PRs or merges. **
- Add automated scripts to setup environments. **

