# HorseKeeper 
HorseKeeper is a web application with an integrated equine cough-detection algorithm that outputs the final cough count, flags, and timestamps for the users. Coughing is one of the most significant symptoms of equine asthma. Currently, there are no easy and efficient methods to monitor cough frequency in horses, thus making diagnosis and treatment monitoring a difficult and tedious process. HorseKeeper enables researchers to easily input audio and acceleration data to receive a cough count, allowing for early diagnosis and regular monitoring of horses at risk.

HorseKeeper can be accessed [here](https://horsekeeper.herokuapp.com/)

#### Definitions:
- **Cough Count:** Any points in which the algorithm classifies a cough has occurred.
- **Flags:** Any points where a cough was detected in addition to other points of interest where the algorithm suspects there may have been a cough.
- **Timestamps:** The points in time within the datasets where a cough or flag may have occurred.

## Function
The function of HorseKeeper is best organized and described into two main components: the application and the cough detection algorithm. The application is the interface that the user interacts with, while the algorithm is what analyzes the data. The application enables the users to upload their datasets and sends the data to the algorithm to be analyzed. The algorithm then returns the cough and flag count to be displayed on the application for the user and prints the timestamps into the terminal.

### Application
The front end of the application consists of the home page, where users can upload their datasets to receive a cough and flag count with their timestamps, and a history page, where users are able to see the cough count and the date of previous cough occurrences.

The function of the home page is best described with the sequence diagram below:
![Home Page Sequence Diagram](static/images/readme_imgs/homeSequenceDiagram.png)

The function of the history page is best described with the sequence diagram below:
![History Page Sequence Diagram](static/images/readme_imgs/historySequence.png)

### Algorithm
The algorithm consists of four subsections: the MainRunner, AudioCalculator class, AccelerometerCalculator class, and AnswerGenerator class, as seen in the class diagram below:

![Algorithm Class Diagram](static/images/readme_imgs/algorithmDiagram.png)

The MainRunner is the application's direct point of access for sharing data and results. The MainRunner receives and reads the CSV data files input by the user. It then slices the entire data set into 4-second slices where each slice has a 2-second overlap with the previous slice. Doing so, enable the algorithm to determine critical features of the dataset in manageable slices.

![Visualization of Slices](static/images/readme_imgs/slices.png)

Once sliced, the AudioCalculator and AccelerometerCalculator classes are called. The calculators determine the average of local maxima, the global maximum, and the global maximum index for their respective data sets. In addition, the AccelerometerCalculator class also finds the average of local minima, the global minimum, and the global minimum index. The local maxima and minima serve as noise thresholds.

For a slice containing a cough, the global maximum represents the sound of the horse coughing. For an accelerometer data slice containing a cough, the global maximum represents the horse's head jolting forward and the global minimum represents the horse's head returning. After the necessary features and thresholds have been calculated the main runner then saves these values until each slice has gone through the calculators.

Using the previously saved values the main runner then calls the AnswerGenerator class to determine which slices contain coughs and flags. The global maximums and the global minimum are classified as possible coughs if they are above 20% of their respective noise thresholds. The following flow chart describes how the answer generator decides if a slice contains a cough or a flag.

![Visualization of Slices](static/images/readme_imgs/flowchart.png)

After the classes of the algorithm have analyzed the data, the MainRunner then collects the answers and their respective indexes. The algorithm then performs final calculations to format and output the cough count, flag number, and time stamps back to the application's user interface and the terminal.


## Specification
Following is the list of software specifications for HorseKeeper:


1. **Web Framework: Flask (Version 2.0.3)**
    
    The framework of the back-end of the application. This acts as the mediator between the front-end, database, and cough-detection algorithm.

2. ***Database: SQLite**
    
    This saves the user data between sessions.

3. **User interface: HTML5, CSS3, and JavaScript** 

    This is the front-end of the application which enables user interaction

4. **Deployment platform: Heroku free tier** 

    This is the cloud computing platform used to host HorseKeeper in the cloud

5. **Web server: Gunicorn (Version 20.1.0)**
    
    This runs multiple worker processes and manages incoming requests from clients, improving the application's performance and stability.

6. **Data modeling: SQLAlchemy (Version 1.4.46)**
    
    The toolkit that enables the application to interact with the SQLite database using Python

7. **Numerical Computing Library: NumPy (Version 1.19.5)** 
    
    The library used to manipulate the data in the algorithm

8. **Version Control: GitHub** 

    The software tool used to manage changes to source code, and documents over time.

## User Manual
Following is a step-by-step guide on how to use HorseKeeper to receive a cough count, flags, and their respective timestamps. 

Using these files, you can follow along this tutorial:


1. Select your filtered audio dataset (Note: these must be retrieved directly from the filtering algorithm and must be in the form of CSVs)
    * First click the "Choose Audio Data File" Button
    ![Choose Audio File Button](static/images/readme_imgs/selectAudioBtn.png)

    * Select your audio data file in the file explorer (Windows) or finder (Mac)
    ![Select Audio File](static/images/readme_imgs/selectAudioData.png)


2. Select your filtered acceleration dataset (Note: these must be retrieved directly from the filtering algorithm and must be in the form of CSVs)

    * First click the "Choose Acceleration Data File" Button
    ![Choose Audio File Button](static/images/readme_imgs/selectAccBtn.png)

    * Select your acceleration data file in the file explorer (Windows) or finder (Mac)
    ![Select Audio File](static/images/readme_imgs/selectAccData.png)

3. Click the 'Upload' button
![Upload Button](static/images/readme_imgs/uploadDataBtn.png)

4. Wait for the algorithm to analyze the datasets
![Loading Screen](static/images/readme_imgs/loadingScreen.png)

5. Receive final cough and flag count
![Loading Screen](static/images/readme_imgs/coughFlagCount.png)

6. Click on the 'See Timestamps' button 
![Timestamp Button](static/images/readme_imgs/timestampBtn.png)

7. See the timestamps corresponding to each cough and flag count
![Timestamps Results](static/images/readme_imgs/timestamps.png)

8. If you wish to navigate to the history page: 
    * Click the "See History" button
![History Button](static/images/readme_imgs/historyBtn.png)
    * See the previous cough count records
![History Page](static/images/readme_imgs/historyPage.png)
9. If you wish to navigate back to the home page:
    * Click the "Back" button
![Back Button](static/images/readme_imgs/backBtn.png)
    * From here you may follow Steps 1-6 to upload more datasets
![Home](static/images/readme_imgs/home.png)
    * From the home page, you may also navigate to the history page by clicking the "History" tab in the navigation bar
![Home](static/images/readme_imgs/historyNavBar.png)