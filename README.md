# Project2-COE379L

3. Model Deployment & Inference
3.1. Inference Server Building
Navigate to the project directory 
Build Docker Image
Initializes the docker image on port 5000, as defined in the Dockerfile.
docker compose build
docker compose up

You can also pull the prebuilt docker image from Docker Hub using the below command. You will then have to connect the image to a running port.  
docker pull ayushik7/lenet-new:v1
docker run -d --rm -p 5000:5000 ayushik7/lenet-new:v1

3.2. Endpoints Summary 
There are two endpoints implemented on this model. 

GET /summary
POST /inference
Returns a JSON summary of the metadata of the model. 
Returns the binary classification in JSON of an image whether it is damaged or not. 


Example Command: 
curl http://localhost:5000/summary
Example Command: 
curl -X POST -F "file=@/data/damage93.539521_30.982434.jpeg" http://localhost:5000/inference
Example Output: 
{"description":"Classify images predicting whether the building has been damaged by a hurricane","input_shape":[null,128,128,3],"model_name":"Alternate-LeNet5","number_of_parameters":2601666,"output_shape":[null,2]}
Example Output: 
{"prediction":"damage"}

