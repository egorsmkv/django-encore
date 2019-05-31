# Example app

First, install frontend dependencies by yarn:

```
yarn install
```

Second, compile assets:

```
# compile assets once
yarn encore dev

# or, recompile assets automatically when files change
yarn encore dev --watch

# on deploy, create a production build
yarn encore production
```

Third, install backend dependencies by pipenv:

```
pipenv install
pipenv shell # to shell with virtual environment
```

Fourth, start django webserver:

```
python ./manage.py runserver
```
