from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from geodata.models import City
from api.city import serializers
from rest_framework_extensions.cache.mixins import CacheResponseMixin


class CityList(CacheResponseMixin, ListAPIView):
    """
    Returns a list of IATI Cities stored in OIPA.

    ## Request parameters

    - `fields` (*optional*): List of fields to display
    - `fields[aggregations]` (*optional*): Aggregate available information.
        See [Available aggregations]() section for details.

    ## Available aggregations

    API request may include `fields[aggregations]` parameter.
    This parameter controls result aggregations and
    can be one or more (comma separated values) of:

    - `total_budget`: Calculate total budget of activities
        presented in cities activities list.
    - `disbursement`: Calculate total disbursement of activities
        presented in cities activities list.
    - `commitment`: Calculate total commitment of activities
        presented in cities activities list.

    ## Result details

    Each result item contains short information about city including URI
    to city details.

    URI is constructed as follows: `/api/cities/{city_id}`

    """
    queryset = City.objects.all().order_by('id')
    serializer_class = serializers.CitySerializer
    fields = ('url', 'id', 'name')


class CityDetail(CacheResponseMixin, RetrieveAPIView):
    """
    Returns detailed information about City.

    ## URI Format

    ```
    /api/cities/{city_id}
    ```

    ### URI Parameters

    - `city_id`: Numerical ID of desired City

    ## Request parameters

    - `fields` (*optional*): List of fields to display

    ## Extra Endpoints

    ### City Indicators

    `/api/cities/{city_id}/indicators`: List of indicators
    connected to specified city.

    """
    queryset = City.objects.all()
    serializer_class = serializers.CitySerializer
