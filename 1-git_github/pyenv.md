# Mostrar as versões de python instaladas
```
pyenv versions
```

# Instalar a versão específica
```
pyenv install 3.13.0
```

# Definir a versão global do python
```
pyenv global 3.12.1
```

# Definir a versão paga o projeto específico (ir primeiro na pasta do projeto)
```
pyenv local 3.12.1
```

# Desinstalar todas as bibliotecas instaladas (funciona no bash)
```
pip freeze | grep -v "^-e" | xargs pip uninstall -y
```

# Criar novo ambiente virtual para o projeto
```
python -m venv .venv
```

# Ativar ambiente virtual
## cmd  
```
.venv\Scripts\Activate
```

## Bash
```
source .venv\Scripts\Activate
```

# Desativar do ambiente virtual
```
deactivate
```