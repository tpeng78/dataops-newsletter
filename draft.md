# **March 2020**

## **Executive Summary**

The Data Team is moved quickly to clarify priorities and reprioritize where necessary as COVID-19 has changed our business. March has been extremely productive in delivering new data models and dashboards (Discounts MRR/ARR, Churn Surveys, R&D Monthly Reporting, and the Initiatives Dashboard). At the same time, we have been looking into ways to optimize our data systems and make our ETL more reliable. We are have defaulted to action to try out new technologies and these given our query and ETL loads a boost, but we have also learned some lessons along the way. We realize this is a bit bumpy, but we are intentionally moving fast here to get results. Please let us know if the turbulence is too much! 😄

[https://media.giphy.com/media/JUGhHEPJujsRARMNXl/giphy.gif](https://media.giphy.com/media/JUGhHEPJujsRARMNXl/giphy.gif)

## **The Details**

## **New data/data models Available!**

### **Discounts included in MRR/ARR**

**Author:**[ Dave Rodabaugh](https://zapier.quip.com/XPRAEAAGkX9)

**Zapier teams / zones that will find value:** Finance and Revenue

**Summary:** MRR/ARR is now more accurate because it includes discounts.

**Driver/initial use case:** Zapier has always offered a limited number of discounts, but discounts may be useful to woo new customers. As discounting increases, MRR without discounts would become less accurate.

**Other details:** Including discounts in MRR/ARR was "just in time" for Zapier’s COVID-19 response, which has resulted in many discounts to keep customers active (and paying upon a future renewal) instead of churning.

**Want to learn more? Please contact****[ Dave Rodabaug**h](https://zapier.quip.com/XPRAEAAGkX9)**.**

### **R&D Monthly Reporting**

**Author:**[ Catia Silvestre](https://zapier.quip.com/eCDAEA1R3CR)

**Zapier teams / zones that will find value:** Accounting

**Summary:** R&D Report is no longer a manual process and it runs every 4th of the month. Reports get added to this folder[ https://drive.google.com/drive/folders/1vQP2_bbOXg8lcXJOjpXG5VGueTWp9BBu](https://drive.google.com/drive/folders/1vQP2_bbOXg8lcXJOjpXG5VGueTWp9BBu).

**Driver/initial use case:** Helping accounting team to have more time to work on other projects whilst still giving them the tools to reclaim tax credit for US employees developed work.

**Want to learn more? Please contact****[ Catia Silvestr**e](https://zapier.quip.com/eCDAEA1R3CR)**.**

### **Initiatives dashboard**

**Author:**[ Catia Silvestre](https://zapier.quip.com/eCDAEA1R3CR)

**Zapier teams / zones that will find value:** Crosses all areas (Org.)

**Summary:** a dashboard that shows every initiative folks work on and any uncategorized work that takes focus out of those initiatives. ([https://zapier.looker.com/dashboards/560](https://zapier.looker.com/dashboards/560))

**Driver/initial use case:** The need to understand how work is allocated across initiatives during 2020. More info on this post[ https://async.zapier.com/p/initiative-allocation-tracking](https://async.zapier.com/p/initiative-allocation-tracking) by[ Alex Zogheb](https://zapier.quip.com/UWKAEAsEyhN).

**Want to learn more? Please contact****[ Catia Silvestr**e](https://zapier.quip.com/eCDAEA1R3CR)

### **Churned Surveys Modeling**

**Author:**[ Catia Silvestre](https://zapier.quip.com/eCDAEA1R3CR) &[ Russell Pierce](https://zapier.quip.com/PeZAEAYokZM)

**Zapier teams / zones that will find value:** Crosses all areas (Org.)

**Summary:** ability to view different reasons why customers downgrade / churn, with a COVID-19 connotation, as well.

**Driver/initial use case:** We want to have a better understanding of what drives account downgrade/churn. Although there were old views on user churn survey data, they had become invalid due to changes in the items in the survey. As COVID got going, it became even more important to analyze the reasons why people were churning. This work processes data from new survey items and uses a more reliable data source.

**Other details:** We can now see the percentage of customers downgrading / churning who fill in our survey[ https://zapier.looker.com/explore/Zapier/fact_churn_surveys?qid=uSvEpHBFi6TUDsNxmfZ5FO](https://zapier.looker.com/explore/Zapier/fact_churn_surveys?qid=uSvEpHBFi6TUDsNxmfZ5FO) and the reasons behind it, per country:[ https://zapier.looker.com/explore/Zapier/hs_churned_surveys?qid=gIu0fv10t9tSpLLSzZ5pxf&toggle=dat,vis](https://zapier.looker.com/explore/Zapier/hs_churned_surveys?qid=gIu0fv10t9tSpLLSzZ5pxf&toggle=dat,vis)

**Want to learn more? Please contact****[ Catia Silvestr**e](https://zapier.quip.com/eCDAEA1R3CR)** /****[ Russell Pierc**e](https://zapier.quip.com/PeZAEAYokZM)**.**

## **Data Products Corner**

### **COVID text analyses**

**Author:** @kristie

**Summary:** These categories of Zaps have increased since COVID: sending users messages, webinar related Zaps, sending client questionnaires, getting news alerts, customer support forms, and volunteer sign up forms. These categories of churn survey responses have increased since COVID: businesses shutting down, cutting costs, and losing clients.

**Challenges:** Churn survey data modeling is a work in progress, so I had to query hs_threads with some custom filters ([https://zapier.slack.com/archives/C43DUMF3P/p1585592989340600](https://zapier.slack.com/archives/C43DUMF3P/p1585592989340600)).

**Want to learn more? Please contact @kristie.**

**Resources:**

* Zap title results

    * Percentage differences by cluster:[ https://docs.google.com/spreadsheets/d/1ZHmCFxhY7dWgm2DcNqJvcAqo2qFkHNWS1tn64RrcMtk/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1ZHmCFxhY7dWgm2DcNqJvcAqo2qFkHNWS1tn64RrcMtk/edit?usp=sharing)

    * Detailed output (example titles, app combinations, keywords in clusters):[ https://github.com/zapier/new-use-cases/tree/master/results](https://github.com/zapier/new-use-cases/tree/master/results)

* Churn survey results

    * Percentage differences by cluster:[ https://docs.google.com/spreadsheets/d/1Aubow7x1goNH5UlnlDlzYSxQUzfQcOMww3lhinG-Zx0/edit#gid=1134494411](https://docs.google.com/spreadsheets/d/1Aubow7x1goNH5UlnlDlzYSxQUzfQcOMww3lhinG-Zx0/edit#gid=1134494411)

    * Details of keywords and example text in each cluster:

        * [https://github.com/zapier/new-use-cases/blob/master/results/NMF_with_20_topics_BEFORE_CHURN_SURVEYS](https://github.com/zapier/new-use-cases/blob/master/results/NMF_with_20_topics_BEFORE_CHURN_SURVEYS)

        * [https://github.com/zapier/new-use-cases/blob/master/results/NMF_with_20_topics_AFTER_CHURN_SURVEYS](https://github.com/zapier/new-use-cases/blob/master/results/NMF_with_20_topics_AFTER_CHURN_SURVEYS)

### **Help Scout Response Suggester Updates**

**Author:** @kristie

**Zapier teams / zones that will find value: **Support

**Summary:** I am now showing suggestions that have 80% similar text or higher, and I went from ~16% of suggestions being approved to ~74% (+/- 14%) of suggestions being approved!

**Driver/initial use case:** Helping support scale.

**Other details:** I’m also continuing to experiment with adding more information to the model, in hopes that it can predict helpful suggestions with even higher precision. So far, I have added contact form category and most recent error message text, and this has slightly improved the model ([https://zapier.slack.com/archives/C43DUMF3P/p1584655865457800](https://zapier.slack.com/archives/C43DUMF3P/p1584655865457800)). Next steps are to add most recent page visit, most recent Zap opened, and most recent email sent as features. Then, I’m planning on running an A/B test(s) and building out the infrastructure to start sending these suggestions directly to users!

**Want to learn more? Please contact @kristie.**

**Resources:**

* Slack convo on latest improvements with real ticket data:[ https://zapier.slack.com/archives/C43DUMF3P/p1585264294173200](https://zapier.slack.com/archives/C43DUMF3P/p1585264294173200)

## **Data Governance**

The Data Governance Team came up with a[ plan](https://coda.io/d/Data-Governance_d8Ek2Dyo_SH/Current-plans_suLXr#_luR5L) that we’re very excited about, however, due to COVID-19 we are going to put the plan on pause. @ale will be working on the Revenue and Finance Pod because there is high priority work that needs more resources.

## **Data. Engineering Technical Corner**

### **Assertion Machine 2.0 Upgrade**

**Author:** @ChrisLettieri

**Zapier teams / zones that will find value: DEs, DWEs, DSs, and any other users of the Assertion Machine**

**Summary:** Assertions can now be executed by sending an HTTP request to data-bridge instead of needing to run Airflow.

**Driver/initial use case: **Airflow is a scheduler and should act only as a scheduler. Previously we had Airflow actually execute the SQL queries and logic that powered the Assertion Machine. Now that Airflow has been decoupled from the Assertion Machine we can execute groups or individual assertions with a simple API request.

**Other details:** The CI has improved as well. Now changes will be automatically deployed upon merging to master and tests ran on each update to your PR branch.

**Want to learn more? Please contact **@ChrisLettieri

**Resources:**

[https://github.com/zapier/assertion_machine#what-you-need-to-know-about-20](https://github.com/zapier/assertion_machine#what-you-need-to-know-about-20)

### **Hookgest to ingest Webhooks**

**Zapier teams / zones that will find value: DEs, DWEs, anyone interested in how ETL is going**

**Summary**:[ Hookgest](https://github.com/zapier/hookgest) - Allows us to process arbitrary json payloads.

**Initial use case**: Ingest Zoom webinar webhooks.

**Details: **Hookgest is a simple proxy standing between the Internet and our Kafka REST endpoints. While we initially built it to support Zoom webinar webhooks, we’ve already added support for Iterable hooks as well.

### **Tool to Query Events in S3**

**Zapier teams / zones that will find value: DEs, DWEs, anyone interested in how ETL is going**

**Summary**:[ Endex](https://github.com/zapier/endex) - Queries event-with-properties data

**Initial use case**: Command line tool that will allow analysts to inspect individual events on S3.

### **More ETL parallelism**

Author: @drazen

**Zapier teams / zones that will find value: DEs, DWEs, DSs, and any Data stakeholders**

**Summary**: We’ve added more task parallelism in Matillion

**Details**: At the moment our ETL workload is primary running in Matillion. Matillion has two types of workload, transformation jobs and orchestration jobs. We’ve previously supported running up to eight orchestration jobs and one transformation job. We’ve now increased those limits to 16 jobs, and the limit is shared between orchestration and transformation jobs.

**Want to learn more? Please contact **@drazen

### **Shiny new Redshift hardware**

**Author: @drazen**

**Zapier teams / zones that will find value: DEs, DWEs, DSs, and anyone using Looker**

**Summary**: We’ve switched to a new node type that should result in faster everything and save some $$ in the process

**Details**: We’ve migrated from a 12 node ds2.xlarge nodes to three ra3.4xlarge nodes. Price points of these two clusters are approximately equal. Ee will experiment with going down to a two node cluster for bigger savings. Overall we’ve traded some processor cores for 5x more IO, faster networking with a lot less network overhead, and about 10x more storage, which will be especially helpful for Looker queries, which can sometimes cache a lot of data to disk. Looks like we’ve shaved about 4 hours off our ETL time, and that is a big win on its own

### **Observability into data processes and metadata**

**Author: @drazen**

**Zapier teams / zones that will find value: DEs, DWEs, anyone interested in how ETL is going**

**Summary**:[ hq.data.zapier.com](http://hq.data.zapier.com/)

**Initial use case**: As our ETL is a true distributed system we have had quite low observability into events across all the systems it touches. We’ve finally made a dent with the launch of[ data-hq](http://hq.data.zapier.com/). Which will overtime become a central place for self-service around data about data.

## **DataOps Backoffice**

### **Prioritization in Jira**

We have worked hard to get a clarified list of priorities across Data! @erinmullen has created a[ Data Planning & Prioritization Jira Board](https://zapierorg.atlassian.net/secure/RapidBoard.jspa?rapidView=288&projectKey=DATA) to track our top priorities across data. This will allow us to align the team on working on the most important things.

We are also starting to use a [looker help us identify tickets that are stuck in progress](https://zapier.looker.com/looks/1959) so we can reach out to help unblock them. 

