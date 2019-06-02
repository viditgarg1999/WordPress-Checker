# WordPress-Checker
This Python Script will check the Username and Passwords combos and predict whether it is working or not.


# How to use?
1. First of all you need to install all the required libraries.(here i am assuming that you have Python latest version installed in your device).
Now in order to install all the libraries you need to write the following commands in the cmd window:


```
pip install selenium
```

```
pip install pandas
```

```
pip install xlwt
```
Once it is done, you can move to the step 2

2. Download the Wordpress_checker.py file and open it in python IDE (jupyter notebook, spider, IDLE...)
3. When you RUN the file it will ask for following things:
<br/>
<ul>
<li>"Enter the path of the chromiumdriver.exe File: "    (Generally it is "C:\Python(version)\Drivers\chromedriver.exe" but it may vary from python verision to version)
</li><br/>
<li>"Enter the url of the Wordpress Website admin page:"  (Give the url of wordpress admin page)
</li>
<br/>
<li>"Enter the Excel file path having Username and password combos: "  (Give the path of Excel file containing username and passwords combos)
</li><br/>
<li>"Enter number of username-password combos in the file: "          (Enter the number of Username and Passwords)
</li><br/>
</ul>
Once it is done, it will reflect some time in seconds for which you have to wait and once the time gets over then it will create a new file on the desktop with a name "Results.xlsx" with a new column having Pass or Fail value in it.

# Instruction:
The Excel file containing Username and Passwords combos, should not have any third column and the number of Username and Passwords should be same. 
<b>Also, Make sure that the excel file should have two header "Username" and "Password" otherwise it will reflect error.</b> 


# Disclaimer
This project is only for Eductional Purposes and the misuse of the information in this project can result in criminal charges brought against the persons in question. I am in no way responsible for the misuse of the information.

