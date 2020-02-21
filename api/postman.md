Using Google Geosite API for GET demo. Create account with billing information and save the api key:
+ `<google-api-key>`
Activate the geocoding API navigating the *developer console* to ``Google Maps / APIs / Geocoding API`` and click *activate*. The API is ready to be called.

Save request `<name.request.postman> = get.request` to request collection `<collection.postman> = request.collection`. A postman collection is an executable description of an API.

+ `<address> = 1263+esplanaden+50+København+K`
+ `<request-url> = https://maps.googleapis.com/maps/api/geocode/json?address=<address>&key=YOUR_API_KEY`
+ `<http-verb> = GET`
Using postman, replace `YOUR_API_KEY` with `{{googleMapsGeocodingApiKey}}`.
Create new environment `<postman-env.postman> = google-maps-api-env` by clicking the `configuration` icon. Add variable to environment:
+ `<var.postman-env.postman> = googleMapsGeocodingApiKey`
+ `<value.postman-env.postman> = <google-api-key>`  
On clicking `Add`, select the recently added environment. Call the endpoint with the parameters above. The result should be:
```json
{
   "results": [
      {
         "address_components": [
            {
               "long_name": "50",
               "short_name": "50",
               "types": [
                  "street_number"
               ]
            },
            {
               "long_name": "Esplanaden",
               "short_name": "Esplanaden",
               "types": [
                  "route"
               ]
            },
            {
               "long_name": "København K",
               "short_name": "København K",
               "types": [
                  "political",
                  "sublocality",
                  "sublocality_level_1"
               ]
            },
            {
               "long_name": "København",
               "short_name": "København",
               "types": [
                  "locality",
                  "political"
               ]
            },
            {
               "long_name": "Denmark",
               "short_name": "DK",
               "types": [
                  "country",
                  "political"
               ]
            },
            {
               "long_name": "1263",
               "short_name": "1263",
               "types": [
                  "postal_code"
               ]
            }
         ],
         "formatted_address": "Esplanaden 50, 1263 København, Denmark",
         "geometry": {
            "location": {
               "lat": 55.6878047,
               "lng": 12.5970483
            },
            "location_type": "ROOFTOP",
            "viewport": {
               "northeast": {
                  "lat": 55.6891536802915,
                  "lng": 12.5983972802915
               },
               "southwest": {
                  "lat": 55.6864557197085,
                  "lng": 12.5956993197085
               }
            }
         },
         "place_id": "ChIJcb-z5iBTUkYRToQHd81FXIw",
         "plus_code": {
            "compound_code": "MHQW+4R Copenhagen, Copenhagen Municipality, Denmark",
            "global_code": "9F7JMHQW+4R"
         },
         "types": [
            "street_address"
         ]
      }
   ],
   "status": "OK"
}
```
Using Twitter API for GET demo. Create account and app at `developer.twitter.com/en/apps` TODO