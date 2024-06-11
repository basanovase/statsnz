<h1>statsnz</h1>

A collection of functions to enable ease of use of the various Stats New Zealand APIs, in python.


Installion:

  pip install statsnz



<h2>Examples:</h2>


Geocoding:


  To get the region with a set of coordinates:

  Below is the core method, other methods below have been retained for legacy compatibility, but but note they're hardcoded to:


```python
from statsnz import StatsNZ
stats = StatsNZ("YOUR_API_KEY")
# Example using the 2015 DHB layer
layer_id = 87883
lat = -41.242
long = 172.323
key_name = 'DHB2015_Name'
```


LEGACY EXAMPLES

dhb_example = stats.get_area_layer(layer_id, lat, long, key_name)
print(dhb_example)

    from statsnz import statsnz

    region_example = statsnz.statsnz("YOUR_API_KEY").get_region(-41.242,172.323)


  Or TLA:

    region_example = statsnz.statsnz("YOUR_API_KEY").get_tla(-41.242,172.323)

  Or DHB:

      region_example = statsnz.statsnz("YOUR_API_KEY").get_dhb(-41.242,172.323)



  Or a custom layer:

    region_example = statsnz.statsnz("YOUR_API_KEY").get_custom(-41.242,172.323)


Odata API:


    from statsnz import statsnz

    statsnz = statsnz("YOUR_API_KEY")
    service = 'https://api.stats.govt.nz/opendata/v1'
    endpoint = 'EmploymentIndicators'
    entity = 'Resources'
    query_option = "10" ##Top 10 records



    Observations = statsnz.statsnz.get_odata_api(service, endpoint, entity, query_option)
