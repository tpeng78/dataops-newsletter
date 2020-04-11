# parse giphy images
# add footer 

import datetime 

def main():
    
    f= open("draft.md","r")
    header= open("intro.html","r")
    footer=open("footer.html","r")

    today= datetime.date.today()
    asyncPost = open(today.strftime("%Y-%b") + ".md","w+")
    tocSnippet = open(today.strftime("%y-%b") + "_toc.md", "w+")
    tocSnippet.write("<ul>\n")

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
            if counterH2 > 0:
                tocSnippet.write("        </ul>\n")
            tocSnippet.write("    <li>" + x.title().rstrip()[startTitle:] + "\n")
            tocSnippet.write("        <ul>\n")
            counterH2 = counterH2 + 1

        else:
            asyncPost.write(x)
            # need code to check if there is a gif and put an exlamation point in front of it. 
    tocSnippet.write("        </ul>\n")
    tocSnippet.write("</ul>\n")

    footerlines = footer.readlines()

    for x in footerlines:
        asyncPost.write(x)

    asyncPost.close()
    tocSnippet.close()
    f.close()
    header.close()

if __name__=="__main__":
    main()