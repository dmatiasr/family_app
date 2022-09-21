# family_app
Docker steps:
docker build -t family_app .
docker run -d -p 8080:8000  -v src:/deb/app --name family_api_v1 family_app