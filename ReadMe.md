# AWS online deployment at
http://34.224.169.99:8080/api/


# Run through docker
```
docker build -t acerta .
docker run -dp 8080:5000 acerta
```

# Run tests
```
cd /acerta_challenge
python manage.py test
```

# Requirements
```
cd /acerta_challenge
pip install -r requirements.txt
```
