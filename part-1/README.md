#### Part-1
This is my submission to DC-Team for `part-1`.

#### Challenge
Precisamos de uma API para receber a atualização de dados cadastrais de produtos. Ela deve receber um corpo no formato JSON, onde o tamanho varia desde alguns poucos Kb até alguns Gb.
Experiências anteriores mostram que alguns clientes costumam enviar o mesmo corpo repetidas vezes ao longo de um curto espaço de tempo.
Isso nos causou alguns problemas, como o fato de ter que escalar nossos bancos de dados muito além do necessário afim de aguentar a carga extra desnecessária.
Para evitar que isto ocorra, precisamos que esta API negue requisições que tem o mesmo corpo num intervalo de 10 minutos.

Aqui está um exemplo do comportamento esperado:
```bash
# 2018-03-01T13:00:00 - primeira requisição, durante 10 minutos requests com o mesmo corpo serão negadas
curl -XPOST http://your-api.chaordic.com.br/v1/products -d '[{"id": "123", "name": "mesa"}]' #=> 200 OK

# 2018-03-01T13:09:59 - mesmo corpo que a request anterior.
curl -XPOST http://your-api.chaordic.com.br/v1/products -d '[{"id": "123", "name": "mesa"}]' #=> 403 Forbidden

# 2018-03-01T13:10:00 - agora a API deve voltar a aceitar o corpo
curl -XPOST http://your-api.chaordic.com.br/v1/products -d '[{"id": "123", "name": "mesa"}]' #=> 200 OK
```
Como esta API atenderá milhares de requisições simultâneas, ela precisa funcionar em um cluster.
É esperado que o comportamento descrito acima se mantenha, independente do nó que receber a requisição.

### Dependencies
- docker
- docker-compose
- *Python 3.5
- *Redis 6.0.6

>*provide in docker container

### Setup
To start the project, just run the command bellow:

```bash
$ docker-composer up -d
```

This command provide a Docker container with the application (API and Cache Server).
After start, the address `http://localhost:5000/v1/products` is available for HTTP Post method.

### Solution
First, we order the body content (JSON) received on route `/v1/products`,
then we make a hash string using `sha1` algoritme. With this value, so check
in the Cache Server by the value of the hash. The registers expires in 10min.

### Test
To run the unit tests, just run the command bellow:

```bach
$ python3 -m unittest
```

#### LAUS DEO ∴
