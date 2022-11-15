# Homework 1 - Network elements
**Due:** Thursday, February 9, 2023 by 11:59pm
 *Read the entire assignment before starting.*

## Assignment

Write a report that contains the answers and *explains how you arrived at the answers* to the following questions. Before starting, review the [HW report guidelines](https://github.com/anwala/teaching-web-science/blob/main/fall-2022/homework/hw0/reports.md).  Name your report for this assignment `hw1_report` with the proper file extension.

(**Report (2 points**)

### Q1 (2 points)
Consider the "bow-tie" structure of the web in the Broder et al. paper ["Graph Structure in the Web"](https://web.archive.org/web/20220505225729/https://snap.stanford.edu/class/cs224w-readings/broder00bowtie.pdf) that was described in Module 1. 

Now consider the following links:

```text
A --> B
B --> C
C --> D
C --> A
C --> G
E --> F
G --> C
G --> H
I --> H
I --> K
L --> D
M --> A
M --> N
N --> D
O --> A
P --> G 
```

Draw the resulting [directed graph](https://en.wikipedia.org/wiki/Directed_graph) (either sketch on paper or use another tool) showing how the nodes are connected to each other and include an image in your report.  This does not need to fit into the bow-tie type diagram, but should look more similar to the graph on slide 24 from [Module-01 Web-Science-Architecture](https://docs.google.com/presentation/d/1sSNcXMBUJWb-rVbTEvKqFAC2SvJugI8m/edit#slide=id.p24).

For the graph, list the nodes (in alphabetical order) that are each of the following categories:
* SCC: 
* IN: 
* OUT: 
* Tendrils: 
    * indicate if the tendril is reachable from IN or can reach OUT
* Tubes: 
    * explain how the nodes serve as tubes
* Disconnected:
    
    
### Q2 (3 points)
Demonstrate that you know how to use `curl` and are familiar with the available options.

a) First, load this URI [https://httpbin.org/user-agent](https://httpbin.org/user-agent) directly in your browser and take a screenshot.  The resulting webpage should show the "User-Agent" HTTP request header that your web browser sends to the web server.

b) In a single `curl` command, issue a `HEAD` HTTP request for the URI, [https://t.co/EYgdZgrm2W](https://t.co/EYgdZgrm2W). Show the HTTP response headers, follow any redirects, and change the User-Agent HTTP request field to "DATA 440."  Show the command you issued and the result of your execution on the command line.  (Either take a screenshot of your terminal or copy/paste into a code segment.)

Briefly explain the results you get for each of these steps.

### Q3 (3 points)
Write a Python program to find links to PDFs in a webpage.

Your program must do the following:
* take the URI of a webpage as a command-line argument
* extract all the links from the page
* for each link, request the URI and use the `Content-Type` HTTP response header to determine if the link references a PDF file 
* for all links that reference a PDF file, print the original URI (found in the parent HTML page), the final URI (after any redirects), and the number of bytes in the PDF file. (Hint: `Content-Length` HTTP response header)

Here is a snippet of the expected operation:

```
% python3 get_pdfs.py https://alexandernwala.com/files/teaching/fall-2022/week-2/2018_wsdl_publications.html

URI: http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf
Final URI: https://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf
Content Length: 994,153 bytes

URI: http://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-atkins-news-similarity.pdf
Final URI: https://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-atkins-news-similarity.pdf
Content Length: 18,995,885 bytes
```

Show that the program works on 3 different URIs, one of which must be https://alexandernwala.com/files/teaching/fall-2022/week-2/2018_wsdl_publications.html, which contains 8 links to PDFs. 
* Many [W&M DS faculty members](https://www.wm.edu/as/data-science/people/index.php) have a list of their publications in PDF form on their webpages. You may search their webpages for URIs to use.
* Also, there are a set of pages linked on our [DATA 440 Syllabus](https://github.com/anwala/teaching-web-science/blob/main/fall-2022/syllabus.md) that say "pdf available".  If you follow some of those links, you'll likely find a page that links to at least one PDF.

You will likely want to use the BeautifulSoup Python library for this question. Run ``pip3 install beautifulsoup4`` to install BeautifulSoup4. I highly recommend that you install Python packages inside your [Python virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/): 
```
$ python3 -m venv p3_env     # Creates a Python 3 virtual environment in a directory called p3_env
$ source p3_env/bin/activate # Activates your Python 3 virtual environment. All new packages will be installed in py_env

$ which python               # Shows the path of your virtual env's Python
$ deactivate                 # Deactivates your Python virtual environment
```

## Submission

Make sure that you have committed and pushed your local repo to your private GitHub repo (inside the `hw1` folder).  Your repo should include your report, images, and any code you developed to answer the questions.  Include "Ready to grade @anwala" in your final commit message. 
