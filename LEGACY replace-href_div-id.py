#MANUAL STEP BEFORE RUNNING THE SCRIPT:
#Replace "&" with "&amp;"
#THIS ADJUSTS THE OLD LINKS COPIED FROM PUBLISHED GOOGLE SITE WITH THAT OF STORED LINKS IN HTML FILE

import fileinput

#FUNCTION TO REPLACE Href
def replace_strings_in_html(file_path, old_string, new_string):
    # Iterate over the lines in the HTML file
    with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
        for line in file:
            # Replace old_string with new_string
            print(line.replace(old_string, new_string), end='')

if __name__ == "__main__":
    # Specify the path to your HTML file
    html_file_path = "C:/Users/susha/Documents/GitHub/Sites/sushanthvarada.github.io/About.html"

    # Specify the string you want to replace and its replacement
    #String entries = [About, Publications, Research, Education, Experience, Contact] 
    old_string = ["https://sushanthvarada.github.io/#h.3241f61572ff7070_3","https://sushanthvarada.github.io/#h.72da52c0c87c277_46","https://sushanthvarada.github.io/#h.7b2b0d2a64a075bc_95","https://sushanthvarada.github.io/#h.ac1910601f7f19a_3"]
    #new string div IDs (cf. ReadMe & DoMe txt file) = [1, 4, 5, 10, 14, 17] 
    new_string = ["https://sushanthvarada.github.io/#h.wac2zk2z9r5i","https://sushanthvarada.github.io/#h.t5dzel4hfwk9","https://sushanthvarada.github.io/#h.rl9tbx1e53v5","https://sushanthvarada.github.io/#h.dgu5f2a7ah10"]
    # Call the function to perform the replacement
    for i in range(len(old_string)):
        replace_strings_in_html(html_file_path, old_string[i], new_string[i])

    print("Replacement completed.")