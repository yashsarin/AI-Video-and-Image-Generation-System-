# AI-Video-and-Image-Generation-System-


# This code covers several parts of a content generation and notification system:
1.	Content Generation (Videos & Images): It generates videos and images by sending API requests and stores them in user-specific directories.
2.	Database Management: It uses SQLite to manage user data and log content views. A table is created to store user content and track user actions.
3.	Flask Web App: The app allows users to log in, view content (videos and images), and log out. It logs user actions and stores content view data in the database.
4.	Notifications: It sends notifications when content is ready, either by email or system notification using plyer. The email functionality uses Gmail's SMTP but failed due to login issues, while system notifications are sent successfully.
5.	Scheduling Notifications: The script schedules notifications for a future time and sends emails and system notifications accordingly
# CONTENT PAGE 
This HTML template is designed for a web page that informs users their content is being processed. It consists of the following main sections:
1.	Header: Displays a greeting with "HELLO USER".
2.	Content Section:
o	A message indicating that the content is being generated and the user should check back later.
o	A placeholder for a loading animation (<div class="loader">), which will be styled using CSS to indicate content is loading.
o	A secondary message thanking the user for their patience.
3.	Logout Section: Includes a logout button that links to a Flask route using {{ url_for('logout') }} to dynamically generate the URL for logging out.
4.	External CSS: The page links to an external stylesheet (styles.css) using Flask’s url_for to generate the correct URL for the static file.
Flask is used to dynamically generate URLs (like the CSS file path and logout URL) using Jinja templating. The page is intended to provide feedback while content is being processed and allow the user to log out.

# DASH PAGE
This HTML template is for a dashboard page displaying videos and images with a logout button. Key points:
•	Header: Greets the user with "WELCOME USER !!".
•	Videos Section: Displays a single video using the <video> tag. The video path is local to the user's machine, which may not work in production.
•	Images Section: Displays a single image with a local file path.
•	Logout Button: A link for logging out, dynamically generated using Flask's url_for.
The page uses local file paths for media, which should be replaced with server paths in a real-world app. The CSS is linked dynamically with Flask.

# LOGIN PAGE
This is a login page HTML template with the following key features:
•	Flash Messages: Displays any notifications or errors from Flask.
•	Login Form: Contains an input for the User ID and a submit button to send a POST request.
•	Register Link: Offers a link to the registration page.
It uses Flask's url_for to generate URLs dynamically and links to an external CSS file for styling.

# REGISTER
This is a registration page template with the following features:
•	Flash Message: Displays a message (e.g., error or success) based on a Flask flash category.
•	Registration Form: Includes an input for a unique User ID and a submit button.
•	Login Link: Provides a link to the login page for users with an existing account.
The page uses Flask's url_for to generate dynamic URLs and links to an external CSS file for styling.





ASSIGNEMENT- 
Part 1: Text-to-Video and Text-to-Image Generation
Accept a text prompt from the user.
Generate at least:
5 videos: Use AI video generation tools like RunwayML or other accessible APIs.
5 images: Use AI tools such as OpenAI’s DALL·E or Stable Diffusion.
Save the generated content:
Videos should be saved as .mp4 files.
Images should be saved as .jpg or .png files.
Store them in a directory named generated_content/<user_id>/.

Part 2: Storing and Managing Content
Maintain a database (SQL or any other DB) with the following structure:
user_id (unique identifier for the user)
prompt (text provided by the user)
video_paths (list of file paths to the generated videos)
image_paths (list of file paths to the generated images)
status (generation status: "Processing" or "Completed")
generated_at (timestamp of content generation)
Once the generation is complete:
Mark the status as "Completed" in the database.
Notify the user that their content is ready (via email or console output) at specified time.

Part 3: User Access and Web Page Display
Create a simple web page using Flask or FastAPI or any other framework to display the content:
The page should allow users to log in using a unique identifier (user_id).
If the user has completed content, display:
Videos in a gallery view with playback functionality.
Images in a grid layout.
If the content is still processing, show a message:
"Your content is being generated. Please check back later."
Log every user login attempt and content view in the database

Part 4: Notifications
Notify the user when their content is ready:
Use email or a system notification (e.g., desktop notification or in-terminal message).
Include a link to the web page where they can view their content.
Allow users to specify a "notification time" for when they'd like to receive the notification.
