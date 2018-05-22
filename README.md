# TAKWIMU

The TAKWIMU web platform powering insight from human development indicators. Helping to find the stories behind the data. Accessible at https://takwimu.africa/

## Background

TODO

---

## Development

## Development

1. Clone the repo
2. ``cd TAKWIMU``
3. ``virtualenv --no-site-packages env``
4. ``source env/bin/activate``
5. ``pip install -r requirements.txt``


***NB:** The set up docs from here assume setting up HURUmap Kenya but is applicable to the rest of the projects.*

You will need a Postgres database:

```
psql
create user takwimu with password takwimu;
create database takwimu;
grant all privileges on database takwimu to takwimu;
```

Run migrations to keep Django happy:
```
python manage.py migrate
```

Import the data into the new database (will overwrite some tables created by Django, but that's ok).
```
cat takwimu/sql/*.sql | psql -U takwimu -W takwimu
```

Start the server:
```
python manage.py runserver
```

### Landing Page

The landing page for TAKWIMU currently lives in the `/docs` folder hosted on Github Pages, powered by Jekyll. This will be fully replaced with actual platform documentation.

### Web Platform

TODO

## Tests

TODO

## Deployment

TODO

---


## Contributing

If you'd like to contribute to TAKWIMU, check out the [CONTRIBUTING.md](CONTRIBUTING.md) file on how to get started.

## Attribution

TAKWIMU has been made possible thanks to:

- Consortium Members:
    - @africapractice
    - @CodeForAfrica
    - @iHub
- Contributors:
    - ?
- Technologies:
    - ?

---

## License

MIT License

Copyright (c) 2018 africapractice, Code for Africa, iHub

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

All content is released under a [Creative Commons 4 Attribution license](https://creativecommons.org/licenses/by/4.0/). If you use this software, please provide attribution to TAKWIMU, africapractice, Code for Africa, and iHub.
