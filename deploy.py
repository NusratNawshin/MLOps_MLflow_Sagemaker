# Deploy image to Sagemaker
import mlflow.sagemaker as mfs

experiment_id = '1'
run_id = 'c8fe6510d4ff4595XXXXXX'
region = 'us-east-2'
aws_id = 'XXXXXX'
arn = 'arn:aws:iam::XXXXXX:role/sagemaker-full-access-role'
app_name = 'model-application'
model_uri = 'mlruns/%s/%s/artifacts/MLmodel' % (experiment_id, run_id)
tag_id = '1.18.0'

image_url = aws_id + '.dkr.ecr.' + region + '.amazonaws.com/mlflow-pyfunc:' + tag_id

mfs.deploy(app_name=app_name, 
           model_uri=model_uri, 
           region_name=region, 
           mode="create",
           execution_role_arn=arn,
           image_url=image_url)