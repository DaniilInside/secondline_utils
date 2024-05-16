**Запуск (Ubuntu)**

Клоним репозиторий
```git clone https://github.com/DaniilInside/secondline_utils.git```

Переходим в репу
```cd ./secondline_utils```

Билдим
```docker build -t secondline_utils .```

Запускаем контейнер на порту 2283 и прокидываем volum на нашу репу
```docker run -d --name secondline_utils -p 2283:2283 -v путь/до/репозитория/secondline_utils:/app secondline_utils```
