- Using filters is essential to optimize the search.
  - The result of a filter can be cached and reused for subsequent searches because the result will be the same for all searches with the same filters. USing a compact bitmap to cach them is quite cheap.
  - Rule of thumb: use filters when you can and queries when you must.
- Three places where filtering can happen: in a **filtered query**, in **filter aggreations** and in **post filters**
![](https://github.com/ujhuyz0110/notes/blob/master/pics/three_filtering_places.png)
[source: https://www.elastic.co/blog/found-optimizing-elasticsearch-searches]
  - `filtered`-query can apply filters *before queries*. Example:
  ```
  query:
   filtered:
       query:
              multi_match:
              query: "query tuning"
              fields: ["title^5", "body"]
       filter:
           term:
               tag: "elasticsearch"
               
  Example taken from: https://www.elastic.co/blog/found-optimizing-elasticsearch-searches
  ```
  - `post_filter` is useful when you need *aggregations to be unfiltered but hits to be filtered*
