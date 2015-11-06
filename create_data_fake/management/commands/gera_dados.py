# coding: utf-8
import sys
from django.core.management.base import BaseCommand
from model_mommy import mommy
from random import choice
from create_data_fake.views import generator_string_by_range
from django.contrib.auth.models import User
from acrux_blog.models import Tag, Post
from ranking_real_time.models import Player
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

    def logger(self, atual, total):
        sys.stdout.write('Criando {} de {}\r'.format(atual, total))
        sys.stdout.flush()

    def generate_tags(self):
        for i in range(0, self.quantity):
            mommy.make(Tag, name=generator_string_by_range(min=4, max=15, space=True))
            self.logger(i+1, self.quantity)

    def generate_users(self):
        for i in range(0, self.quantity):
            user = mommy.make(User, username=generator_string_by_range())
            mommy.make(Player, username=user, pontos=1000)
            self.logger(i+1, self.quantity)

    def generate_posts(self):
        for i in range(0, self.quantity):
            titulo = generator_string_by_range(min=25, max=55, space=True)
            text = choice([content.alan_turing, content.george_boole])
            author = choice(User.objects.all()[:50])
            tag = choice(Tag.objects.all())
            mommy.make(Post, title=titulo, content=text, author=author, tag=tag)
            self.logger(i+1, self.quantity)

    def handle(self, **options):
        model = options['model']
        self.quantity = int(options['quantity'])

        if model == 'User':
            self.generate_users()
        elif model == 'Tag':
            self.generate_tags()
        elif model == 'Post':
            self.generate_posts()
        else:
            print 'Model not found'
        print 'Todos registros cadastrados com sucesso'
