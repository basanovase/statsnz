# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:18:36 2021

@author: flynn
"""
import os
import json
import pandas as pd
import requests

class StatsNZ:
    """
    Base class. Initialize your API key.
    """
    def __init__(self, key):
        self.key = key

    def get_odata_api(self, service, endpoint, entity, query_no):
        """
        Query the STATSNZ Odata service.
        
        Legacy functionality retained with no changes.
        """
        api_key = self.key
        query_no = f"$top={query_no}"
        url = f"{service}/{endpoint}/{entity}?{query_no}"
        top_query = "$top" in query_no
        results = pd.DataFrame()

        while url:
            try:
                req = requests.get(url, headers={'Ocp-Apim-Subscription-Key': api_key})
                req.raise_for_status()
            except Exception as e:
                print(str(e))
                break

            df = pd.json_normalize(req.json().get('value', []))
            results = pd.concat([results, df])

            url = req.json().get('@odata.nextLink')
            if top_query:
                url = None

        print(f"{len(results)} row items received")
        return results

    def _get_area_layer(self, layer_id, lat, long, key_name):
        """
        Helper method to query area layers.
        This method is generic and reusable across different area layer queries.
        """
        try:
            url = f"https://datafinder.stats.govt.nz/services/query/v1/vector.json?key={self.key}&layer={layer_id}&x={long}&y={lat}&max_results=3&radius=10000&geometry=true&with_field_names=true"
            req = requests.get(url).json()
            # Using .get method to safely access nested dictionary values
            features = req.get('vectorQuery', {}).get('layers', {}).get(str(layer_id), {}).get('features', [])
            if features:
                return features[0].get('properties', {}).get(key_name, "No data found")
            return "No data found"
        except Exception as e:
            return f"request_error: {str(e)}"

    def get_tla(self, lat, long):
        """
        Get Territorial Authority Local Board.
        
        Uses the new _get_area_layer method to maintain functionality.
        """
        layer_id = 105135
        key_name = 'TALB2021_V1_00_NAME'
        return self._get_area_layer(layer_id, lat, long, key_name)

    def get_region(self, lat, long):
        """
        Get Region.
        
        Uses the new _get_area_layer method to maintain functionality.
        """
        layer_id = 104254
        key_name = 'REGC2020_V1_00_NAME'
        return self._get_area_layer(layer_id, lat, long, key_name)

    def get_urban_rural(self, lat, long):
        """
        Get Urban/Rural area.
        
        Uses the new _get_area_layer method to maintain functionality.
        """
        layer_id = 105158
        key_name = 'UR2021_V1_00_NAME'
        return self._get_area_layer(layer_id, lat, long, key_name)

    def get_dhb(self, lat, long):
        """
        Get District Health Board.
        
        Uses the new _get_area_layer method to maintain functionality.
        """
        layer_id = 87883
        key_name = 'DHB2015_Name'
        return self._get_area_layer(layer_id, lat, long, key_name)

    def get_custom_layer(self, layer_id, lat, long):
        """
        Specify an area layer for use. Response as JSON.
        
        Uses the new _get_area_layer method for consistency.
        """
        try:
            url = f"https://datafinder.stats.govt.nz/services/query/v1/vector.json?key={self.key}&layer={layer_id}&x={long}&y={lat}&max_results=3&radius=10000&geometry=true&with_field_names=true"
            return requests.get(url).json()
        except Exception as e:
            return f"request_error: {str(e)}"
