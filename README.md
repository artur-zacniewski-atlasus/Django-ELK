# Django-ELK
Django centralised logging using Elasticsearch, Logstash, Kibana (ELK) + Filebeat

## Components:  
  - **Filebeat** monitors changes in the log file and sends all new records to the Elasticsearch storage directly or through a parser called Logstash,  
  - **Elasticsearch** is an open source, full-text search and analysis engine,  
  - **Kibana** is a visualization layer that works on top of Elasticsearch, providing users with the ability to analyze and visualize the data,
  - **Logstash**  is a tool for parsing and streaming data from our log files to Elasticsearch.  

    ![schema](https://remaster.com/img/blog/elk/schema.png)

## Running the project

The project is split into the following two apps:  
  - blog - for our Django models, serializers, and ViewSets,
  - search - for Elasticsearch documents, indexes, and queries.

#### How to start it?
1. Fork/Clone

2. [Install Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) if you haven't already and make sure it is running on port `9200` (check 'Remarks' for more information).

3. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv venv && source venv/bin/activate
    ```

4. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

5. Apply the migrations:

    ```sh
    (venv)$ python manage.py migrate
    ```

6. Populate the database with some test data by running the following command:

    ```sh
    (venv)$ python manage.py populate_db
    ```

7. Create and populate the Elasticsearch index and mapping:

    ```sh
    (venv)$ python manage.py search_index --rebuild
    ```

8. Run the server

    ```sh
    (venv)$ python manage.py runserver
    ```

9. Test Elasticsearch with the following queries:

     - [http://127.0.0.1:8000/search/user/mike/](http://127.0.0.1:8000/search/user/mike/) - should find the user 'mike13'
     - [http://127.0.0.1:8000/search/user/jess_/](http://127.0.0.1:8000/search/user/jess_/) - should find the user 'jess_'
     - [http://127.0.0.1:8000/search/category/seo/](http://127.0.0.1:8000/search/category/seo/) - should find the category 'SEO optimization'
     - [http://127.0.0.1:8000/search/category/progreming/](http://127.0.0.1:8000/search/category/progreming/) - should find the category 'Programming' (:warning: notice the typo)
     - [http://127.0.0.1:8000/search/article/linux/](http://127.0.0.1:8000/search/article/linux/) - should find the article 'Installing the latest version of Ubuntu'
     - [http://127.0.0.1:8000/search/article/java/](http://127.0.0.1:8000/search/article/java/) - should find the article 'Which programming language is the best?'


## Remarks
1. The configuration file for Elasticsearch is `/etc/elasticsearch/elasticsearch.yml`,
  - due to security reasons the default setting is `xpack.security.enabled: true`,
  - to get some information about our node after `curl -X GET "127.0.0.1:9200` or `curl -X GET "localhost:9200` 
  and to avoid `elasticsearch.exceptions.ConnectionError` error the aforementioned setting must be set to `false`
  - example of information:  
  ```bash
     {
      "name" : "artur-PC",
      "cluster_name" : "elasticsearch",
      "cluster_uuid" : "jaX4OnGHQSGrEzV6-9pl1w",
      "version" : {
        "number" : "8.6.2",
        "build_flavor" : "default",
        "build_type" : "deb",
        "build_hash" : "2d58d0f136141f03239816a4e360a8d17b6d8f29",
        "build_date" : "2023-02-13T09:35:20.314882762Z",
        "build_snapshot" : false,
        "lucene_version" : "9.4.2",
        "minimum_wire_compatibility_version" : "7.17.0",
        "minimum_index_compatibility_version" : "7.0.0"
      },
      "tagline" : "You Know, for Search"
    }
  ```
2. The project is based mainly on [Testdriven.io](https://testdriven.io/blog/django-drf-elasticsearch/) tutorial.  
