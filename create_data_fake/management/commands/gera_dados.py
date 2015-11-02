# coding: utf-8
from django.core.management.base import BaseCommand
from model_mommy import mommy
from random import choice
from create_data_fake.views import generator_string_by_range
from django.contrib.auth.models import User
from acrux_blog.models import Tag, Post
from create_data_fake import content
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
        for i in range(0, self.quantity):
            mommy.make(Tag, name=generator_string_by_range(min=4, max=15, space=True))

    def generate_users(self):
        for i in range(0, self.quantity):
            mommy.make(User, username=generator_string_by_range())

    def generate_posts(self):
        for i in range(0, self.quantity):
            titulo = generator_string_by_range(min=25, max=55, space=True)
            text = choice([content.alan_turing, content.george_boole])
            author = choice(User.objects.all()[:50])
            tag = choice(Tag.objects.all())
            mommy.make(Post, title=titulo, content=text, author=author, tag=tag)

    def handle(self, **options):
        self.model = options['model']
        self.quantity = int(options['quantity'])

        self.generate_posts()
