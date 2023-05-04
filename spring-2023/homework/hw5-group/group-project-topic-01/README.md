# Network Science (DATA 340-02) Final Project Task
*Read the [group project description](/spring-2023/homework/hw5-group/) before this group project task*

> Mapping Collaboration Networks in Film and TV Production (building a film/TV director-crew network). (This project was designed jointly by Dr. Alexander C. Nwala (Instructor) and [Dr. Arthur Knight](https://www.wm.edu/as/english/facultystaff/knight_a.php), Associate Professor, American Studies and English at W&M)

## Introduction

Some renowned film directors are known to work persistently with the same key collaborators. For example, [Wes Anderson](https://en.wikipedia.org/wiki/Wes_Anderson) employed the same movie score composer, [Alexandre Desplat](https://en.wikipedia.org/wiki/Alexandre_Desplat) for multiple movies, including, [The French Dispatch](https://www.imdb.com/title/tt8847712/?ref_=nm_flmg_c_10_com) [Isle of dogs](https://www.imdb.com/title/tt5104604/?ref_=ttfc_fc_tt) and [The Grand Budapest Hotel](https://www.imdb.com/title/tt2278388/?ref_=ttfc_fc_tt). 

Shifting ground to questions of access and representation: Some directors hire collaborators from groups that were historically prevented from working in the
mainstream U.S. film industry --- e.g., African Americans, women. Among the
reasons given by such directors is that this opens opportunities and diversifies the U.S. film
industry creative labor pool and, thus, expands the perspectives represented in and
benefiting from U.S. movies and TV.

Create a network that explores these phenomena from the following [list of directors](#list-of-directors).

## Research Questions

* How widespread is the phenomenon of directors re-using the same crew? Do renowned directors (and women/minority directors) tend to work persistently with the same key collaborators and less recognized directors tend to work with shifting groups of collaborators? 
* How will you characterize the film-director network? What are the properties (Average shortest path length, triangles aka clustering coefficient, density/sparcity)? 
* Did you find any interesting nodes/links?

## List of directors

The [following list of directors](100_film_directors.csv) consists the `LastName`, `FirstName`, `Sex`, `Ethnicity_Race` (A=Asian, Asian American (incl India), B=Black, I=Indigenous (Native American, Maori), L=Latin American, W=White), `Labels` (H=top 25 highest grossing directors (excluding animation directors) and Q=identifies as LGBTQ"), and `IMDb_URI`s of 101 directors.

## Data extraction

Using the [list of directors](#list-of-directors) as a starting point, extract their IMDb URIs (e.g., [Wes Anderson](https://www.imdb.com/name/nm0027572/)).

Next, scrape all the IMBb links of the movies (e.g., [https://www.imdb.com/title/tt5104604/](https://www.imdb.com/title/tt5104604/)) from the `Director` section of the Credits pages of the directors in your dataset (e.g., [https://www.imdb.com/name/nm0027572/fullcredits/](https://www.imdb.com/name/nm0027572/fullcredits/))

Next, scrape the crew members (exclude Cast since the focus is not on actors/actresses) from the full credits pages (e.g., [https://www.imdb.com/title/tt5104604/fullcredits/](https://www.imdb.com/title/tt5104604/fullcredits/)) of all movies in your dataset: `Writing Credits`, `Produced by`, `Music by`, `Cinematography by`, etc.

Consider storing the data hierarchically (organized by last names of directors), e.g., 
```
film-directors/
├── a
│   └── wes-anderson
│       └── movies.jsonl
├── b
│   └── luc-besson
│       └── movies.jsonl
...
├── x
├── y
└── z
```
OR (organized by IMBb page identifiers), e.g.,
```
film-directors/
├── nm0000108
└── nm0027572
```
Consider storing movie details in a module form in a JSONL file, e.g.,
```
$ more film-directors/A/wes-anderson/movies.jsonl
{"movie_title": "Isle of Dogs", "music_by": ["Alexandre Desplat"], "directed_by": ["nm0000108"], "gender": "male", "ethnicity": "W"}
{"movie_title": "The Grand Budapest Hotel", "music_by": ["Alexandre Desplat"], "directed_by": ["nm0000108"], "gender": "male", "ethnicity": "W"}
```

Discard all non-feature films from your dataset. Use `imdb_scraper.py.is_feature_film()` (or `imdb_scraper.py.is_feature_film_v2()` on the occasion that `is_feature_film()` fails) to test for feature films (i.e. Films at least 70 minutes long, shown in a cinema for a paying audience; or promoted similarly for TV or streaming).

### Scraping code

I have provided [`imdb_scraper.py`](imdb_scraper.py) to facilitate scraping 
* Movie URIs from the `Director` section of the Credits pages, for example, `dir_cred = get_full_credits_for_director('nm0027572')`.
* Full crew information from the full credits pages of movies, for example, `full_credits = get_full_crew_for_movie('tt2278388')`.

## Network generation

Generate a network that permits the exploration of the film director-crew relationships and address the research questions. Use the entire toolkit from this networks course to accomplish this task and justify/explain decisions for encoding nodes, links, directions, weights, etc.

## Visualization

Implement a network visualization that enables visualizing (a subset) of the film director-crew network and addresses the research questions. You may use a combination of Networkx, Gephi, [D3](https://d3js.org/), or any instructor-approved tool to build your network visualizations.

## Analyses

Provide useful summary statistics to understand the composition of the evaluation dataset. For example, for individual directors and across the dataset, provide the number of directors and the number of movies they have directed, types/counts of crews. Next, informed by the knowledge gained during this course, provide useful network statistic that address the research questions and identify important network phenomena, e.g., important nodes (hubs), short paths, triangles, etc.