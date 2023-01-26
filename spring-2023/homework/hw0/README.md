# Homework 0 - Writing HW Reports
**Due:** Thursday, February 2, 2023 by 11:59pm
*Read the entire assignment before starting.*

## Assignment

Unless otherwise stated, for each HW assignment, you are required to write a report. Reports are not just a list of questions and answers, but *must* include descriptions, screenshots, copy-paste of code output, references, as necessary. For each question you address, you must provide a discussion of how you answered the question.  

You may use existing code, but you **must** document and reference where you adapted the code -- give credit where credit is due! *Use without attribution is plagiarism!*  **All reports must have a section labeled "References" for listing the outside resources you consulted.**

Each report may be written in [Google Collab notebooks](#google-collab-notebooks), [Markdown](#markdown), or [LaTeX](#latex). Assignments may include instructions on what tool to use otherwise you may use any. For an example of what I'm expecting, you can look at a [previous student's LaTeX report](https://github.com/anwala/teaching-web-science/blob/main/fall-2022/homework/hw0/report_exemplar.pdf). Assignments must be submitted on Github.

For this assignment you have 2 tasks outlined by Q1 and Q2.

## Formatting Requirements

All reports must include your name, class (DATA 340-02), assignment number/title, and dates. You do not need a title page.

You *may* complete your reports in Google Collab or Markdown or LaTeX. Ensure all images, code, datasets, etc. referenced in the report are  included in your GitHub repo. Consider modifying and using these templates:

* [Google collab notebook template](https://github.com/anwala/teaching-network-science/blob/main/spring-2023/week-1/data_340_02_report_template.ipynb)

* [Markdown report template](https://github.com/anwala/teaching-web-science/blob/main/fall-2022/homework/hw0/data440_report_template.md)
To write your reports using LaTeX to generate to a PDF file,

* I've provided a [LaTeX report template in Overleaf](https://www.overleaf.com/read/vrfznvpgyrjc).  You can view the PDF that's generated there as well.
  * You should sign up for a free [Overleaf](https://overleaf.com) account.

* When you include images in your reports, *do not change its [aspect ratio](https://en.wikipedia.org/wiki/Aspect_ratio_(image))*.

* If you use LaTeX, you must include your .tex source file and any images used along with your .pdf report in your GitHub repo.  There are a couple different ways to do this.
  * Download the source files from Overleaf and upload to your GitHub repo.  See [Downloading a Project](https://www.overleaf.com/learn/how-to/Downloading_a_Project) for instructions on how to download a .zip file of your Overleaf project source files.  You should unzip this file locally and only upload the .tex, .pdf, and image files needed for your report to your GitHub repo.  Do not directly upload the .zip file to GitHub.
  
When you are asked to include a graph/chart in your report, they must be generated in R or using a Python plotting library.  *Excel graphs are not acceptable.* Although scientific graphs can be created in Excel, I want you to become familiar with common data science tools.

## Q1 (3 points): Create private Github repo

Create a private Github repo for the class and the folders for each assignment. E.g., `hw0`, `hw1`, etc:
```bash
data-340-02/
├── README.md
├── hw0
├── hw1
├── hw2
├── hw3
├── hw4
├── group-project
```
This is where you'd submit all your assignments. Since this is a private Github repo, only you and your collaborators will have access. Please add me as a collaborator:```Settings > Collaborators > Add people > type "anwala" > Press select a collaborator above```.

## Q2 (7 points): Write a sample report with Google collab or Markdown or LaTeX

### Google collab notebook

1. From the `hw0` folder of your private GitHub assignment repo, create a new Python notebook file (`hw0_report.ipynb`) by editing the content of [data_340_02_report_template.ipynb](https://github.com/anwala/teaching-network-science/blob/main/spring-2023/week-1/data_340_02_report_template.ipynb). 

2. Modify the content to include your name, class (DATA 340-02), assignment number/title, and dates for this exercise.

3. Upload an image to your GitHub repo and include it in place of the "Growth of the Early Web" image. Make sure to change the description of the image in the report, too.

4. Replace the code in the fenced code block with any other block of code.  You can use some Python code, or you can insert code from a different language -- just change the language indicated so that syntax highlighting still works properly.

5. Edit the first table so that it matches the first 4 weeks of our class schedule, as given in our [syllabus](https://github.com/anwala/teaching-network-science/blob/main/spring-2023/syllabus.md#summary-schedule).

6. In the References section, replace the placeholder references with three webpages that you've visited so far this semester related to the class. These should include both the title of the webpage/article and the URL.

7. Finally, make sure that your `hw0` folder in your GitHub assignments repo contains the final version of your edited report file (`hw0_report.ipynb`) and your included image.  In your final commit, use the commit message `@anwala ready to grade`.

### Markdown

1. From the `hw0` folder of your private GitHub assignment repo, create a new Markdown file named `hw0_report.md` and copy the content from [data440_report_template.md](https://github.com/anwala/teaching-web-science/blob/main/fall-2022/homework/hw0/data440_report_template.md) into it. 

2. Modify the content to include your name, class (DATA 340-02), assignment number/title, and dates for this exercise.

3. Upload an image to your GitHub repo and include it in place of the "Growth of the Early Web" image. Make sure to change the description of the image in the report, too.

4. Replace the code in the fenced code block with any other block of code.  You can use some Python code, or you can insert code from a different language -- just change the language indicated so that syntax highlighting still works properly.

5. Edit the first table so that it matches the first 4 weeks of our class schedule, as given in our [syllabus](https://github.com/anwala/teaching-network-science/blob/main/spring-2023/syllabus.md#summary-schedule).

6. In the References section, replace the placeholder references with three webpages that you've visited so far this semester related to the class. These should include both the title of the webpage/article and the URL.

7. Finally, make sure that your `hw0` folder in your GitHub assignments repo contains the final version of your edited report file (`hw0_report.md`) and your included image.  In your final commit, use the commit message `@anwala ready to grade`.

### LaTeX

Reports may be written in LaTeX and compiled into a PDF document. [Overleaf](https://overleaf.com) provides an online setup for writing and compiling LaTeX into PDF.  You will need to sign up for a free [Overleaf](https://overleaf.com) account. Alternatively, you may run LaTeX locally to generate your PDF.

1. Use the "[DATA440 - report template](https://www.overleaf.com/read/vrfznvpgyrjc)". Rename your folder containing your LaTeX files to `report`. It should contain a `report.tex` and `report.pdf`. All these should be placed inside the `hw0` folder of your private GitHub assignment repo. 

2. Modify the report to include your name, class (DATA 440), assignment number/title, and dates for this exercise.

3. Replace the "Growth of the Early Web" image. Make sure to change the image caption and description of the image in the report, too.

4. Replace the code in the `lstlisting` environment with another block of code.  You can use some Python code, or you can insert code from a different language -- just change the language indicated so that syntax highlighting still works properly.  Make sure to change the caption as needed.

5. Edit Table 1 so that it matches the first 4 weeks of our class schedule, as given in our [syllabus](https://github.com/anwala/teaching-network-science/blob/main/spring-2023/syllabus.md#summary-schedule).

6. In the References section, replace the placeholder references with three webpages that you've visited so far this semester related to the class. These should include both the title of the webpage/article and the URL.

7. Finally, make sure that your `hw0` folder in your GitHub assignments repo contains the PDF and all necessary files required to generate your PDF (e.g., `report.tex` and images). In your final commit, use the commit message `@anwala ready to grade`

## Submitting Reports

Solutions for an assignment must be uploaded into its [respective assignment folder in your private Github repo](#create-private-github-repo). Before you submit your assignment, ensure to include all scripts, code, output files, and images needed to complete the assignment and your report.