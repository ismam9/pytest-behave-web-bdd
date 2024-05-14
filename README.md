> [!IMPORTANT]
> I would love for any bugs, improvements, changes, or interesting implementations to be commented on. These technologies change every day, and it's normal to catch someone being outdated. I hope it helps you! :)

# Resume

I am a Software QA Automation Engineer with experience primarily in Functional Testing for Web Browsers and Mobile Applications.

This guide is intended for beginners or junior professionals who aspire to develop a comprehensive Framework for conducting Functional Testing. There are numerous tools and frameworks available for Testing, and this guide focuses on 
those based on widely-used technologies such as Selenium and Bevahe/Gherking. It aims to assist in common QA Automation tasks, such as implementing a Testing Framework for Regression Testing, Smoke Testing, Sanity Testing, etc.

# Purpose of the Framework.
The purpose of this guide is to provide a well-structured and documented approach for building an Automated Testing Framework from scratch on **Python**. Additionally, it will include links to the official documentation of the tools we use, enabling users to familiarize themselves with the official resources. Furthermore, we will address common challenges and difficulties that may arise when following this guide. Most importantly, this guide will provide a foundational framework for users to begin implementing their test cases, regression suites, and more.

# 
### pytest-behave-web-bdd
# 

To set up and use the Testing Framework, ensure that you have the following prerequisites installed:
1. Python latest version (I am using 3.12.2)
> Remember to add to the path on the enviornment variables panel. Achieved by **checking this option on the python installation** (you will se an cheack-option). https://www.python.org/downloads/
3. Pycharm
> I recommend you to use the last version. Remember to download the Community Edition for a free account.
4. Pip
> You will see by default that a **check-option for Pip it is checked** for installing pip when you install Python. https://www.python.org/downloads/
#

### About the Framework.
We will focused this Framework on a Methology called BDD (they exists others like TDD, ATDD, etc). 

> BDD (Behavior-Driven Development)** is a software development methodology that encourages collaboration between developers, QA engineers, and business stakeholders. Can be implemented on **all Development Software & Software Development Life Cycle (SDLC).**
> 
> **On Testing** it emphasizes writing test cases in a **human-readable language** that can be understood by all parties involved in the development process. **BDD focuses on defining the behavior of a system from the end user's perspective.**
**One of the most common well known tool for archiving this is Cucumber and moreover Gherkin** because **we can write test cases in a human-readable language that can be understood by all humans.**

More specifically **Behave** allows the creation of executable specifications written in plain text using the Gherkin syntax. Gherkin is a simple, structured language that uses keywords like Feature, Background, Given, When, Then, And. But to describe the behavior of a system in a way that is understandable by non-technical stakeholders. Bevahe then translates these specifications into automated tests that can be executed by QA engineers.

Also a key thing about the Framework is that uses a design patter called POM **(Page Object Model).**

>**Page Object Model is a design pattern** (as we said) used in test automation to enhance test maintenance and readability.
>
>It involves creating separate classes for each web Page** or component of a Web Application, encapsulating the interactions with those elements within their respective classes. These page classes expose methods that represent the >actions that can be performed on the page, making the test scripts more readable and maintainable. 

So, Selenium WebDriver it is completed with POM by structuring the test code in a way that separates the page-specific actions, the page objects from the test case. This separation of concerns improves the maintainability and scalability of the test automation codebase.
##


<details>
<summary>Set-up, Tools</summary>

# Set-up
If you know anything of Python, then you you are familiarized with virual enviroments. This is a way Python help us to manage our libraries, dependencies, packages. So for each project we have, we have our packages that belongs to this projects. This is really helpfull, the idea of not having a central, generic and gigantic space where we have all the dependencies of all our projects saves us a lot of troubles. We this approach we can simple have the packages we need for the project we are building.

Setting-up our virutal enviornment (communly called venv) for our ptoject it really simple.
- If we are working with PyCharm, when we create a new project (File > New Project), we can stabilish the name of the project, the location, and use a **'Custom Interpreter'** and select **'Generate One'**, finally click on **"Create"** and we will se our **/venv directory**
- If we are not using PyCharm we have to create our /venv. For this task, **on the terminal** just go to the **project directory** and use the **command:** ´´´python -m venv c:\path\to\myenv´´´ it looks like this: ´´´python -m venv .venv´´´ (I usually set-up the enviornment as an hidden directory that why i use the '.' before the name of the venv)
- Now we just have to activate the venv. For this, if we use **the terminal** we just **move to the .venv/Scripts directoy** (we would see the activate executable) and use **the command: ´´´ activate ´´´ or ´´´ .\actiavte ´´´ or directly use ``` project-name\Scripts\activate ```**. If we are using **PyCharm** the **venv** of the project **will automatically be activated** **(you can prove this opening a terminal on PyCharm and see if there is (venv) on the command line).**

Now all the packages we download for the project will be on the /Lib directory and only can be used on this project while we have the venv activate. 

> :heavy_exclamation_mark: If you do not activate the venv of the project, **the python & pip of the terminal began from the global installation** so all the packages you download **will be downloaded globally and not be shown on the /Lib directory** of your project.


# Tools
Selenium WebDriver: This tool is employed for controlling web browsers and automating web application testing. Selenium WebDriver allows testers to interact with web elements, simulate user actions, and validate application behavior 
across different browsers. https://www.selenium.dev/documentation/webdriver/

Before proceeding, just take care that each Selenium is compatible with specific versions of web browsers. But we will not face this problem.
[Selenium on Python](https://selenium-python.readthedocs.io/))
Just type ```pip install selenium``` and you will get the latest stable version of Selenium.

Behave and Gherkin: Behave is utilized as the BDD framework, while Gherkin serves as the language for defining test scenarios in a human-readable format. Cucumber enables collaboration between technical and non-technical stakeholders 
by translating Gherkin scenarios into executable test scripts. [Behave on Python](https://behave.readthedocs.io/en/latest/)
Just type ```pip install behave``` and you will get the latest stable version of Selenium.

> :heavy_exclamation_mark: On PyCharm you should install the Gherkin Plugin for a better experience. Maybe you have already installed.


Allure Report: Allure Reports is a **tool for generating interactive and detailed test reports.** It is basicaly the most powerfull open-source reporting tool. Now a days it is been using a lot. Obviously it can be integrated with Cucumber to provide comprehensive reports with visual representations of test results, enhancing the readability and analysis of Cucumber test executions. Also, it supports the implementation with Junit5, JUnit4, TestNG, Cypress and other Testing tools.

#
### You will need these things. 
#
* Download Allure Command Line. [Allure-Commnand-Line Installation](https://allurereport.org/docs/install/). For this, I would recommend you to install it with **nodejs** which is the easiest way for install it on Windows machines.
* Just install [NodeJs](https://nodejs.org/en).
* Then you can follow this guide [Allure installation using node](https://allurereport.org/docs/install-for-nodejs/). 
* Finally and most important thing is that you **MUST** add to the enviornment variables the path of your allure-command-line installation **(usually installed on: C:\Users\ismam\AppData\Roaming\npm\node_modules\allure-commandline)** and put the \bin directory on the path **C:\Users\ismam\AppData\Roaming\npm\node_modules\allure-commandline\bin.** Now you can use the ```allure``` command on any place/directoy of your computer.
* Install Allure for Behave. Just type ```pip install allure-behave``` and you will get the latest stable version of Selenium. [Allure on Behave](https://allurereport.org/docs/behave/)

</details>

#

Now for achieving a nice project structure and nice POM (Page Object Model) design pattern, I am go to desribe how are my directories structured.
# 1. Project Structure

```
pytest-behave-web-bdd
├── .venv
├── configuration
│    ├── __init__.py               // We need __init__.py to make Python able to recognize this direcotry as a package. **THIS IS REALLY  IMPORTANT**. And be able to import this classes and methods.
│    └── config.ini                // This configuration file on .ini extension it is util for parameterized variables as URL or BROWSER.
├── features
│    ├── pages
│    │    ├── __init__.py          // We need __init__.py to make Python able to recognize this direcotry as a package. **THIS IS REALLY  IMPORTANT**. And be able to import this classes and methods.
│    │    ├── ArchiveObject.py     // Usually you get the Objects of a page inside the Page class. I decided to separate the Objects (the Archive and the Google Objects) from the all rest of pages.
│    │    └── GoogleObject.py      // Objects of all GooglePages
│    │    ├── ArchivePage.py       // ArchivePage were we found the methods used on the page we are placed
│    │    ├── GooglePage.py        // GooglePage were we found the methods used on the page we are placed
│    │    └── etc...
│    ├── __init__.py               // We need __init__.py to make Python able to recognize this direcotry as a package. **THIS IS REALLY  IMPORTANT**. And be able to import this classes and methods.
│    ├── actions.py                // Here we found the actions that selenium and the driver can take to the browser     
│    ├── enviornment.py            // Here we found the HookSteps for the before/after execution of features, steps or scenario.
│    ├── smoke.feature             // The feature where are described on Gherkin language all our TestCases/Scenarios.
│    ├── steps
│    │    ├── __init__.py          // We need __init__.py to make Python able to recognize this direcotry as a package. **THIS IS REALLY  IMPORTANT**. And be able to import this classes and methods.
│    │    ├── arhive.py            // Implementation of the steps we declared on the feature smoke.feature
│    │    └── google.py            // Implementation of the steps we declared on the feature smoke.feature
├── utils
│    │    ├── __init__.py          // We need __init__.py to make Python able to recognize this direcotry as a package. **THIS IS REALLY  IMPORTANT**. And be able to import this classes and methods.
│    │    ├── ConfigReader.py      // Helpfull class for importing the .ini config parameters (which are url and browser)
│    │    └── EmailGenerator.py    // Helpfull class actually for generating random emails.
└── ────────────

```

# 2. Features

As I was setting-up the project I realize how much important it is the directory structure for this kind of project were you use tools that uses gherkin languages (human readable language). **Gherkin have to detect where are the steps**, **the steps are who make this human-readable language (Gherkin) and traduce it through the steps to a language that it is comprehisive for the machine.**

> So as you see the /pages directory, .feature files, actions, and the enviornment files **must be** located on the /features directory, so **behave** can the associate the features with the steps.

What i recommend is:
* **To create** your feature.feature file **first**. 
* Then you can run the command: ``` behave -k features ```.
> This command shows you **if the steps that are implemented on the feature** can be found by Behave on any directory. **Not only tells you which steps are not implemented it also provides the methods and implementations of the steps we found on the features.**

* Also we can use something like this ```behave features/smoke.feature``` to select the execution of an specific feature
* Finally we can use the **tags**. Just put  **@some-tag** on the definition of a scenario or for the complete feature as this:
```
@all
Feature: Archive Tabs Funcionality
```
or 
```
@test1
  Scenario: Comprobación de pagina de inicio y tabs de navegación
```
Then you should be able to type de command: ```behave features --tags=all``` or ```behave features --tags=test1``` for target the scenario or feature you want.
#

:large_blue_circle: Something important to remark is that Behave have some key words. 

:large_blue_circle: We use for exmaple the key 'step_' to define funcitions to tell Behave this is a step definition. We can see in our code as def ```def step_impl(context):```. 

:large_blue_circle: A part from this we have the funcion names **before_scenario, after_scenario or after_step,** this is commonly used for setting up the driver after each scenario execution and setting-up the close of the browser. On my enviornment.py class we found this:

```
def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))
```


# 3. Run

So yo have seen some of the commands **for execute the features or for execute some specific scenario tagged** by his tag (really usefull if we are develpment the scenarios and not want to execute the complete feature)

As we have seen how to download Allure :white_circle:**(allure-command-line with nodejs)** and install the package for behave :white_circle:**(pip install allure-behave)**. 
> :information_source: We now want to execute the features as we have seen. And setup the report with the data results of the execution.

Achive this is really simple if had already :white_circle: allure-command-line globally installed and :white_circle: behave-allure package installed on the venv of our project.

:yellow_circle: ```behave -f allure_behave.formatter.AllureFormatter -o Reports/ features``` THIS ONE EXECUTE ALL THE FEATURES AND SAVE ALL THE DATA AND RESOURCES (NEDEED FOR ALLURE) ON THE ALLURE REPORTS DIRECTORY THAT CREATES.

:yellow_circle: ```allure serve Reports ``` THIS ONE SHOULD BE LAUNCH WHEN WE KNOW THE RESOUCER AND DATA ARE READY ON THE /Resource DIRECTORY. ALLURE WITH COMMAND CREATE A SERVER AND OPEN IN THE BROWSER THE REPORT ON AN SPECIFIC URL AND PORT

:yellow_circle: ```allure generate --single-file --clean Reports``` THIS IS THE MOST USEFULL BECAUSE IT GENERATE THE REPORT AND EMBEDED AS IT WERE A single-file-html TYPE REPORT SO YOU NOT HAVE TO LAUNCH ```allure serve``` TO LAUNCHE THE ALLURE SERVER. INSTEAD CREATES A single-file-html THAT YOU CAN SEND VIA EMAIL OR MOVE WHERE YOU WANT.

:yellow_circle: The ```--clean``` parameter it is used when the /Report directory already have some data and you want to cleared for the new report.


# TO DO
- [ ] Make the project get the Bahave.ini and not use the global configuration of Behave.ini.
- [ ] Finish the Test Cases / Scenarios that are uncompleted or unfinished.
- [ ] Make a better solution for shadow-elements. Make it work for all actions of the browser.
- [ ] Parametize for being able to select the platform: Unix, Windows, Mac, Android, iOS.
- [ ] Parametize for being able to select type of report: allure or other one
- [ ] Parametize for being able to select if we want to send email or no with the report
- [ ]  Parametize for being able to select parallel testing or not.
