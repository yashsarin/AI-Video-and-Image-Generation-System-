# AI-Video-and-Image-Generation-System-
This project is designed to assess your programming skills, creativity, problem-solving abilities, and ability to work with AI tools.


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
Log every user login attempt and content view in the database.


Part 4: Notifications
Notify the user when their content is ready:
Use email or a system notification (e.g., desktop notification or in-terminal message).
Include a link to the web page where they can view their content.
Allow users to specify a "notification time" for when they'd like to receive the notification.
