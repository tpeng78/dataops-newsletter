def main():
    
    f= open("draft.md","r")


    f1 = f.readlines()

    for x in f1:
        header3 = x.find("###",0,5)
        if header3 < 0:
            print(x)
        else:
            ## Find the text
            ## remove spaces
            ## take first 20 chars
            ## create an anchor
            formattedText = x.lstrip()
            formattedText = formattedText.rstrip()
            
            print(formattedText)



if __name__=="__main__":
    main()