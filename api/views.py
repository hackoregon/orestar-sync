from api.models import (Transactions,
                        TransactionDetails,
                        StatementOfOrg,
                        Payee,
                        ElectionActivity,
                        Donor,
                        CommitteesList,
                        CommitteeHistory,
                        Ballots,
                        TotalContributions,)
from api.serializers import (TransactionsSerializer, 
                            TransactionDetailSerializer,
                            StatementOfOrgSerializer, 
                            PayeeSerializer,
                            ElectionActivitySerializer, 
                            DonorSerializer,
                            CommitteesListSerializer, 
                            CommitteeHistorySerializer,
                            BallotsSerializer,
                            TotalContributionsSerializer,)

from rest_framework.decorators import api_view, detail_route
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet

class TransactionsViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionsSerializer
    queryset = Transactions.objects.all()    
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filtering_fields = '__all__'

class TransactionDetailViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionDetailSerializer
    queryset = TransactionDetails.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filtering_fields = '__all__'
    
class StatementOfOrgViewSet(viewsets.ModelViewSet):
    serializer_class = StatementOfOrgSerializer
    queryset = StatementOfOrg.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)   
    ordering_fields = '__all__'
    search_fields = '__all__'
    filtering_fields = '__all__'
    
class PayeeViewSet(viewsets.ModelViewSet):
    serializer_class = PayeeSerializer
    queryset = Payee.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)    
    ordering_fields = '__all__'
    search_fields = '__all__'    
    filtering_fields = '__all__'
    
class ElectionActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ElectionActivitySerializer
    queryset = ElectionActivity.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filtering_fields = '__all__'
    
class DonorViewSet(viewsets.ModelViewSet):
    serializer_class = DonorSerializer
    queryset = Donor.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter) 
    ordering_fields = '__all__'
    search_fields = '__all__' 
    filtering_fields = '__all__'
    
class CommitteesListViewSet(viewsets.ModelViewSet):
    serializer_class = CommitteesListSerializer
    queryset = CommitteesList.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filtering_fields = '__all__'
    
class CommitteeHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = CommitteeHistorySerializer
    queryset = CommitteeHistory.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__' 
    search_fields = '__all__'
    filtering_fields = '__all__'
    
class BallotsViewSet(viewsets.ModelViewSet):
    serializer_class = BallotsSerializer
    queryset = Ballots.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filtering_fields = '__all__'

class TotalContributionsViewSet(viewsets.ModelViewSet):
    serializer_class = TotalContributionsSerializer
    queryset = TotalContributions.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    search_fields = '__all__'
    filtering_fields = '__all__'    
