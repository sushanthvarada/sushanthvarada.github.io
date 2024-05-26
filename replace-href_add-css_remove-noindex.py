#MANUAL STEP BEFORE RUNNING THE SCRIPT:
#Replace "&" with "&amp;"
#THIS ADJUSTS THE OLD LINKS COPIED FROM PUBLISHED GOOGLE SITE WITH THAT OF STORED LINKS IN HTML FILE

import fileinput
import re


#FUNCTION TO REPLACE Href
def replace_strings_in_html(file_path, old_string, new_string):
    # Iterate over the lines in the HTML file
    with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
        for line in file:
            # Replace old_string with new_string
            print(line.replace(old_string, new_string), end='')

#FUNCTION TO ADD CSS reference
def add_string_before_head(html_file_path, string_to_add):
    try:
        # Read the HTML file
        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Define the pattern to locate </head> tag
        head_pattern = re.compile(r'</head>', re.IGNORECASE)

        # Insert the string before </head>
        modified_html = re.sub(head_pattern, f'{string_to_add}</head>', html_content)

        # Write the modified HTML back to the file
        with open(html_file_path, 'w', encoding='utf-8') as file:
            file.write(modified_html)

        print(f'String added successfully to {html_file_path}')
    
    except FileNotFoundError:
        print(f'Error: File not found - {html_file_path}')
    except Exception as e:
        print(f'An error occurred: {e}')

#FUNCTION TO REMOVE META TAG 'NOINDEX'
def remove_text_from_html(html_file_path, string_to_remove):
    try:
        with open(html_file_path, 'r') as file:
            html_content = file.read()

        # Use regular expression to find and remove the specified text
        modified_html = re.sub(re.escape(string_to_remove), '', html_content)

        with open(html_file_path, 'w') as file:
            file.write(modified_html)

        print(f"Text '{string_to_remove}' removed successfully from {html_file_path}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Specify the path to your HTML file
    html_file_path = "C:/Users/susha/Documents/GitHub/Sites/sushanthvarada.github.io/About.html"

    # Specify the string you want to replace and its replacement
    
    #old string entry links = [About, Publications, Research, Education, Experience, Contact]
    old_string = ["About.html","https://www.google.com/url?q=https%3A%2F%2Fsites.google.com%2Fview%2Fsushanthvarada%2Fabout%23h.wac2zk2z9r5i&amp;sa=D&amp;sntz=1&amp;usg=AOvVaw0EJMxFKbOj2TFI-XsI4L4B","https://www.google.com/url?q=https%3A%2F%2Fsites.google.com%2Fview%2Fsushanthvarada%2Fabout%23h.t5dzel4hfwk9&amp;sa=D&amp;sntz=1&amp;usg=AOvVaw31nwu5fpZ2kpfKBcrrjwWr","https://www.google.com/url?q=https%3A%2F%2Fsites.google.com%2Fview%2Fsushanthvarada%2Fabout%23h.rl9tbx1e53v5&amp;sa=D&amp;sntz=1&amp;usg=AOvVaw1pfszewwnFn5sCu1lmA6pA","https://www.google.com/url?q=https%3A%2F%2Fsites.google.com%2Fview%2Fsushanthvarada%2Fabout%23h.dgu5f2a7ah10&amp;sa=D&amp;sntz=1&amp;usg=AOvVaw2EG_MPWVALCO9guXvp8REX","https://www.google.com/url?q=https%3A%2F%2Fsites.google.com%2Fview%2Fsushanthvarada%2Fabout%23h.2anh11c2z94e&amp;sa=D&amp;sntz=1&amp;usg=AOvVaw2rHJmZ2IVCFHzAPCnzolom"]
     
    # (Legacy) new string Section ID numbers out of 18 (cf. ReadMe & DoMe txt file) = [1, 4, 5, 10, 14, 17]
    #new_string = ["https://sushanthvarada.github.io/#h.46484830237903f6_31","https://sushanthvarada.github.io/#h.3241f61572ff7070_3","https://sushanthvarada.github.io/#h.72da52c0c87c277_46","https://sushanthvarada.github.io/#h.7b2b0d2a64a075bc_95","https://sushanthvarada.github.io/#h.ac1910601f7f19a_3","https://sushanthvarada.github.io/#h.65707dc883f98522_84"]
     
    #new string with About.html replaced with Section ID and the rest replaced with div ID
    new_string = ["https://sushanthvarada.github.io/#h.46484830237903f6_31","https://sushanthvarada.github.io/#h.wac2zk2z9r5i","https://sushanthvarada.github.io/#h.t5dzel4hfwk9","https://sushanthvarada.github.io/#h.rl9tbx1e53v5","https://sushanthvarada.github.io/#h.dgu5f2a7ah10","https://sushanthvarada.github.io/#h.2anh11c2z94e"]
    
    # Call the function to perform the replacement
    for i in range(len(old_string)):
        replace_strings_in_html(html_file_path, old_string[i], new_string[i])

    print("Replacement completed.")

    # Example usage for Addition of css string
    string_to_add = '<link rel="stylesheet" href="global-styles.css"><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta property="og:site_name" content="Sushanth Varada | Doctoral Researcher"><meta property="og:title" content="Sushanth Varada | Doctoral Researcher"/><meta property="og:url" content="https://sushanthvarada.github.io/"><meta property="og:type" content="website"><meta property="og:description" content="PhD Candidate at Uppsala University"/><meta property="og:image" content="https://sushanthvarada.github.io/About/DSCN1274.jpg"/><meta property="og:image:width" content="700"><meta property="og:image:height" content="500"><meta itemprop="name" content="Sushanth Varada | Doctoral Researcher"><meta itemprop="url" content="https://sushanthvarada.github.io/"><meta itemprop="description" content="PhD Candidate at Uppsala University"><meta itemprop="thumbnailUrl" content="https://sushanthvarada.github.io/About/DSCN1274.jpg"><link rel="image_src" href="https://sushanthvarada.github.io/About/DSCN1274.jpg"><meta itemprop="image" content="https://sushanthvarada.github.io/About/DSCN1274.jpg"><meta name="twitter:title" content="Sushanth Varada | Doctoral Researcher"><meta name="twitter:image" content="https://sushanthvarada.github.io/About/DSCN1274.jpg"><meta name="twitter:url" content="https://sushanthvarada.github.io/"><meta name="twitter:card" content="Sushanth Varada | Doctoral Researcher"><meta name="twitter:description" content="PhD Candidate at Uppsala University"><meta name="description" content="PhD Candidate at Uppsala University"><meta name="thumbnail" content="https://sushanthvarada.github.io/About/DSCN1274.jpg">'
    add_string_before_head(html_file_path, string_to_add)

    # Example usage for removal of noindex meta tag
    string_to_remove = '<meta name="robots" content="noindex">'
    remove_text_from_html(html_file_path, string_to_remove)
