# coding: utf-8
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self):
        pass
        # pega os ultimos 20 posts criados
        # pega os ultimos 5 tags criadas
        # pega os ultimos 5 authores criados
        # adiciona uma url padrão no settings localhost, quando for local, e www.douglasbastos.com.br no ambiente. (Talvez se alterar meu host não precisa separar por ambiente)
        # Use reverse para montar as urls
        # Criar os arquivos em um static qualquer para que eu possa pegar via wget quando o servidor estiver no ar.