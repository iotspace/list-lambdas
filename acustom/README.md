```
pipenv install
pipenv shell
```


```
python list_lambdas.py

python list_lambdas.py --csv lambdas_list.csv

python lambdas_report.py --csv lambdas_report.csv
```

```
python list_lambdas.py --token-key-id AKIA4GQUY4HCYNJJXXXX --token-secret s6VgVue62rU+5BtIkpPcTd/vsgZHD+g4nFmvXXXX
```

Save results to CSV file
```
python list_lambdas.py --token-key-id AKIA4GQUY4HCYNJJXXXX --token-secret s6VgVue62rU+5BtIkpPcTd/vsgZHD+g4nFmvXXXX --csv lambda_list.csv
```


https://gist.github.com/gene1wood/ad9083866a7d5cb68ef0543786c2fdf9
https://stackoverflow.com/questions/66127551/list-of-all-roles-with-attached-policies-with-boto3