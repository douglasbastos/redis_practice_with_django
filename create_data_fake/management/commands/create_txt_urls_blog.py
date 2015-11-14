# coding: utf-8
from django.core.management.base import BaseCommand
from django.core.urlresolvers import reverse
from django.conf import settings
from acrux_blog.models import Post, Tag
from acrux_blog.views import Base


class Command(BaseCommand):

    def handle(self, **options):
        base = Base()

        posts = Post.objects.all()[::-1][:20]
        tags = Tag.objects.all()[::-1][:5]
        authors = base.authors_with_post[:5]

        with open('urls_blog.txt', 'w') as urls,\
                open('urls_blog_with_cache.txt', 'w') as urls_cache:

            index = '{}{}'.format(settings.DOMAIN, reverse('page_index'))
            index_cache = '{}{}'.format(settings.DOMAIN, reverse('page_index_cache'))
            urls.write(index+'\n')
            urls_cache.write(index_cache+'\n')

            for i in range(2, 4):
                urls.write('{}?page={}\n'.format(index, i))
                urls_cache.write('{}?page={}\n'.format(index_cache, i))

            print 'Armazenando home'

            for post in posts:
                urls.write('{}{}\n'.format(settings.DOMAIN, reverse('post', kwargs={'slug': post.slug})))
                urls_cache.write('{}{}\n'.format(settings.DOMAIN, reverse('post_cache', kwargs={'slug': post.slug})))
            print 'Armazenamento de link com post OK'

            for tag in tags:
                urls.write('{}{}\n'.format(settings.DOMAIN, reverse('tags_posts', kwargs={'tag': tag.slug})))
                urls_cache.write('{}{}\n'.format(settings.DOMAIN, reverse('tags_posts_cache', kwargs={'tag': tag.slug})))
            print 'Armazenamento de link com tag OK'

            for author in authors:
                urls.write('{}{}\n'.format(settings.DOMAIN, reverse('author_posts', kwargs={'author': author.username})))
                urls_cache.write('{}{}\n'.format(settings.DOMAIN, reverse('author_posts_cache', kwargs={'author': author.username})))
            print 'Armazenamento de link com author OK'
        print 'FIM'


