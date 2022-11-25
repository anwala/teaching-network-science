# Homework 5 - Network Models
**Due:** Thursday, April 13, 2023 by 11:59pm
 *Read the entire assignment before starting.*

## Assignment

Write a report that contains the answers and *explains how you arrived at the answers* to the following questions. Before starting, you are encouraged to review the [Chapter 5 Python Google Colab notebook](https://github.com/anwala/teaching-network-science/blob/main/spring-2023/week-10/data_340_02_s23_chp_05_network_models.ipynb). Name your report for this assignment `hw5_report` with the proper file extension.

(**Google Colab Report (2 points**)

### Q (2 points x 4)

* Build a random network with 1000 nodes and p = 0.002. Plot its degree distribution. (Hint: We show how to plot a distribution in the [Chapter 3 Tutorial](https://github.com/anwala/teaching-network-science/blob/main/spring-2023/week-4/data_340_02_s23_chp_03_hubs.ipynb).) Answer the following questions:
* What is the largest degree of the network? and What is the *mode* of the distribution (i.e. the most common value of the degree)?
* Is the network connected? If not, how many nodes are in the giant component?
* What is the average clustering coefficient? Compare it with the link probability *p*
* What is the network diameter?

### Extra-credit (2 point)

* Build Watts–Strogatz networks with 1000 nodes, k=4, and these values for the rewiring probability: p=0.0001, 0.001, 0.01, 0.1, 1. Compute and compare their degree distributions, by plotting them in the same diagram.

## Submission

Make sure that you have committed and pushed your local repo to your private GitHub repo (inside the `hw5` folder).  Your repo should include your report, images, and any code you developed to answer the questions.  Include "Ready to grade @anwala" in your final commit message. 
