'use strict'

cached_data = 
  data: {}

is_first = true

angular.module 'roadpinFrontendApp'
  .factory 'jsonAll', <[ $resource ]> ++ ( $resource ) -> do
    getData: ->
      if not is_first
        return cached_data.data

      is_first := false

      url = 'http://106.187.101.193/get_json_all'
      QueryData = $resource url

      the_data = QueryData.query {}, ->
        cached_data.data <<< the_data
        console .log 'cached_data.data.length:', cached_data.data.length, 'cached_data.data:', cached_data.data
          
      return cached_data.data
