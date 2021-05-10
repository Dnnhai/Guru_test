

This is a demo POM (Page Object Model) automation framework website using Selenium, Python, and Behave as a BDD framework. 

The goal of the framework is to be able to easily use business Gerkin language in .feature files and allow creating new steps as fast and easy as possible. 

1. Environment 
	Install Python
		--> add to environment
		
	Pycharm IDE
	
	Selenium library 
		--> set up through pip
	Behave library
		--> set up through pip 
	allure_behave
		--> set up through pip 
		
command when install throgh pip: "pip install <packege_name>"


2. Setting for new project
	Install selenium packege
		File-> New Project Setting-> setting for new projects-> python interpreter-> + -> <find "selenium">-> install 
	Install behave package
		File-> New Project Setting-> setting for new projects-> python interpreter-> + -> <find "behave">-> install 
	Install behave package
	
3. Run project

		NOTE:	3.1 please change the link to chromedriver.exe 
				3.2 please change your information at file "test_create_customer_successful_1.py"

open terminal and run this command:
	behave -f allure_behave.formatter:AllureFormatter -o Reports ./Features				<1>
after that run:
	allure serve Reports/																<2>
Incase report cannot gen: run this commnad before <2>
	npm install -g allure-commandline --save-dev										<3>


<1> for run test and export report
<2> for open report



3. http://demo.guru99.com/v4/

	id: mngr324520
	pass: Ynymeta
