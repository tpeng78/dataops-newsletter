import re

def main():

    giphy_regex_string = "(\[(http(s?):)([/|.|\w|\s|-])*\.(?:jpg|gif|png)\]\((http(s?):)([/|.|\w|\s|-])*\.(?:jpg|gif|png)\))"
    test_string = "thomas [https://media.giphy.com/media/JUGhHEPJujsRARMNXl/giphy.gif](https://media.giphy.com/media/JUGhHEPJujsRARMNXl/giphy.gif) looking  [https://media.giphy.com/media/JUGhHEPJujsRARMNXl/giphy.gif](https://media.giphy.com/media/JUGhHEPJujsRARMNXl/giphy.gif)  end"

    if re.search(giphy_regex_string, test_string):
        print("match found!")
        print(re.sub(giphy_regex_string, r"!\1", test_string))

if __name__=="__main__":
    main()