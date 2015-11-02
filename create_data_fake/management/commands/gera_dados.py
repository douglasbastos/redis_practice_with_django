# coding: utf-8
from django.core.management.base import BaseCommand
from model_mommy import mommy
from create_data_fake.views import generator_string_by_range
# from optparse import make_option


class Command(BaseCommand):

    # option_list = BaseCommand.option_list + (
    #     make_option('--long', '-l', dest='long',
    #                 help='Help for the long options'),
    # )
    def add_arguments(self, parser):
        parser.add_argument('-m', dest='model',
                            default='', help='Select model for includes data automatic (Tag, User or Post)')
        parser.add_argument('-q', dest='quantity',
                            default='', help='Set quantity of inserted items')

    def generate_tags(self):
        from acrux_blog.models import Tag
        for i in range(0, self.quantity):
            mommy.make(Tag, name=generator_string_by_range(min=4, max=15))

    def handle(self, **options):
        self.model = options['model']
        self.quantity = int(options['quantity'])

        self.generate_tags()


        import ipdb; ipdb.set_trace()