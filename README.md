# ISS Locator App
### Find the ground location and a list of crew members aboard the ISS
This is a simple Flask App that uses the Open Notify [ISS Current Location](http://open-notify.org/Open-Notify-API/ISS-Location-Now/) and [People in Space](http://open-notify.org/Open-Notify-API/People-In-Space/) APIs to show the ground location of the ISS and a list of the astronauts aboard the spacecraft.

### Installation
1. Clone the repo
`git clone https://github.com/j-tew/iss_location.git`
2. Go into the project directory
`cd iss_location`
3. Create a virtual environment
`python3 -m venv venv`
4. Activate the virtual environment
`source venv/bin/activate`
5. Install dependencies
`pip install -r requirements.txt`
6. Start the app
`flask run`
7. View the webpage by navigating to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser




### The skills I applied to this project:
- Flask framework
- Jinja templating
- Basic front end UI/UX with HTML and CSS
- Interacting with an API
- Parsing JSON with Python
