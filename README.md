# Django-ELK
Django centralised logging using Elasticsearch, Logstash, Kibana (ELK) + Filebeat

## Components:  
  - **Filebeat** monitors changes in the log file and sends all new records to the Elasticsearch storage directly or through a parser called Logstash,  
  - **Elasticsearch** is an open source, full-text search and analysis engine,  
  - **Kibana** is a visualization layer that works on top of Elasticsearch, providing users with the ability to analyze and visualize the data,
  - **Logstash**  is a tool for parsing and streaming data from our log files to Elasticsearch.  

    ![schema](https://remaster.com/img/blog/elk/schema.png)

