# Tips for Elasticsearch Optimization

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
- Combine filters with bool. Order filters by their selectivity. *Higher selectivity ones come first.*
- Understand what filters can be cached and what can't.
  - Cacheable filteres can reduce the burden of more expensive filters.
- Consider whether your aggregation can be implemented with a `filter` aggregation instead since you are already paying for the filters' memory.
- **Aggregations are expensive**. Reuse cached results or skip them entirely if possible.
- Think about how many top N results you really need to rank. If you really need to scroll through huge result sets, use `scroll` and `scan` APIs.
![](https://github.com/ujhuyz0110/notes/blob/master/pics/where_scoring_happens.png)
[source: https://www.elastic.co/blog/found-optimizing-elasticsearch-searches]
- Do not shoehorn everything into a single search request.
- If you use you use `_source` or `_fields` you will quickly **kill performance**. They access the stored fields data structure, which is intended to be used when accessing the resulting hits, not when processing millions of documents.

## Credits:
- https://www.elastic.co/blog/found-optimizing-elasticsearch-searches
