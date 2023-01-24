# Network Science (DATA 340-02) Group Project Description - Building real-world applications
**Due:** May 15, 2023

*Read this group project description before the [group project task](group-project-topic-01/)*

## Introduction

The goals of this group project include fostering and assessing your problem-solving, collaboration, time management, and communication skills. These skills are essential for success in building real-world applications.

This project is designed for groups of **four** members, responsible for executing four of five subtasks of the project: *Data extraction/cleaning*, *Network generation*, *Visualization*, and *Analyses*. All members must be involved in the last component *Final report/Presentation*. All team members must work together by division of labor. Even though each member is responsible for a subtask (e.g., *Data extraction*), you are encouraged to help one another and track the collective progress of your group. I will also permit groups of **two** members for those willing to accomplish multiple subtasks.

A maximum of **12 individual-points** will be awarded to individuals responsible for the four subtasks of the group project. A maximum of **8 group-points** will be awarded to all members of the group for the final report and presentation, and **2 extra-credit points** reserved to reward excellence. This means, you can obtain a maximum score of 20/20 or 22/20 for this project. See [Project subtasks and point system](#project-subtasks-and-point-system) for more details. 

All groups must select a group name and nominate a single member as its leader to supervise and ensure the success of the entire project. Even though there is division of labor and dependency, members must submit individual reports that explain their progress in accomplishing their subtask. For example, consider a group (called *Tribe*) consisting of four members:
|Name |Team Role|Subtask|
|---|---|---|
|Liz    |Team leader| Data extraction        
|Li     |Member     | Network generation       
|Mohamed|Member     | Visualization          
|Udo |Member     | Analyses               
|Liz, Li, Mohamed, & Udo| Team | Presentation 

In this scenario, a single member, say Liz, would submit four milestone reports explaining how she worked to accomplish the *Data extraction* subtask or any additional subtask --- in the event that she completed her subtask early and took on additional roles. 

In summary, subtasks are the problems group members must solve as individuals (e.g., *Data extraction*) while milestone reports communicate progress, challenges, plans, etc. in accomplishing the goals of subtask. I expect **four** individual reports chronicling progress updates (see [Submission/Deliverables (due dates)](#submission-deliverables-due-dates).

Individual report must include the team member's name, group name, the subtask's goals and objectives, and *explanations of how each milestone of the subtask was accomplished*. Individual reports should be named `gp_groupname_milestone_number` (e.g., `gp_tribe_milestone_1.md`) and uploaded into the `group-project` folder on your Github repo.

The final report `gp_groupname_final_report` must be written by all team members, should include their names and subtask roles, and submitted on the Github repo of the team leader. A final presentation must be given to the entire class on the date of the final exam, May 15, 2023 at 2pm ET.

## Group formation and task division

Students are expected to form groups of four (or two) members and submit the membership details (role of members) to me by **February 21, 2023**. I encourage you to maximize the diversity of expertise by forming groups that feature different majors (e.g., CS/DS, Biology, Business). I reserve the right to assign students to existing groups for those without groups.

Each group is responsible for selecting a group leader and assigning subtasks to members. Even though there is dependency, I strongly encourage group members to work in parallel but help one another. This is possible even in the absence of real data and can be accomplished if the expected input/output of subtasks are known ahead of time. For example, the data extraction leader could create "fake data" or a small sample of the data in a JSON format that mimics the actual data. The network generation leader could use this to begin modeling the problem as a graph. Similarly, the Visualization leader could use the same data to begin creating network visualizations and the Analyses leader could start implementing extraction of useful metrics across all subtasks.

## Project subtasks and point system

The following are the subtasks for the group project.

#### SUBTASK 1, Data extraction/cleaning (max 12 points):
This subtask involves extracting the data - the raw material needed to address the project goals. This could also involve cleanup/transformation of the data, deciding what to collect (sample) and what to exclude (ensure to include in report) and saving the data into a machine-readable format (e.g., JSON, CSV).

##### Grading rubric
* Complete network dataset was downloaded
* Dataset includes fields pertinent to address research questions
* Dataset is human/machine-readable and well-organized
* Data extraction was implemented in documented (comments and ReadMes) Python scripts (not Notebooks). Code for generating dataset is modular (uses separate files/functions) and reusable (no hard-coding). 
* Report includes problem summary/questions, code snippets, and is clearly written: well-organized and includes few typos/grammatical errors

#### SUBTASK 2, Network generation (max 12 points):
This subtask requires transforming the data into a network model involving nodes and links to model relationships. This includes deciding what relationships to model and how (e.g., (un)directed vs. (un)weighted) to represent them.

##### Grading rubric
* Network model is capable of addressing research questions
* Reasonable justifications are provided for network generation decisions
* Network generation was implemented in documented (comments and ReadMes) Python scripts (not Notebooks). Code is modular (uses separate files/functions) and reusable (no hard-coding). 
* Report includes problem summary/questions, code snippets, and is clearly written: well-organized and includes few typos/grammatical errors

#### SUBTASK 3, Visualization (max 12 points):
This subtask involves implementing a network visualization with Gephi, Networkx, D3 or another instructor-approved tool to visualize the project network. This involves deciding the best way to visualize the network. For example, deciding the network layout (e.g., force-directed vs. circular), color scheme (e.g., color-blind friendly), and what attributes to map to channel (e.g., size, position).

##### Grading rubric
* Network visualization is legible and helps explore/understand various network phenomena
* Network visualization was implemented in documented (comments and ReadMes) Python scripts (not Notebooks). Code is modular (uses separate files/functions) and reusable (no hard-coding). 
* Report includes problem summary/questions, code snippets, and is clearly written: well-organized and includes few typos/grammatical errors

#### SUBTASK 4, Analysis (max 12 points):
This subtask involves generating statistics to understand the data and identify useful insights. It could involve presenting relevant summary statistics of the dataset. Additionally, summarizing membership of nodes and links and identifying various network phenomena (e.g., hubs, small worlds) and emphasizing important characteristics (e.g., heterogeneous distribution of node/link properties) of the network.

##### Grading rubric
* Analyses was provided to understand the composition of dataset
* Analyses was provided to address relevant research questions
* Analysis is sound and code provided for computing metrics. Documented (comments and Readmes) Python scripts (not Notebooks) were used. Code is modular (uses separate files/functions) and reusable (no hard-coding). 
* Report includes problem summary/questions, code snippets, and is clearly written: well-organized and includes few typos/grammatical errors

#### SUBTASK 5, Final report/Presentation (max 8 points assigned to all members):
A single report that summarizes all effort taken to accomplish the group tasks. It must present/introduce the problem and have sections that document how each subtask was accomplished to address the project research questions.

##### Grading rubric

* Report includes project topic summary and research questions. 
* Report addresses research questions.
* Report is well-organized and includes few typos/grammatical errors
* Report includes code snippets, and Github repo includes all code, data, and resources used in project.
* Repo Python scripts (not Notebooks) are well-documented (have comments and ReadMes). Code is modular (uses separate files/functions) and reusable (no hard-coding). 
* Presentation slides are well-organized and include images and code snippets to assist illustration and explanations.
* Presenters effectively communicated their solution to class

## Submission/Deliverables (due dates)

#### Four individual reports:
Make sure to commit and push your local repo to your private GitHub repo (inside the `group-project` folder).  Your repo should include your report, images, and any code you developed in the course of accomplishing your subtask. Include "Ready to review @anwala" in your final commit message. Here are submission deadlines for the reports:
* Milestone report 1/5 due Apr 13
* Milestone report 2/5 due Apr 20
* Milestone report 3/5 due Apr 27
* Milestone report 4/5 due May 4

#### One final reports:
The final report must be written by all group members and submitted on the date of the final exam May 15, 2023 at 2pm ET.