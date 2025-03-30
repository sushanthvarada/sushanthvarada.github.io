AFTER Running the Python script --> Copy "About.html" --> Rename it to "index.html"

SEARCH ENGINES INDEXING - Delete the following from About.html and index.html
[Automated through python script]
1) search for <meta name="robots" content="noindex">
2) Remove it from the html files

CSS - Fonts & Scrollings effects (UPDATE About.html and then COPY to CREATE index.html)
[Automated this CSS file link addition via Python script: "replace-href_add-css.py"] 
1) Add the code snippet "<link rel="stylesheet" href="global-styles.css">" just before <\head> in About/index.html
2) Add "html {scroll-behaviour: smooth}" and relevant @font-face{<code>} to global-styles.css file 
2) Make sure to upload the global-styles.css file (within this folder) to the GitHub repository

NAVBAR - Replace googlesites section links with HTML section_ids for same-page navigation without refreshing the page:
HTML File Section IDs
1) About Section ID: #h.46484830237903f6_31
2) News Section ID: #h.65707dc883f98522_53
3) Archived News Section ID: #h.4258b6f0a078c348_3
4) Publications Section ID: #h.3241f61572ff7070_3
5) Research (a) Superconducting Phase Crystal Section ID: #h.72da52c0c87c277_46
6) Research Divider 1 Section ID: #h.7b2b0d2a64a075bc_65
7) Research (b) Laughlin Anyons Section ID: #h.7b2b0d2a64a075bc_37
#Purged 8) Research Divider 2 Section ID: #h.7b2b0d2a64a075bc_17
#Purged 9) Research (c) Viterbi Decoders Section ID: #h.7b2b0d2a64a075bc_11
10) Education heading Section ID: #h.7b2b0d2a64a075bc_95
11) Education Uppsala Section ID: #h.7b2b0d2a64a075bc_147
12) Education Chalmers Section ID: #h.2112a6e7406b8374_0
13) Education KUL Section ID: #h.7b2b0d2a64a075bc_151
14) Experience heading Section ID: #h.ac1910601f7f19a_3
15) Experience imec Section ID: #h.ac1910601f7f19a_4
16) Experience Deloitte Section ID: #h.ac1910601f7f19a_14
17) Contact Section ID: #h.65707dc883f98522_84 
18) Footer Section ID: #h.7b2b0d2a64a075bc_29 

Google Sites Links
1) a) SV Mobius ring icon: About.html
   b) Sushanth Varada | Doctoral Researcher title: About.html
   c) About Navbar button: About.html

2) Publications Navbar button - https://www.google.com/url?q=https%3A%2F%2Fsites.google.com%2Fview%2Fsushanthvarada%2Fabout%23h.wac2zk2z9r5i&amp;sa=D&amp;sntz=1&amp;usg=AOvVaw0EJMxFKbOj2TFI-XsI4L4B

3) Research Navbar button - https://www.google.com/url?q=https%3A%2F%2Fsites.google.com%2Fview%2Fsushanthvarada%2Fabout%23h.t5dzel4hfwk9&amp;sa=D&amp;sntz=1&amp;usg=AOvVaw31nwu5fpZ2kpfKBcrrjwWr

4) Education Navbar button - https://www.google.com/url?q=https%3A%2F%2Fsites.google.com%2Fview%2Fsushanthvarada%2Fabout%23h.rl9tbx1e53v5&amp;sa=D&amp;sntz=1&amp;usg=AOvVaw1pfszewwnFn5sCu1lmA6pA

5) Experience Navbar button - https://www.google.com/url?q=https%3A%2F%2Fsites.google.com%2Fview%2Fsushanthvarada%2Fabout%23h.dgu5f2a7ah10&amp;sa=D&amp;sntz=1&amp;usg=AOvVaw2EG_MPWVALCO9guXvp8REX

6) Contact Navbar button: https://www.google.com/url?q=https%3A%2F%2Fsites.google.com%2Fview%2Fsushanthvarada%2Fabout%23h.2anh11c2z94e&amp;sa=D&amp;sntz=1&amp;usg=AOvVaw2rHJmZ2IVCFHzAPCnzolom

HTML File relevant div IDs
1) About - Use Section ID for this
2) Publications - #h.wac2zk2z9r5i
3) Research - #h.t5dzel4hfwk9
4) Education - #h.rl9tbx1e53v5
5) Experience - #h.dgu5f2a7ah10
6) Contact - #h.2anh11c2z94e (Use[d] Section ID for this)

Replace with GitHub Pages links
1) About: https://sushanthvarada.github.io/#h.46484830237903f6_31
2) Contact: https://sushanthvarada.github.io/#h.65707dc883f98522_84

RUNNING the Python Script "replace-href_add-css.py"
Perform (1) if links don't contain "&amp;" else we can ignore it
(1) MANUAL STEP BEFORE RUNNING THE SCRIPT:
   Replace "&" with "&amp;"
   THIS ADJUSTS THE OLD LINKS COPIED FROM PUBLISHED GOOGLE SITE WITH THAT OF STORED LINKS IN HTML FILE
(2) AFTER Running the Python script --> Copy "About.html" --> Rename it to "index.html"