# Takes a markdown file and then creates a table of contents based on the <h2> and <h3> headers. 
# Current process is the following:
#   1. create the newsletter in a quip document. 
#   2. copy the section and then past into google docs
#   3. run the convert2markdown script on google docs
#   4. The markdown file is emailed to you
#   5. copy the markdown file into ths root directory of this script and rename it to draft.md
#   6. Take the final version of the output and past into async
#
# to convert google docs to markdown use these directions: https://lifehacker.com/this-script-converts-google-documents-to-markdown-for-e-511746113 
# todo -  parse giphy images


import datetime 
import re 

def main():
    
    f= open("draft.md","r")
    header= open("intro.html","r")
    footer=open("footer.html","r")

    today= datetime.date.today()
    fileName = today.strftime("%Y-%b") + ".md"
    finalFileName = today.strftime("%Y-%b") + "-final.md"
    asyncPost = open(fileName,"w+")
    toc_filename = today.strftime("%y-%b") + "_toc.md"
    tocSnippet = open(toc_filename, "w+")
    tocSnippet.write("<ul>\n")
    giphy_regex_string = "(\[(http(s?):)([/|.|\w|\s|-])*\.(?:jpg|gif|png)\]\((http(s?):)([/|.|\w|\s|-])*\.(?:jpg|gif|png)\))"

    headerlines = header.readlines()

    for x in headerlines:
        asyncPost.write(x)

    f1 = f.readlines()
    counterH2 = 0
    for x in f1:
        linePrefix= x.split(" ")[0]
        if linePrefix == "###":
            ## Find the text
            ## remove spaces
            ## take first 20 chars
            ## create an anchor
            formattedText = x.lstrip()
            formattedText = formattedText.rstrip()
            formattedText = formattedText.title()
            startTitle = formattedText.index(" ")
            formattedText = formattedText.replace(" ","")
            formattedText = formattedText.replace('**','')
            anchorName = formattedText[startTitle:startTitle+20]
            anchorName = anchorName.replace('**','')
            
            # remove bolding in headers. this is not necessary. 
            x = x.replace("**","")

            asyncPost.write("<a name='" + anchorName + "'><h3>" + x.rstrip()[startTitle:] + "</h3></a>")
            tocSnippet.write("            <li><a href='#"+anchorName+"'>" + x.rstrip()[startTitle:].lstrip() + "</a>\n")
        elif linePrefix == "##":
            startTitle = x.index(" ")
            x = x.replace("**","")

            # Skip writing Executive Summary or The Details to the table of contents

            if x.find("# Executive Summary") == -1 and x.find("# The Details") == -1:
                if counterH2 > 0:
                    tocSnippet.write("        </ul>\n")
                tocSnippet.write("    <li>" + x.title().rstrip()[startTitle:] + "\n")
                tocSnippet.write("        <ul>\n")
                counterH2 = counterH2 + 1
            
            
            asyncPost.write(x)
        elif linePrefix == "#":
            startTitle = x.index(" ")
            x = x.replace("**","")

            # do not write this to Table of Contents            
            asyncPost.write(x)
        else:
            #assume that giphys are not in header lines
            if re.search(giphy_regex_string, x):
                print("match found!")
                print(re.sub(giphy_regex_string, r"!\1", x))
                x = re.sub(giphy_regex_string, r"!\1", x)

            asyncPost.write(x)
            # need code to check if there is a gif and put an exlamation point in front of it. 
    tocSnippet.write("        </ul>\n")
    tocSnippet.write("</ul>\n")

    footerlines = footer.readlines()

    for x in footerlines:
        asyncPost.write(x)

    asyncPost.close()

    f.close()
    header.close()
    tocSnippet.close()


    # reopen the file and insert the table of contents
    new_toc_snippet = open(today.strftime("%y-%b") + "_toc.md", "r+")

    draft = open(fileName,"r")
    final = open(finalFileName, "w")
    for x in draft: 
        if x.find("# The Details") != -1: 
            final.write(x)
            for l in new_toc_snippet.readlines():
                final.write(l)
        else:
            final.write(x)

    final.close()
    new_toc_snippet.close()

if __name__=="__main__":
    main()