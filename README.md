# Requirements

**Note: Following steps are for Ubuntu/Debian**

1. `sudo apt-get install g++ libxrandr-dev libfox-1.6-dev python-pip`
2. `pip install pipenv`
3. Add `$HOME/.local/bin` to PATH
4. `pipenv install`

# Exporting the model to frozengraph format

`aocr export --format=frozengraph ./exported-model-frozen`

# Starting the server

**Note: you need to have a frozengraph model inside `./exported-model-frozen` from the previous step**

`FLASK_APP=app.py pipenv run flask run`

# API

`POST /predict`

## Params

Encoding: `form-data`

name | description
------ |----
`file` | PNG/JPG/GIF file with the text image


## Request:

```
curl --request POST \
  --url http://localhost:5000/predict \
  --form file=@local_file.png
```

## Response

```json
{
    "text": "Some recognized text"
}
```





