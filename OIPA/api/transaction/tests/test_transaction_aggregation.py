
from django.test import TestCase
from iati.factory import iati_factory
from iati.transaction import factories as transaction_factory
from rest_framework.test import APIClient
from decimal import Decimal

class ActivityAggregationTestCase(TestCase):
    def setUp(self):
        """set up 2 activities with the shown specs

        then create individual tests to check most used aggregation / group by combinations.

        activity 1
            id - IATI-0001
            sectors
                sector 1
                    code        - 11000
                    name        - Sector 1
                    percentage  - 100
            recipient countries
                country 1
                    code        - AD
                    name        - Andorra
                    percentage  - 50
            budgets
                budget 1
                    value       - 20000
                budget 2
                    value       - 50000
            transactions
                transaction 1
                    type        - incoming funds
                    value       - 50000

        activity 2
            id - IATI-0002
            sectors
                sector 1
                    code        - 11000
                    name        - Sector 1
                    percentage  - 50
                sector 2
                    code        - 11001
                    name        - Sector 2
                    percentage  - 50
            recipient countries
                country 1
                    code        - AD
                    name        - Andorra
                    percentage  - 50
                country 2
                    code        - KE
                    name        - Kenya
                    percentage  - 50
            budgets
                budget 1
                    value       - 80000
            transactions
                transaction 1
                    type        - incoming funds
                    value       - 10000
                transaction 1
                    type        - incoming funds
                    value       - 25000

        """

        first_activity = iati_factory.ActivityFactory.create()
        second_activity = iati_factory.ActivityFactory.create(
            id='IATI-0002',
            iati_identifier='IATI-0002',
            iati_standard_version=first_activity.iati_standard_version)

        # transaction type = 1 (incoming funds), works the same for disbursements etc.
        first_transaction = transaction_factory.TransactionFactory.create(
            activity=first_activity,
            value=50000)
        second_transaction = transaction_factory.TransactionFactory.create(
            activity=second_activity,
            value=10000,
            transaction_type=first_transaction.transaction_type)
        third_transaction = transaction_factory.TransactionFactory.create(
            activity=second_activity,
            value=25000,
            transaction_type=first_transaction.transaction_type)

        first_sector = iati_factory.SectorFactory.build(code=11000, name='Sector 1')
        second_sector = iati_factory.SectorFactory.build(code=11001, name='Sector 2')

        # TODO: Create appropraite objects here - 2016-04-18
        transaction_sector = transaction_factory.TransactionSectorFactory.create(
            transaction=first_transaction,
            sector=first_sector,
            percentage=100
        )
        transaction_factory.TransactionSectorFactory.create(
            transaction=second_transaction,
            sector=first_sector,
            percentage=50,
            vocabulary=transaction_sector.vocabulary
        )
        transaction_factory.TransactionSectorFactory.create(
            transaction=third_transaction,
            sector=first_sector,
            percentage=50,
            vocabulary=transaction_sector.vocabulary
        )
        transaction_factory.TransactionSectorFactory.create(
            transaction=second_transaction,
            sector=second_sector,
            percentage=50,
            vocabulary=transaction_sector.vocabulary
        )
        transaction_factory.TransactionSectorFactory.create(
            transaction=third_transaction,
            sector=second_sector,
            percentage=50,
            vocabulary=transaction_sector.vocabulary
        )

        country = iati_factory.CountryFactory.build(code="AD", name="Andorra")
        second_country = iati_factory.CountryFactory.build(code="KE", name="Kenya")

        transaction_factory.TransactionRecipientCountryFactory.create(
            transaction=first_transaction,
            country=country,
            percentage=100
        )
        transaction_factory.TransactionRecipientCountryFactory.create(
            transaction=second_transaction,
            country=country,
            percentage=50
        )
        transaction_factory.TransactionRecipientCountryFactory.create(
            transaction=third_transaction,
            country=country,
            percentage=50
        )
        transaction_factory.TransactionRecipientCountryFactory.create(
            transaction=second_transaction,
            country=second_country,
            percentage=50
        )
        transaction_factory.TransactionRecipientCountryFactory.create(
            transaction=third_transaction,
            country=second_country,
            percentage=50
        )

        self.api_client = APIClient()

    def get_results(self, group_by, aggregations, order_by):
        url = ''.join([
            '/api/transactions/aggregations/?format=json&group_by=',
            group_by,
            '&aggregations=',
            aggregations,
            '&order_by=',
            order_by
        ])
        response = self.api_client.get(url)

        return list(response.data['results'])


    def test_sector_incoming_fund_group_by(self):
        """group incoming funds by sector, this is the non percentage aware sector aggregation

        expected results:
            sector 11000 = 85000 (50000 + 10000)
            sector 11001 = 35000 (10000 + 25000
        """
        results = self.get_results(
            group_by='sector',
            aggregations='incoming_fund',
            order_by='sector')

        self.assertTrue(len(results) == 2)
        self.assertEqual(results[0]['incoming_fund'], Decimal(85000))
        self.assertEqual(results[1]['incoming_fund'], Decimal(35000))

    def test_recipient_country_incoming_fund_group_by(self):
        """group incoming fund by recipient country, this is the non percentage aware sector aggregation

        expected results:
            country AD = 85000 (50000 + 10000 + 25000)
            country KE = 35000 (10000 + 25000)
        """
        results = self.get_results(
            group_by='recipient_country',
            aggregations='incoming_fund',
            order_by='recipient_country')

        self.assertTrue(len(results) == 2)
        self.assertEqual(results[0]['incoming_fund'], Decimal(85000))
        self.assertEqual(results[1]['incoming_fund'], Decimal(35000))
