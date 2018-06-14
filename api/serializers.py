from rest_framework import serializers
from api.models import (Transactions, TransactionDetails, StatementOfOrg,
                       Payee, ElectionActivity, Donor, CommitteesList,
                       CommitteeHistory, Ballots, ContributorBreakdown,
                       ElectionCycles,TotalContributionsMonthly,
                       TotalContributionsYearly,TotalContributionsRawInState,
                       TotalContributionsRawMonthRaceType,)

class TransactionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = (
            "transaction_id", "committee_id", "transaction_date",
            "status", "filer_committee", "contributor_payee",
            "transaction_subtype", "total_amount",
        )

class TransactionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransactionDetails
        fields = (
            "transaction_id", "payee_id", "donor_id",
            "address", "address_book_type", "agent",
            "total_aggregate", "total_amount", "associations",
            "description", "due_date", "employer_name",
            "filed_date", "name", "occupation", "occupation_letter_date",
            "payer_of_personal_expenditure", "payment_method",
            "process_status", "purpose", "repayment_schedule",
            "transaction_date", "transaction_sub_type", "transaction_type",
        )

class StatementOfOrgSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatementOfOrg
        fields = '__all__'

class PayeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payee
        fields = '__all__'

class ElectionActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ElectionActivity
        fields = '__all__'

class DonorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donor
        fields = '__all__'

class CommitteesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommitteesList
        fields = '__all__'

class CommitteeHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CommitteeHistory
        fields = '__all__'

class BallotsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ballots
        fields = '__all__'

class ContributorBreakdownSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContributorBreakdown
        fields = '__all__'

class ElectionCyclesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElectionCycles
        fields = '__all__'

class TotalContributionsYearlySerializer(serializers.ModelSerializer):

    class Meta:
        model = TotalContributionsYearly
        fields = '__all__'

class TotalContributionsMonthlySerializer(serializers.ModelSerializer):

    class Meta:
        model = TotalContributionsMonthly
        fields = '__all__'

class TotalContributionsRawInStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TotalContributionsRawInState
        fields = '__all__'

class TotalContributionsRawMonthRaceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TotalContributionsRawMonthRaceType
        fields = '__all__'

class SpendingBreakdownSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpendingBreakdown
        fields = '__all__'
