# stalled

# # import django
#
# from django.core.management import BaseCommand
# import tablib
# from import_export import resources
# # from django.conf import settings
# #
# # settings.configure(DEBUG=True)
# # django.setup()
# from contacts.models import Contact
#
#
# contact_resource = resources.modelresource_factory(model=Contact)()
# dataset = tablib.Dataset(['', 'New contact'], headers=['id', 'name'])
# result = contact_resource.import_data(dataset, dry_run=True)
# print(result.has_errors())
#
# result = contact_resource.import_data(dataset, dry_run=False)
#
# print("OK")
#
# class Command(BaseCommand):
#     def add_arguments(self, parser):
#         parser.add_argument("import_contact", required=True)
#
#     def handle(self, campaign_id, **options):
#         campaign = Campaign.objects.get(pk=campaign_id)
#         xml = create_xml(campaign)
#         print(xml)
