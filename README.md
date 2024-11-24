# Sistema Integrado para Gerenciamento e Resposta a Incidentes de Segurança

### Equipe 3

## Instalação
Para utilizar o sistema, é necessário inicial o backend em python e o frontent em React

### Iniciando o Backend
Antes de iniciar o backend, é preciso ter uma instância do TheHive, Cortex e MISP rodando.
Após se certificar de que os 3 serviços estão prontos, é preciso criar o arquivo `.env` dentro da pasta `backend`.

Dentro do arquivo é preciso adicionar as seguintes variáveis: 
* `THEHIVE_URL=[adicionar a url correspondente do thehive]`
* `THEHIVE_USERNAME=[adicionar o username do adm da organisation no thehive]`
* `THEHIVE_PASSWORD=[adicionar a password do usuario adm da organisation no thehive]`
* `MONGO_URI=[adicionar o valor da URI de conexao ao mongoDB]`

Essas são as variáveis de ambiente necessárias para que o backend funcione corretamente.

Feito isso, é hora de instalar as dependências.
* Abra um novo terminal
* Dentro do terminal, certifique-se de que você se encontra na pasta raiz do backend
* Confirmando de que está no diretório correto, escreva o seguinte comando e pressione Enter:

* `pip -r install requiremtents.txt`
* Após todas as bibliotecas instaladas, rode o seguinte comando:
* `python run.py`
* Tudo certo, você verá que o backend já está rodando no localhost, porta 5000

### Iniciando o Frontend