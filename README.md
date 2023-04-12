# HorseKeeper 
HorseKeeper is a web application with an integrated equine cough-detection algorithm that outputs the final cough count, flags, and timestamps for the users. Coughing is one of the most significant symptoms of equine asthma. Currently, there are no easy and efficient methods to monitor cough frequency in horses, thus making diagnosis and treatment monitoring a difficult and tedious process. HorseKeeper enables researchers to easily input audio and acceleration data to receive a cough count, allowing for early diagnosis and regular monitoring of horses at risk.

#### Definitions:
- **Cough Count:** Any points in which the algorithm classifies a cough has occurred.
- **Flags:** Any points where a cough was detected in addition to other points of interest where the algorithm suspects there may have been a cough.
- **Timestamps:** The points in time within the datasets where a cough or flag may have occurred.

## Function
HorseKeeper worked by 

## Specification


## User Manual
Following is a step-by-step guide on how to use HorseKeeper to recieve a cough count, flags, and their respective timestamps. 

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