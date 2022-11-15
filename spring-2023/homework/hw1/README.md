# Homework 1 - Network elements
**Due:** Thursday, February 9, 2023 by 11:59pm
 *Read the entire assignment before starting.*

## Assignment

Write a report that contains the answers and *explains how you arrived at the answers* to the following questions. Before starting, review the [HW report guidelines](https://github.com/anwala/teaching-network-science/blob/main/spring-2023/homework/hw0/README.md).  Name your report for this assignment `hw1_report` with the proper file extension.

(**Report (2 points**)

### Q1 (3 points)

Go through the [tutorial on Network elements](https://github.com/anwala/teaching-network-science/blob/main/spring-2023/week-2/data_340_02_s23_mod_02_network_elements.ipynb).

Now implement functions for Exercises 1 -- 3    
    
### Q2 (2 points)

Consider this adjacency matrix.

<img src="adj_mat.png" alt="Ajacency matrix for hw1 Q2" height="200"><br/>

An entry in the *i*th row and *j*th column indicates the weight of the link from node i to node j. For instance, the entry in the second row and third column is 2, meaning the weight of the link from node **B** to node **C** is 2. What kind of network does this matrix represent?

**a.** Undirected, unweighted

**b.** Undirected, weighted

**c.** Directed, unweighted

**d.** Directed, weighted

Why?

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
