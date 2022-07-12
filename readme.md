Title: Stackoverflow Question Finder

FEATURES OF THE SYSTEM

1. List the questions based on the User's requests with pagination
2. Users can also apply parameters to the search such as sort, order, etc
3. Cache the Fetched result using Redis
4. Limit the maximum number of searches to 5/minute and 100/day by using the Throttle technique in the Django rest framework


CACHING TECHNIQUE

Here I'm using Redis for caching the data. It stores the requested API as the key and the data as the value.


The frontend template is built with HTML CSS and Bootstrap.