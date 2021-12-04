# Decifra AES-128 ECB

-  ## Tecnologias Utilizadas

### Backend:

> + cryptography: disponibiliza código de alto nível e interfaces de baixo nível para algoritmos criptográficos comuns, como cifras simétricas, resumos criptográficos de mensagens e funções de derivação de chaves. [1]
>> Utilizado para cifrar e decifrar bytes com AES-128 ECB.
> + Flask: É um *framework* leve de aplicações web com Python. Projetado para tornar o desenvolvimento rápido e fácil, com a capacidade de escalar para aplicações mais complexas. [2]
>> Utilizado para disponibilizar a interface gráfica da aplicação.

### Frontend:
> + Jinja: É um mecanismo de modelos rápido e extensível, que permite substituir *placeholders* com código semelhante a Python. [4]
>> Utilizado para gerar a interface gráfica web.
> + Axios: É um cliente *HTTP* baseado em promessas para o navegador. [5]
>> Utilizado para realizar as chamadas *HTTP* *client-side* para a *API* *server-side* da aplicação.

-  ## Dificuldades Encontradas

> Falta de conhecimento sobre o framework Flask no desenvolvimento do *backend* da aplicação, resolvido após assistir alguns tutoriais no YouTube e leitura da documentação.

> Falta de conhecimento sobre chamadas HTTP no desenvolvimento *frontend*, resolvido após encontrar o *client* Axios e ler sua documentação.

### Utilização do Endpoint de Teste
> 1. Preencher o nome do arquivo com extensão .py
> 2. Preencher o link do arquivo com http://localhost:5000/api/test
> 3. Preencher a senha do arquivo com abcdefghijklmnop
> * Só são permitidas senhas UTF-8 com 16 caracteres (16 bytes -> 128 bits)
> 4. Clicar em Decifrar

### Referências

1. [cryptography](https://cryptography.io/)
2. [Flask](https://flask.palletsprojects.com/)
3. [Jinja](https://jinja.palletsprojects.com/)
4. [Axios](https://axios-http.com/docs/intro)
