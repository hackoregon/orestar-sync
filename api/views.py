from datetime import datetime
import json

from api.models import (Transactions,
                        TransactionDetails,
                        StatementOfOrg,
                        Payee,
                        ElectionActivity,
                        Donor,
                        CommitteesList,
                        CommitteeHistory,
                        Ballots,
                        ContributorBreakdown,
                        ElectionCycles,
                        TotalContributionsMonthly,
                        TotalContributionsYearly,
                        TotalContributionsRaw,
                        TotalContributionsRawInState,
                        TotalContributionsRawMonthRaceType,
                        TotalContributionsRawMonthTotal,
                        SpendingBreakdown,
                        CommitteeContributors,
                        ContributorGraph,
                        VoterAcquisitionCost,)
from api.serializers import (TransactionsSerializer,
                            TransactionDetailSerializer,
                            StatementOfOrgSerializer,
                            PayeeSerializer,
                            ElectionActivitySerializer,
                            DonorSerializer,
                            CommitteesListSerializer,
                            CommitteeHistorySerializer,
                            BallotsSerializer,
                            ContributorBreakdownSerializer,
                            ElectionCyclesSerializer,
                            TotalContributionsMonthlySerializer,
                            TotalContributionsYearlySerializer,
                            TotalContributionsRawSerializer,
                            TotalContributionsRawInStateSerializer,
                            TotalContributionsRawMonthRaceTypeSerializer,
                            TotalContributionsRawMonthTotalSerializer,
                            SpendingBreakdownSerializer,
                            CommitteeContributorsSerializer,
                            ContributorGraphSerializer,
                            VoterAcquisitionCostSerializer,)

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

class TransactionsViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionsSerializer
    queryset = Transactions.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class TransactionDetailViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionDetailSerializer
    queryset = TransactionDetails.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class StatementOfOrgViewSet(viewsets.ModelViewSet):
    serializer_class = StatementOfOrgSerializer
    queryset = StatementOfOrg.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class PayeeViewSet(viewsets.ModelViewSet):
    serializer_class = PayeeSerializer
    queryset = Payee.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class ElectionActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ElectionActivitySerializer
    queryset = ElectionActivity.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class DonorViewSet(viewsets.ModelViewSet):
    serializer_class = DonorSerializer
    queryset = Donor.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class CommitteesListViewSet(viewsets.ModelViewSet):
    serializer_class = CommitteesListSerializer
    queryset = CommitteesList.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class CommitteeHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = CommitteeHistorySerializer
    queryset = CommitteeHistory.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class BallotsViewSet(viewsets.ModelViewSet):
    serializer_class = BallotsSerializer
    queryset = Ballots.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class ContributorBreakdownViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorBreakdownSerializer
    queryset = ContributorBreakdown.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class ElectionCyclesViewSet(viewsets.ModelViewSet):
    serializer_class = ElectionCyclesSerializer
    queryset = ElectionCycles.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class TotalContributionsMonthlyViewSet(viewsets.ModelViewSet):
    serializer_class = TotalContributionsMonthlySerializer
    queryset = TotalContributionsMonthly.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class TotalContributionsYearlyViewSet(viewsets.ModelViewSet):
    serializer_class = TotalContributionsYearlySerializer
    queryset = TotalContributionsYearly.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class TotalContributionsRawViewSet(viewsets.ModelViewSet):
    serializer_class = TotalContributionsRawSerializer
    queryset = TotalContributionsRaw.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class TotalContributionsRawInStateViewSet(viewsets.ModelViewSet):
    serializer_class = TotalContributionsRawInStateSerializer
    queryset = TotalContributionsRawInState.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class TotalContributionsRawMonthRaceTypeViewSet(viewsets.ModelViewSet):
    serializer_class = TotalContributionsRawMonthRaceTypeSerializer
    queryset = TotalContributionsRawMonthRaceType.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class SpendingBreakdownViewSet(viewsets.ModelViewSet):
    serializer_class = SpendingBreakdownSerializer
    queryset = SpendingBreakdown.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class CommitteeContributorsViewSet(viewsets.ModelViewSet):
    serializer_class = CommitteeContributorsSerializer
    queryset = CommitteeContributors.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class TotalContributionsRawMonthTotalViewSet(viewsets.ModelViewSet):
    serializer_class = TotalContributionsRawMonthTotalSerializer
    queryset = TotalContributionsRawMonthTotal.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filter_fields = '__all__'

class VoterAcquisitionCostViewSet(viewsets.ModelViewSet):
    serializer_class = VoterAcquisitionCostSerializer
    queryset = VoterAcquisitionCost.objects.all()
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
