CSS - Fonts & Scrollings effects (UPDATE About.html and then COPY to CREATE index.html)
[Automated this CSS file link addition via Python script: "replace-href_add-css.py"] 
1) Add the code snippet "<link rel="stylesheet" href="global-styles.css">" just before <\head> in About/index.html
2) Add "html {scroll-behaviour: smooth}" and relevant @font-face{<code>} to global-styles.css file 
2) Make sure to upload the global-styles.css file (within this folder) to the GitHub repository

NAVBAR - Replace googlesites section links with HTML section_ids for same-page navigation without refreshing the page:
HTML File Section IDs
1) About Section ID: #h.46484830237903f6_31
2) Contact Section ID: #h.65707dc883f98522_84

Google Sites Links
1) a) SV Mobius ring icon: About.html
   b) Sushanth Varada | Doctoral Researcher title: About.html
   c) About Navbar button: About.html
2) Contact Navbar button: https://www.google.com/url?q=https%3A%2F%2Fsites.google.com%2Fview%2Fsushanthvarada%2Fabout%23h.2anh11c2z94e&sa=D&sntz=1&usg=AOvVaw2rHJmZ2IVCFHzAPCnzolom

Replace with GitHub Pages links
1) About: https://sushanthvarada.github.io/#h.46484830237903f6_31
2) Contact: https://sushanthvarada.github.io/#h.65707dc883f98522_84

RUNNING the Python Script "replace-href_add-css.py"
1) MANUAL STEP BEFORE RUNNING THE SCRIPT:
   Replace "&" with "&amp;"
   THIS ADJUSTS THE OLD LINKS COPIED FROM PUBLISHED GOOGLE SITE WITH THAT OF STORED LINKS IN HTML FILE