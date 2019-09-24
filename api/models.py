from django.db import models

class oreStarData(models.Model):
    tran_id = models.IntegerField(null=True)
    original_id = models.IntegerField(null=True)
    tran_date = models.DateField(null=True)
    tran_status = models.CharField(max_length=200, null=True)
    filer = models.CharField(max_length=200, null=True)
    payee = models.CharField(max_length=200, null=True)
    subtype = models.CharField(max_length=200, null=True)
    amount = models.FloatField(null=True)
    agg_amount = models.FloatField(null=True)
    payee_id = models.IntegerField(null=True)
    filer_id = models.IntegerField(null=True)
    attest_by_name = models.CharField(max_length=200, null=True)
    attest_date= models.DateField(null=True)
    review_by_name = models.CharField(max_length=200, null=True)
    review_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    occptn_ltr_date = models.CharField(max_length=200, null=True)
    payment_text = models.CharField(max_length=200, null=True)
    purps_desc = models.CharField(max_length=200, null=True)
    intrst_rate = models.IntegerField(null=True)
    check_numb = models.IntegerField(null=True)
    trans_status_ind = models.NullBooleanField(null=True)
    file_by_name = models.CharField(max_length=200, null=True)
    file_date = models.DateField(null=True)
    addr_book_agent = models.CharField(max_length=200, null=True)
    book_type = models.CharField(max_length=200, null=True)
    title_txt = models.CharField(max_length=200)
    occptn_txt = models.CharField(max_length=200, null=True)
    emp_name = models.CharField(max_length=200, null=True)
    emp_city = models.CharField(max_length=200,null=True)
    emp_state = models.CharField(max_length=200, null=True)
    emploeed_ind = models.NullBooleanField(null=True)
    self_employee_ind = models.NullBooleanField(null=True)
    addr_line_1 = models.CharField(max_length=200, null=True)
    addr_line_2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.IntegerField(null=True)
    zipplus = models.IntegerField(null=True)
    county = models.CharField(max_length=200, null=True)
    purpose_code = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'OreStar Data Scrape'
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'

class election:
    candidates = [] #Reference to a list of all candidates that are apart of this election
    date_range = models.DateField
    pass

class candidate:
    candidates_firstname = models.CharField(max_length=200, null=True)
    candidates_lastname = models.CharField(max_length=200, null=True)
    contributions = [] #Reference to a list of contributions that this candidate collected
    pass

class contributor:
    contributor_firstname = models.CharField(max_length=200, null=True)
    contributor_lastname = models.CharField(max_length=200, null=True)
    contributions = [] # Reference to a list of all the contributions made by this contributor
    candidates = [] # List of all the candidates this contributor donated to
    pass

class campaign:
    candidate = [] #Reference to all the candidates in an elections
    elections = [] #Reference to all the elections
    contrinbutions = [] #Reference to all elections from this campaign
    pass

class contribution:
    election = [] #reference to the election
    candidate = [] #reference to the candidate
    contribution_id = models.IntegerField()
    amount = models.DecimalField()
    date = models.DateField()
    pass

class taxonomyTerms:
    amount_range = ['$0 - $50', '$50 - $250', '$250 - $500', '500+'] # make a selection field
    pass