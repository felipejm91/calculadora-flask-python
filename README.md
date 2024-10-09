# calculadora-flask-python


  Calculadora para operações aritméticas básicas; desenvolvida com HTML, CSS, Flask, Python E Docker. Esse projeto tem como finalidade, implantar todos os conhecimentos básicos adquiridos durante os estudos das ferramentas citadas. 

  Repositório do Github já conta com uma pipeline de automatização de CI, para que seja feito o upload automático de uma nova versão da aplicação para o repositório do Docker Hub.
  
  Aplicação foi configurada em um cluster kubernetes no ambiente do Google Cloud(GKE) e configurado o acesso através dop domínio "calc.felipemeneguetti.com.br" e implantado segurança de SSL/TLS. 
  
 

----------------------------------


**INSTRUÇÕES DE EXECUÇÃO**


**>Execução local**

  --REQUISITOS DA APLICAÇÃO
  
    Python 3
    Python3-Pip

  1º) Clone do repositório
      
      git clone https://github.com/felipejm91/calculadora-flask-python.git
      
  2º) Instalação dos requisitos
  
      **OBS: Dentro do diretório da aplicação**
      
      pip install -r requeriments.txt
      
  3º) Execução da aplicação
    
      python3 app.py
      
  4º) Acesso à aplicação
       
      127.0.0.1:5000
               
      
 **>Execução em Container**
 
 
    --REQUISITOS DA APLICAÇÃO
    
      Docker
      
    --Executar o comando para criação do container
      
      docker run -d -p 5000:5000 felipejm91/calculadora-flask-python
      
      
