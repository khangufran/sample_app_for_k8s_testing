#!/usr/bin/zsh

docker image build -t khhangufran/sample_app_for_k8s_testing:latest .
docker image push khhangufran/sample_app_for_k8s_testing:latest
docker image rm khhangufran/sample_app_for_k8s_testing:latest

kubectl rollout restart deployment sample_app_for_k8s_testing
