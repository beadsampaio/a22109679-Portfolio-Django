from django.db import models

# Create your models here.


class Educacao(models.Model):
    tipo_formacao = models.CharField(max_length=40)
    curso = models.CharField(max_length=40)
    local = models.CharField(max_length=20)
    periodo = models.CharField(max_length=30)
    logotipo = models.ImageField(upload_to='static/portfolio/images')

    def __str__(self):
        return self.tipo_formacao[:50]


class Pessoa(models.Model):
    nome = models.CharField(max_length=40)
    link_lusofona = models.CharField(max_length=1000, null=True, blank=True)
    link_linkedin = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.nome[:50]


class Tecnologia(models.Model):
    nome = models.CharField(max_length=80)
    acronimo = models.CharField(max_length=10, blank=True)
    anoCriacao = models.IntegerField()
    criador = models.CharField(max_length=80)
    logotipo = models.ImageField(upload_to='static/portfolio/images')
    link_site = models.CharField(max_length=1000, null=True, blank=True)
    descricao = models.TextField(max_length=1000)

    def __str__(self):
        return self.nome[:50]


class Projeto(models.Model):
    titulo = models.CharField(max_length=80)
    descricao = models.CharField(max_length=500)
    imagem = models.ImageField(upload_to='static/portfolio/images', blank=True)
    ano_realizacao = models.IntegerField()
    participantes = models.ManyToManyField(Pessoa, blank=True)
    link_github = models.CharField(max_length=1000, null=True, blank=True)
    link_youtube = models.CharField(max_length=1000, null=True, blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    def __str__(self):
        return self.titulo[:50]


class Cadeira(models.Model):
    nome = models.CharField(max_length=40)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=2)
    ects = models.IntegerField()
    ano_letivo = models.CharField(max_length=20)
    topicos_abordados = models.TextField()
    ranking = models.IntegerField()
    docente_teorica = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    docentes_praticas = models.ManyToManyField(Pessoa, related_name='professor_pratica')
    link_cadeira = models.CharField(max_length=1000)
    linguagens = models.ManyToManyField(Tecnologia, blank=True)
    projetos = models.ManyToManyField(Projeto, blank=True)

    def __str__(self):
        return self.nome[:50]


class Competencia(models.Model):
    titulo = models.CharField(max_length=20)
    descricao = models.TextField(max_length=1000)
    projetos = models.ManyToManyField(Projeto, blank=True)
    cadeira = models.ManyToManyField(Cadeira, blank=True)

    def __str__(self):
        return self.titulo[:50]


class Lingua(models.Model):
    nome = models.CharField(max_length=30)
    nivel = models.CharField(max_length=30)
    explicacao = models.TextField(max_length=500)

    def __str__(self):
        return self.nome[:50]


class Interesse(models.Model):
    titulo = models.CharField(max_length=40)
    descricao = models.TextField(max_length=1000)
    imagem = models.ImageField(upload_to='static/portfolio/images')
    link = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.titulo[:50]


    #TFC

class TFC(models.Model):
    titulo = models.CharField(max_length=80)
    autor = models.ManyToManyField(Pessoa, related_name='autor')
    orientador = models.ManyToManyField(Pessoa, related_name='orientador')
    anoRealizacao = models.IntegerField()
    sumario = models.CharField(max_length=500)
    link_relatorio = models.CharField(max_length=1000)
    link_github = models.CharField(max_length=1000, null=True, blank=True)
    link_youtube = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.titulo


    # PROGRAMAÇÃO WEB
class Laboratorio(models.Model):
    titulo = models.CharField(max_length=80)
    descricao = models.TextField(max_length=1000)
    link = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.titulo[:50]


class Tecnologiawebsite(models.Model):
    nome = models.CharField(max_length=80)
    acronimo = models.CharField(max_length=10, blank=True)
    anoCriacao = models.IntegerField()
    criador = models.CharField(max_length=80)
    logotipo = models.ImageField(upload_to='static/portfolio/images')
    codigo = models.ImageField(upload_to='static/portfolio/images')
    link = models.CharField(max_length=1000, null=True, blank=True)
    descricao = models.TextField(max_length=1000)

    def __str__(self):
        return self.nome[:50]


