#Imagem base que será utilizada
FROM python:3

#Diretório da aplicação
WORKDIR /app

#Copia arquivos ou diretórios para o Workdir
COPY ./requeriments.txt /app

#Instala dependências da aplicação
RUN pip install -r ./requeriments.txt

#Copia restante dos arquivos para o diretório
COPY . .

#Expõe a porta que o container irá escutar
EXPOSE 5000

#Executa comando para colocar o serviço em funcionamento
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
