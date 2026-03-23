# End-To-End-Data-Science-Project

Company Name: CodeTech It Solutions

Name : Prem M

Domain : Data Science

Duration : 4 Weeks

Intern ID : CTIS6711

Desprition of the task:

This Python script illustrates how to deploy a trained machine learning model as a web application using the lightweight framework Flask. The purpose of the application is to provide an easy-to-use interface where users can input their years of experience and receive a predicted salary, making the model accessible beyond a programming environment.

The script begins by importing the required modules. Flask is used to handle web requests and create routes, while the pickle module is used to load a pre-trained machine learning model from a file. The application is initialized with Flask(__name__), which prepares the app to receive and respond to HTTP requests. This setup forms the backbone of the web server.

Next, the trained model is loaded from the file "Task3\data\model.pkl". This model was previously created using a regression algorithm, likely from scikit-learn, and saved using pickle. By loading the model instead of retraining it, the application becomes efficient and ready for real-time predictions. This approach is standard in production systems, where models are trained offline and deployed for inference.

The application defines two routes to handle user interaction. The first route ("/") acts as the home page. When accessed, it returns a simple HTML form embedded directly in the Python code. This form contains a text input field labeled “Experience” and a submit button. The user enters their years of experience into this field, and upon submission, the data is sent to the /predict route using the POST method.

The second route ("/predict") processes the form data and generates a prediction. Inside this function, the input value is retrieved using request.form["exp"]. Since data from web forms is always received as a string, it is converted into a floating-point number to match the format expected by the model. The processed input is then passed to the model’s predict() method as a two-dimensional list, which is the required input structure for most machine learning models.

The model returns a predicted salary value based on the input experience. This value is extracted and displayed to the user using a formatted string. The result is shown as a simple text response on the webpage, making the interaction straightforward and user-friendly.

Finally, the application is executed using app.run(debug=True). Running the app in debug mode is helpful during development, as it enables automatic reloading and provides detailed error messages. However, this setting should be disabled in a production environment to ensure security and stability.

output of the task :


Overall, this script demonstrates a complete workflow for deploying a machine learning model as a web service. It combines backend logic, user input handling, and real-time prediction into a single application. While simple, it effectively showcases how machine learning models can be integrated into web applications to create interactive and practical tools for end users.
