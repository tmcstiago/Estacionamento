from django.db import models
import math

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    segundo_nome = models.CharField(max_length=100)    
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Marca(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    proprietario = models.ForeignKey(Pessoa, on_delete = models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=7)
    cor = models.CharField(max_length=15)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.modelo + ' - ' + self.placa


class Parametro(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        resposta =  'Valor por hora: R$ ' + str(self.valor_hora)
        resposta += '  -  Valor por mês: R$ ' + str(self.valor_mes)
        return resposta 
    

class MovRotativo(models.Model):
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, blank=True, null=True)
    valor_hora = models.ForeignKey(Parametro, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)

    def horas_total(self):
        return math.ceil((self.checkout - self.checkin).total_seconds()/3600)
    
    def total(self):
        return self.valor_hora.valor_hora * self.horas_total()

    def __str__(self):
        return self.veiculo.modelo + '  -  ' + self.veiculo.placa


class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    inicio = models.DateField()
    valor_mes = models.ForeignKey(Parametro, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.veiculo) + '  -  R$ ' + str(self.valor_mes.valor_mes)


class MovMensalistas(models.Model):
    mensalista = models.ForeignKey(Mensalista, on_delete=models.CASCADE)
    data_pagamento = models.DateField()
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.mensalista) + '  -  R$' + str(self.total)