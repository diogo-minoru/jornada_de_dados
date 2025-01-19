# Configurar o git
### Definir nome do usuário
```
git config --global user.name "Diogo Minoru"
```
### Definir email do usuário
```
git config --global user.email "diogominoru@hotmail.com"
```

### Mostrar configurações
```
git config --global --list
```

# Comandos Git Bash

### Inicializando o Repositório
```
git init
```

### Criar pasta
```
mkdir "nome"
```

### Criar arquivo
```
touch main.py
```

### Verificar o estado do repositório para ver como o Git está reconhecendo o arquivo
```
git status
```

### Adicionar esse arquivo ao Git para que ele comece a ser rastreado
```
git add main.py

git add .
```
### Remover o arquivo do stage
```
git restore --staged main.py
```

### Realizar o commit
```
git commit -m "descrição"
```

### Restaurar arquivo no estado do último commit
```
git restore main.py
```

### Log de commits
```
git log
```