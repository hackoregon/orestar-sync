from django.core.management.base import BaseCommand
from ..models import Transactions

class Command(BaseCommand):
    help = 'Selenium Based Scrapper for OreStar'

    def handle(self, *args, **kwargs):
        