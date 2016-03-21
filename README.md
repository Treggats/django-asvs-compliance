Django ASVS compliance
======================

A application to support developers making [ASVS](https://owasp.org/index.php/ASVS) compliant applications.

## Installation

This application uses postgresql as a database, create a database by running

`createdb asvs_compliance`

create `conf/secrets.json` with the following contents
```javascript
{
  "secret_key": "13hrn^p9lf_jcumy^s8d!t@55d**cp@^nxsm_bvcpl&7a8+_8%",
  "db_name": "asvs_compliance",
  "db_user": "bobby",
  "db_password": "Hard to guess"
}
 ```
change the values accordingly.

Create a virtual environment and run

`pip install -r requirements.txt`

Create the database tables by running

`./manage.py migrate`

Create a superuser to use the admin environment

`./manage.py createsuperuser`

## Load the data

There is a json file present which can be used to load the ASVS Requirement data, run
`./manage.py loadasvsdata --file asvsrequirement/management/helpers/asvs.json --type version`
`./manage.py loadasvsdata --file asvsrequirement/management/helpers/asvs.json --type level`
`./manage.py loadasvsdata --file asvsrequirement/management/helpers/asvs.json --type category`
`./manage.py loadasvsdata --file asvsrequirement/management/helpers/asvs.json --type requirement`

In order to load the data for ASVS Annotation, you need to clone the owasp-aasvs repository.
After that you can run
`./manage.py loadaasvsdata --file asvsannotation/management/helpers/aasvs.json`

`./manage.py loadaasvsdata --dir <pathto>/owasp-aasvs/src/help`

## References

* https://owasp.org/index.php/ASVS
* https://github.com/ibuildingsnl/owasp-aasvs
