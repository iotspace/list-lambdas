#!/bin/bash
# STOP: DON'T USE/RUN THIS SCRIPT UNLESS YOU ARE 100% SURE WHAT YOU ARE DOING 
#       I am a learner and created 20+ lambda functions while following a tutorial 
#       I wrote this script to programatically cleanup functions at the end of course    
# precondition: your aws cli is configured 
# get all functions from aws account


# functions=(`aws lambda list-functions --query 'Functions[*].[FunctionName]' --output text`)
# for i in "${functions[@]}"
# do
#    #delete functions 1-by-1 
#    #aws lambda delete-function --function-name "$i"   
#    echo "deleted $i"
# done


for roleArn in $(aws lambda list-functions --query 'Functions[*].Role' --output text) ; do
	roleName = aws iam list-roles --query "Roles[?Arn=='${roleArn}'] | [0].{RoleName: RoleName}" ; 
	policies = aws iam list-role-policies --role-name ${roleName} ;
	echo $policies ; done