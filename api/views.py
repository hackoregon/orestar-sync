from datetime import datetime
import json

from api.models import oreStarData
from api.serializers import oreStarSerializer

from rest_framework.decorators import api_view, detail_route
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.exceptions import APIException
from django_filters.rest_framework import DjangoFilterBackend, FilterSet

from api.transaction_analysis.funding_similarity import SimilarityGraph

class oreStarDetailViewSet(viewsets.ModelViewSet):
    serializer_class = oreStarSerializer
    queryset = oreStarData.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

@api_view(['GET'])
def graph(request):
    """
    make a graph of donor contributions

    example --- /local-elections/contributorgraph?start=2002-12-31&end=2003-12-31&name=Barnie+Rubble
    `start` --- start date in format YYYY-m-d
    `end` --- end date in format YYYY-m-d
    `name` --- url encoded campaign to check
    """
    start = request.query_params.get("start")
    end = request.query_params.get("end")
    name = request.query_params.get("name")

    if not start or not end or not name:
        raise APIException("query parameters must include `start`, `end`, and `name`")

    try:
        start = datetime.strptime(start, "%Y-%m-%d")
        end = datetime.strptime(end, "%Y-%m-%d")
    except ValueError:
        raise APIException("date format is YYYY-m-d")

    graph = SimilarityGraph(start_date=start,
                        end_date=end)
    graph = graph.look_up(name)

    return Response(graph)
