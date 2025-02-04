# entrypoint.sh
#!/bin/sh
# Ativar o ambiente virtual (supondo que você criou um com o nome '.venv')
#source /vercel/.venv/bin/activate

# Executar a aplicação Flask
# O Vercel irá definir a variável de ambiente $PORT automaticamente
flask run --host=0.0.0.0
