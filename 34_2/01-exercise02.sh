# get request using curl
curl -H "Content-Type: application/json" \
-d '{"userId": 2}' https://jsonplaceholder.typicode.com/posts
# since I'm using -d (sending data), I don't need to specify that it's a POST request
