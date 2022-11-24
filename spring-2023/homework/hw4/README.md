# Homework 4 - Directions and Weights
**Due:** Thursday, April 6, 2023 by 11:59pm
 *Read the entire assignment before starting.*

## Assignment

Write a report that contains the answers and *explains how you arrived at the answers* to the following questions. Before starting, you are encouraged to review the [Chapter 4 Python Google Colab notebook](https://github.com/anwala/teaching-network-science/blob/main/spring-2023/week-8/data_340_02_s23_chp_04_directions_and_weights.ipynb). Name your report for this assignment `hw4_report` with the proper file extension.

Download [`repealthe19th.jsonl.gz`](https://github.com/CambridgeUniversityPress/FirstCourseNetworkScience/raw/master/datasets/repealthe19th.jsonl.gz) to answer the following questions.

Build the retweet network for `#RepealThe19th`, a controversial hashtag used during the 2016 US presidential campaign to advocate for the repeal of the 19th amendment to the US Constitution, which grants women the right to vote. 

`repealthe19th.jsonl.gz` includes 23,343 tweets containing the hashtag. Each line is a tweet JSON object. After parsing the file, you should verify that you have this many tweets; a deviation from this number would flag parsing errors that may affect your answers. 

Keep the following in mind. (i) Link direction follows information flow: if Alice retweets Bob, there is a link from Bob to Alice. (ii) Remove self-loops; you can do so after creating the network, or modify your network creation code to not add them at all. This will definitely affect some answers.

(**Google Colab Report (2 points**)

### Q1 (2 points)

Draw the `#RepealThe19th` retweet network. Ensure the graph is legible and pretty:
* Edge crossings are minimized

### Q2 (1 point x 6)

* How many nodes are in the retweet network?
* How many links are in the retweet network?
* What is the screen name of the node with highest out-strength in the network? What is its out-strength?
* What is the screen name of the node with the second-highest out-strength in the network?
* What is the screen name of the node with highest in-strength in the network? What is its in-strength?
* Describe what the out-strength and in-strength values of these accounts tell you about their online behavior.

### Extra-credit (1 point)

* How many nodes are in this network’s largest weakly connected component?

## Submission

Make sure that you have committed and pushed your local repo to your private GitHub repo (inside the `hw4` folder).  Your repo should include your report, images, and any code you developed to answer the questions.  Include "Ready to grade @anwala" in your final commit message. 
