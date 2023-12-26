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

    # Example usage for Addition of css
    string_to_add = '<link rel="stylesheet" href="global-styles.css">'
    add_string_before_head(html_file_path, string_to_add)
