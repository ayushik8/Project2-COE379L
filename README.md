# README: Project2-COE379L

### Overview
This project includes the deployment of an alternate LeNet-5 model that classifies images of buildings as damaged or not damaged from a hurricane. The model is deployed on an inference server and packaged into a Docker container. This repository includes the necessary files to run the server, including: 
- Dockerfile
- app.py
- docker-compose.yml
- requirements.txt

### To Build the Inference server
- Navigate to the project directory
- Build Docker Image
The docker image is initialized on port 5000, as defined in the Dockerfile.
```bash
docker compose build
docker compose up
```

- You can also pull the prebuilt docker image from Docker Hub using the below command.
- You will then connect the image to a running port.  
```bash
docker pull ayushik7/lenet-new:v1
docker run -d --rm -p 5000:5000 ayushik7/lenet-new:v1
```

### Endpoints Summary 
There are two endpoints implemented on this model. 

### GET Endpoint
```bash
GET /summary
```
- Returns a JSON summary of the metadata of the model.
- Example Command:
``` bash
curl http://localhost:5000/summary
```
- Example Output
```json
{
  "description":"Classify images predicting whether the building has been damaged by a hurricane",
  "input_shape":[null,128,128,3],
  "model_name":"Alternate-LeNet5",
  "number_of_parameters":2601666,
  "output_shape":[null,2]
}
```

 
### POST Endpoint 
```bash
POST /inference
```
Returns the binary classification in JSON of an image whether it is damaged or not. 
- Example Command:
``` bash
curl -X POST -F "file=@/data/damage93.539521_30.982434.jpeg" http://localhost:5000/inference
```
- Example Output
```json
{
  "prediction":"damage"
}
```
