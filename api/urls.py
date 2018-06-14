from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view


router = DefaultRouter()
router.register(r'transactions', views.TransactionsViewSet)
router.register(r'transactiondetail', views.TransactionDetailViewSet)
router.register(r'statementoforg', views.StatementOfOrgViewSet)
router.register(r'payee', views.PayeeViewSet)
router.register(r'electionactivity', views.ElectionActivityViewSet)
router.register(r'donor', views.DonorViewSet)
router.register(r'committeeslist', views.CommitteesListViewSet)
router.register(r'committeehistory', views.CommitteeHistoryViewSet)
router.register(r'ballots', views.BallotsViewSet)
router.register(r'contributorbreakdown', views.ContributorBreakdownViewSet)
router.register(r'electioncycles', views.ElectionCyclesViewSet)
router.register(r'totalcontributionsmonthly', views.TotalContributionsMonthlyViewSet)
router.register(r'totalcontributionsyearly', views.TotalContributionsYearlyViewSet)
router.register(r'totalcontributionsrawinstate', views.TotalContributionsRawInStateViewSet)
router.register(r'totalcontributionsrawonthracetype', views.TotalContributionsRawMonthRaceTypeViewSet)

schema_view = get_swagger_view(title='Hack Oregon 2018 Local Elections APIs')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^', include(router.urls)),
]
