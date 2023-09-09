from django.core.management import BaseCommand
from main.models import Payments, Curse


class Command(BaseCommand):

    def handle(self, *args, **options):
        data = [
            {
                "user": "Mad",
                "pay_day": "2022-03-02",
                "pay_check": "True",
                "pay_summ": 333,
                "pay_way": "карта"
            }
        ]
        records = Payments.objects.all()
        records.delete()

        Pyments_for_create = []

        for item_product in data:
            Pyments_for_create.append(Payments(**item_product))

        Payments.objects.bulk_create(Pyments_for_create)
