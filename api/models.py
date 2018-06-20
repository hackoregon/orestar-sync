# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ballots(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=64, blank=True, null=True)
    party = models.CharField(max_length=4, blank=True, null=True)
    race = models.CharField(max_length=128, blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True)
    won = models.IntegerField()
    writein = models.IntegerField()
    year = models.CharField(max_length=4, blank=True, null=True)
    votes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ballots'


class CommitteeHistory(models.Model):
    committee_id = models.IntegerField(primary_key=True)
    committee_name = models.CharField(max_length=255, blank=True, null=True)
    committee_description = models.CharField(max_length=1024, blank=True, null=True)
    effective = models.DateField(blank=True, null=True)
    expiration = models.DateField(blank=True, null=True)
    filing_type = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'committee_history'


class CommitteesList(models.Model):
    id = models.IntegerField(primary_key=True)
    filer_name = models.CharField(max_length=255, blank=True, null=True)
    filer_description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'committees_list'


class Donor(models.Model):
    donor_id = models.IntegerField(primary_key=True)
    donor_name = models.CharField(max_length=255, blank=True, null=True)
    donor_address = models.CharField(max_length=255, blank=True, null=True)
    donor_type = models.CharField(max_length=32, blank=True, null=True)
    donor_cats = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'donor'


class ElectionActivity(models.Model):
    election = models.CharField(max_length=64, blank=True, null=True)
    committee_id = models.IntegerField(primary_key=True)
    active_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=8, blank=True, null=True)
    active_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'election_activity'


class Payee(models.Model):
    payee_id = models.IntegerField(primary_key=True)
    payee_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payee'


class StatementOfOrg(models.Model):
    committee_id = models.IntegerField(primary_key=True)
    committee_name = models.CharField(max_length=255, blank=True, null=True)
    candidate_address = models.CharField(max_length=255, blank=True, null=True)
    committee_acronym = models.CharField(max_length=32, blank=True, null=True)
    committee_address = models.CharField(max_length=255, blank=True, null=True)
    committee_campaign_phone = models.CharField(max_length=32, blank=True, null=True)
    committee_filing_effective_from = models.CharField(max_length=255, blank=True, null=True)
    committee_filing_type = models.CharField(max_length=10, blank=True, null=True)
    committee_pac_type = models.CharField(max_length=32, blank=True, null=True)
    election_office = models.CharField(max_length=255, blank=True, null=True)
    email_address = models.CharField(max_length=255, blank=True, null=True)
    employer = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=32, blank=True, null=True)
    home_phone = models.CharField(max_length=32, blank=True, null=True)
    mailing_address = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    party_affiliation = models.CharField(max_length=16, blank=True, null=True)
    treasurer_email_address = models.CharField(max_length=255, blank=True, null=True)
    treasurer_fax = models.CharField(max_length=32, blank=True, null=True)
    treasurer_home_phone = models.CharField(max_length=32, blank=True, null=True)
    treasurer_mailing_address = models.CharField(max_length=255, blank=True, null=True)
    treasurer_name = models.CharField(max_length=255, blank=True, null=True)
    treasurer_work_phone = models.CharField(max_length=32, blank=True, null=True)
    work_phone = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statement_of_org'


class TransactionDetails(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    payee_id = models.IntegerField(blank=True, null=True)
    donor_id = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    address_book_type = models.CharField(max_length=32, blank=True, null=True)
    agent = models.CharField(max_length=64, blank=True, null=True)
    aggregate = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    associations = models.CharField(max_length=2048, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    employer_name = models.CharField(max_length=255, blank=True, null=True)
    filed_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    occupation_letter_date = models.DateField(blank=True, null=True)
    payer_of_personal_expenditure = models.CharField(max_length=255, blank=True, null=True)
    payment_method = models.CharField(max_length=32, blank=True, null=True)
    process_status = models.CharField(max_length=32, blank=True, null=True)
    purpose = models.CharField(max_length=512, blank=True, null=True)
    repayment_schedule = models.CharField(max_length=128, blank=True, null=True)
    transaction_date = models.DateField(blank=True, null=True)
    transaction_sub_type = models.CharField(max_length=255, blank=True, null=True)
    transaction_type = models.CharField(max_length=32, blank=True, null=True)

    @property
    def total_amount(self):
        if self.amount.is_nan():
            return "not available"
        return self.amount

    @property
    def total_aggregate(self):
        if self.aggregate.is_nan():
            return "not available"
        return self.aggregate

    class Meta:
        managed = False
        db_table = 'transaction_details'


class Transactions(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    committee_id = models.IntegerField(blank=True, null=True)
    transaction_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    filer_committee = models.CharField(max_length=255, blank=True, null=True)
    contributor_payee = models.CharField(max_length=255, blank=True, null=True)
    transaction_subtype = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    @property
    def total_amount(self):
        if self.amount.is_nan():
            return "not available"
        return self.amount

    class Meta:
        managed = False
        db_table = 'transactions'


class ContributorBreakdown(models.Model):
    committee_id = models.IntegerField(primary_key=True)
    sum = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    filer_name = models.CharField(max_length=255, blank=True, null=True)
    donor_category = models.CharField(max_length=255, blank=True, null=True)
    ratio = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    election_cycle = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'contributor_breakdown'


class TotalContributionsMonthly(models.Model):
    committee_id = models.IntegerField(primary_key=True)
    sum = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    filer_name = models.CharField(max_length=255, blank=True, null=True)
    election_cycle = models.CharField(max_length=255, blank=True, null=True)
    month = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'total_contributions_raw_month'


class TotalContributionsYearly(models.Model):
    committee_id = models.IntegerField(primary_key=True)
    sum = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    filer_name = models.CharField(max_length=255, blank=True, null=True)
    election_cycle = models.CharField(max_length=255, blank=True, null=True)
    year = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'total_contributions_raw_year'


class ElectionCycles(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'election_cycles'

class TotalContributionsRaw(models.Model):
    sum = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    filer_name = models.CharField(max_length=255, blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    election_cycle = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'total_contributions_raw'

class TotalContributionsRawInState(models.Model):
    committee_id = models.IntegerField(primary_key=True)
    sum = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    filer_name = models.CharField(max_length=255, blank=True, null=True)
    election_cycle = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'total_contributions_raw_in_state'

class TotalContributionsRawMonthTotal(models.Model):
    id = models.IntegerField(primary_key=True)
    sum = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    election_cycle = models.CharField(max_length=255, blank=True, null=True)
    month = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    year = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'total_contributions_raw_month_total'

class TotalContributionsRawMonthRaceType(models.Model):
    id = models.IntegerField(primary_key=True)
    sum = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    election_cycle = models.CharField(max_length=255, blank=True, null=True)
    race_type = models.CharField(max_length=255, blank=True, null=True)
    month = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    year = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'total_contributions_raw_month_race_type'


class SpendingBreakdown(models.Model):
    sum = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    filer_name = models.CharField(max_length=255, blank=True, null=True)
    committee_id = models.IntegerField(primary_key=True)
    election_cycle = models.CharField(max_length=255, blank=True, null=True)
    spending_category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spending_breakdown'


class CommitteeContributors(models.Model):
    sum = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    contributor_payee = models.CharField(max_length=255, blank=True, null=True)
    filer_name = models.CharField(max_length=255, blank=True, null=True)
    election_cycle = models.CharField(max_length=255, blank=True, null=True)
    committee_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'committee_contributions'


class ContributorGraph(models.Model):

    class Meta:
        managed = False

class VoterAcquisitionCost(models.Model):
    voter_acquisition_cost = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    year = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    votes = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    election_cycle = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    election_cycle = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voter_acquisition_cost'

class CommitteeElectionCycle(models.Model):
    committee_name = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    committee_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'committee_election_cycle'
