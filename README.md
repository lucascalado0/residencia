# Sistema Integrado para Gerenciamento e Resposta a Incidentes de Segurança

### Equipe 3

## Instalação
Para utilizar o sistema, é necessário iniciar o backend em python e o frontent em React

### Iniciando o Backend
Este projeto utiliza Python como linguagem principal para a construção do back-end.

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

* `pip install -r requiremtents.txt`
* * Se não for possível instalar as bibliotecas, talvez seja necessário iniciar um venv python. Para isso, siga os passos abaixo:
* * - Ainda no diretório raiz do backend, escreva o seguinte comando: `python -m venv venv`
* * - Com isso, você verá que uma pasta `venv`será criada dentro de `/backend/`.
* * - - Se você estiver no Linux rode o seguinte comando: `source venv/bin/activate` e tente usar o `pip install...` acima novamente.
* * - - Se estiver no windows use `./venv/Scripts/activate` e tente usar o `pip install...` acima novamente.
* Após todas as bibliotecas instaladas, rode o seguinte comando:
* `python run.py`
* Tudo certo, você verá que o backend já está rodando no localhost, porta 5000

### Iniciando o Frontend
Este projeto utiliza React.js como biblioteca principal para construção da interface de usuário, biblioteca JavaScript amplamente utilizada para criar interfaces dinâmicas, escaláveis e baseadas em componentes reutilizáveis.

Para iniciar o frontend, é necessário realizara a seguinte tarefa: 
* Abrir terminal
* Dentro do terminal observe a pasta em que o mesmo se encontra e localize o caminho para o diretório frontend
* Digite o comando 'cd frontend' no terminal para acessar o diretório
* Com o terminal no diretório frontend, digite o comando `npm install` para instalar as dependências necessárias
* Por fim, digite o comando `npm run dev` para inicial o frontend