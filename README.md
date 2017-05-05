# Social Web Service
Código fonte de um microserviço que busca informações do Facebook de um usuário logado. 

O código teve como base os seguintes tutoriais:

1) [How to Implement OAuth2 using Django REST Framework](https://chrisbartos.com/articles/how-to-implement-oauth2-using-django-rest-framework/)
2) [Django rest-framework Social Oauth2](https://github.com/PhilipGarnero/django-rest-framework-social-oauth2)

## USO:

### CONFIGURAÇÃO DA APLICAÇÃO:

1) Acesso o Django Admin: http://localhost:8000/admin
2) Crie uma nova applicação (add a New Application)
3) client_id e client_secret não deve ser modificado 
4) redirect_uris deve ficar em branco 
5) client_type setado como To confidential
6) authorization_grant_type setado como 'Resource owner password-based'
7) O campo name pode ser qualquer um que desejar. 

### ETAPAS DO USO:

Não é adequado que o usuário envie o token do facebook sempre que quiser acessar um recurso. Para isso, o serviço armazena o token do facebook e envia um token próprio da aplicação para acessar recursos da microserviço 

A converção do token do facebook para o token da aplicação é feita da seguinte forma: 

```
curl -X POST -d "grant_type=convert_token&client_id=<CLIENT_ID_DJANGO>client_secret=<CLIENT_SECRET_DJANGO>&backend=facebook&token=<TOKEN_USER_FACEBOOK>" http://localhost:8000/auth/convert-token
```

O retorno dessa requisição é dessa forma: 

```
{"refresh_token":"<REFRESH_TOKEN>","expires_in":36000,"token_type":"Bearer","scope":"read write","access_token":"<ACCESS_TOKEN>"}
```
Esse novo ACCESS_TOKEN é utilizado para acessar os recursos do serviço. Veja um exemplo de acesso:

```
curl -H "Authorization: Bearer <ACCESS_TOKEN>" -X GET http://localhost:8000/facebook/me/

```
Dessa forma, o usuário pode obter dados do facebook. 
## DICAS
