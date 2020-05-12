# dataops-newsletter
scripts to help with generating dataops newsleter

* Edit the Newsletter in Quip - https://zapier.quip.com/DCGCAJ866aoB/DataOps-Newsletter
* Copy and paste it into Google Docs here - https://docs.google.com/document/d/14hyyvJL28WwMSOEupPGuaE-br1vMfVWtPiWnB567Xw0/edit#heading=h.yc9oymy5947m
* Run the script in Tools -> Script Editor in google docs
* The output will be emailed to you. 
* download the .md file and copy that into /Users/pengthom/Project/dataops-newsletter/draft.md
* run python3 gen_toc.py
        The script expects that "Executive Summary" and "The Details" are header 1 style. 
        Sections are Header 2
        Articles are Header 3
* open the <year>-<month>-final.md file and review it. 
* copy The file and post in async
* Replace quip referenceses to users names with @username   
