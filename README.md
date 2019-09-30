# BloodBankManagementWithBarcodeAndBiometric

# Section 1-Introduction: 
This module will provide a solution to a very important aspect of Hospital Management which is Blood Bank Management. Database Systems can be efficiently and properly utilized to solve this problem. This module is responsible for storing, maintaining and retrieving of useful information. Moreover, it will take some advanced sub modules into working as well, which are Barcode scanning and biometric scanning. These sub modules would increase ease and at the same time enhance security.

# Section 2-Working: 
This module is based on the following sub modules which contribute to its working:
1.	The back end linking all the submodules together
2.	A Database System responsible for storing and retrieving information when required
3.	GUI which allows features to be accessed in a visual manner
4.	Barcode Scanner that can scan and process Bar Codes 
5.	A Biometric Scanner used to provide access based on matching fingerprints

The overall working is demonstrated by this flowchart:

![](images/bb_flowchart.jpeg)
 
The Database System working is as follows:



GUI module works according to this flow chart:







	








The Barcode Scanner Module works according to this:


  

 















The Biometric Scanner Module works according to the following flowchart

Pubic database is firstly design that can store the fingerprint of all patients and must be capable to add new one. Fingerprints store in database pass through these steps:

  









Critical points are then act as a primary key for the database and further data is stored in the database according to the schema.

COMPARISION:
For comparison, again input is taken from the user again these steps are implemented:


  

 














# Section 3-Roles: 
These are the rules that will benefit from this module:

Admin:  He have full rights of the system/database. He creates doctor, nurse, patients and other users. He can issue notices and manage complete hospital operations. 

Patient: Read data from the database about patient general information, their medication history and recommended doctors.
Doctor: Database store Doctor’s general information, Numbers of patients deal, their timing, experience, specialty, patient response. 

Nurse: Nurse will manage the patient data. She can allocate bed to the patient and monitor the patient conditions. She can also manage blood bank.

Pharmacist: He will manage the complete stock of medicine. He will add medicine with price and supplier details. He can view patient description and manage medicine categories.

Accountant: He will manage invoices in the database. He will keep record of the hospital’s income and expenses of the hospital.
Laboratorist/Pathologist: He will manage the lab reports for each patient and manage blood bank. 



