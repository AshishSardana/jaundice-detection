# Make-A-Thon 2017 

## Neonatal Jaundice Detection

A way to alert a mother in home about early stage of Neonatal Jaundice in order to get an early treatment to prevent newborn mortality/morbidity.

![1](https://cloud.githubusercontent.com/assets/22201681/25775004/90fb762e-32b8-11e7-9ec1-284c5aabced2.JPG)

![2](https://cloud.githubusercontent.com/assets/22201681/25775028/e50f81ce-32b8-11e7-8865-0a9d387cfaf9.JPG)![3](https://cloud.githubusercontent.com/assets/22201681/25775034/f14a9712-32b8-11e7-8ee2-ed5f4e722aaa.JPG)



### Solution:

The most reliable and non-invasive way to detect jaundice is to check the skin tone of a person.

Adopting the same technique for a new born baby, identifying the color of baby's face will help in detecting jaundice.

* CNN to classify an image for jaundice/non-jaundice. Dataset used for this were images collected from google.
* Uniform Image - Resizing the images to 28x28 px.
* Face Detection - To use the baby's face only for identifying the color of the skin. (Using Haar-Cascade and OpenCV)
* Skin Detection - To detect just the skin of the face and ignoring eyes, hair and other unnecessary features.
* Obtaining Color - Extracting color only from the skin region. (Using ColorThief)
* Classification - Comparing the color value with different shades of yellow.



1. Click the picture of the baby's face using Raspberry Pi's camera.
2. The image will be processed and the corresponding LED (Jaundice/Non-Jaundice) glows.



## Smart Medical Record Collection using Aadhar Card

A person's health is directly affected by the food he/she consume. We devised an automated solution to keep track of the calories a student intakes in a day (separate for each meal).

#### How it works?

1. Student's ID-Card will be read by the RFID after entering the 'mess'. The average calorie of that meal will be added in that student's account.
2. The calorie count is dependent on the meal (breakfast, lunch, dinner) the student is taking.
3. This information is saved in the database maintained in an Excel sheet.
4. Total calorie intake by the student will be calculated every week. If this intake is less than the minimum calorie required by a person of his/her age group, an e-mail will be sent to his/her Proctor informing them about this.





