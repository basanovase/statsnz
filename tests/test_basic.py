from statsnz import statsnz

#region_example = statsnz("YOUR_API_KEY").get_region(-41.242,172.323))

#print(region_example)


service = 'https://api.stats.govt.nz/opendata/v1'
endpoint = 'EmploymentIndicators'
entity = 'Resources'
query_option = "$top=10"


proxies = {'https': 'your-proxy.co.nz:8080'}  ## proxies = {} if none
Observations = statsnz("7299df151fd448508e2d70be509bfeae").get_odata_api(service, endpoint, entity, query_option, proxies)

print(observations)
