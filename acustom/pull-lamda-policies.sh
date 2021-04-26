echo "aws lambda list-functions --query 'Functions[*].Role'"
roleArns=(`aws lambda list-functions --query 'Functions[*].Role'`)
echo "aws lambda list-functions --query 'Functions[*].FunctionName'"
functionNames=(`aws lambda list-functions --query 'Functions[*].FunctionName'`)
echo "rm policies.csv"
rm policies.csv
echo 'Add-Content policies.csv "Functions,Roles,Policies"'
echo "Function,Role,Policies" >> policies.csv
for ((i=1;i<roleArns.Length-1;i++))
do
    roleName=roleArns[i].Split("/")[-1].Replace('"', "").Replace(',', "")
    functionName=functionNames[i].Replace('"', "").Replace(',', "").Replace(' ', "")
	echo $functionName
    policies=(`aws iam list-role-policies --role-name $roleName --query 'PolicyNames'`)
    echo "$functionName,$roleName,$policies" >> policies.csv
done