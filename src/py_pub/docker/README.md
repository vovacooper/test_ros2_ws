

# compile docker

    docker build -t 675375151216.dkr.ecr.us-east-1.amazonaws.com/py_pub:v1.0 -f docker/Dockerfile .

# run docker

    docker run --rm -it --net=host 675375151216.dkr.ecr.us-east-1.amazonaws.com/py_pub:v1.0 
    ros2 run py_pub listener

# push to ECR

## login
    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 675375151216.dkr.ecr.us-east-1.amazonaws.com

## push
    docker push 675375151216.dkr.ecr.us-east-1.amazonaws.com/py_pub:v1.0 
