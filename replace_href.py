#MANUAL STEP BEFORE RUNNING THE SCRIPT:
#Replace "&" with "&amp;"
#THIS ADJUSTS THE OLD LINKS COPIED FROM PUBLISHED GOOGLE SITE WITH THAT OF STORED LINKS IN HTML FILE

import fileinput

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
    old_string = ["About.html","https://www.google.com/url?q=https%3A%2F%2Fsites.google.com%2Fview%2Fsushanthvarada%2Fabout%23h.2anh11c2z94e&amp;sa=D&amp;sntz=1&amp;usg=AOvVaw2rHJmZ2IVCFHzAPCnzolom"]
    new_string = ["https://sushanthvarada.github.io/#h.46484830237903f6_31","https://sushanthvarada.github.io/#h.65707dc883f98522_84"]

    # Call the function to perform the replacement
    for i in range(len(old_string)):
        replace_strings_in_html(html_file_path, old_string[i], new_string[i])

    print("Replacement completed.")
