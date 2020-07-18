from django import forms
from django.core.mail.message import EmailMessage

#Criando formulário de contato

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget= forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema django2',
            body=conteudo,
            from_email='jacksonrodrigues4049@gmail.com',
            to=['jacksonrodrigues405@gmail.com'],
            headers={'Reply-To': email}

        )
        mail.send()
         
        nomes = ['Jackson']
        print([print(nome) for nome in nomes])
