# https://stackoverflow.com/questions/66127551/list-of-all-roles-with-attached-policies-with-boto3

import boto3

from typing import Dict, List

client = boto3.client('iam')


def get_role_names() -> List[str]:
    """ Retrieve a list of role names by paginating over list_roles() calls """
    roles = []
    role_paginator = client.get_paginator('list_roles')
    for response in role_paginator.paginate():
        response_role_names = [r.get('RoleName') for r in response['Roles']]
        roles.extend(response_role_names)
    return roles


def get_policies_for_roles(role_names: List[str]) -> Dict[str, List[Dict[str, str]]]:
    """ Create a mapping of role names and any policies they have attached to them by 
        paginating over list_attached_role_policies() calls for each role name. 
        Attached policies will include policy name and ARN.
    """
    policy_map = {}
    policy_paginator = client.get_paginator('list_attached_role_policies')
    for name in role_names:
        role_policies = []
        for response in policy_paginator.paginate(RoleName=name):
            role_policies.extend(response.get('AttachedPolicies'))
        policy_map.update({name: role_policies})
    return policy_map




def get_paginated_results(product, action, key, args=None):        
    return [y for sublist in [x[key] for x in boto3.client(
        product).get_paginator(action).paginate(**args)]
            for y in sublist]

def get_policy_documents_for_role(role_name):
    attached_policies = get_paginated_results(
        'iam', 'list_attached_role_policies', 'AttachedPolicies', {'RoleName': role_name})
    inline_policies = get_paginated_results(
        'iam', 'list_role_policies', 'PolicyNames', {'RoleName': role_name})
    policies = []
    client_iam = boto3.client('iam')
    for policy_arn in [x['PolicyArn'] for x in attached_policies]:
        version_id = client_iam.get_policy(
            PolicyArn=policy_arn)['Policy']['DefaultVersionId']
        response = client_iam.get_policy_version(
            PolicyArn=policy_arn, VersionId=version_id)
        # supposedly boto3 urldecodes and json parses the document
        # https://docs.aws.amazon.com/code-samples/latest/catalog/python-iam-get_policy_version.py.html
        policies.extend(response['PolicyVersion']['Document'])
    for policy_name in inline_policies:
        response = client_iam.get_role_policy(
            RoleName=role_name,
            PolicyName=policy_name)
        # see if an IAM policy written in YAML in CloudFormation is correctly parsed and returned here as an object
        policies.extend(response['PolicyDocument'])
    return policies

#role_names = get_role_names()
'''
role_names = ['ria-crop-image-role-wxpkpwcs']
attached_role_policies = get_policies_for_roles(role_names)
print(attached_role_policies)
'''

'''
policies = get_policy_documents_for_role('ria-crop-image-role-wxpkpwcs')
print(policies)
'''


client_iam = boto3.client('iam')

'''
inline_response = client_iam.get_role_policy(
            RoleName='ria-crop-image-role-wxpkpwcs',
            PolicyName='AWSLambdaBasicExecutionRole-52db32c5-0793-4bd4-ab8b-449016e0b153')
print(inline_response)
'''

version_id = client_iam.get_policy(
            PolicyArn='arn:aws:iam::838635938245:policy/service-role/AWSLambdaBasicExecutionRole-52db32c5-0793-4bd4-ab8b-449016e0b153')['Policy']['DefaultVersionId']
print('policy version id:'+version_id)      
attached_response = client_iam.get_policy_version(
            PolicyArn='arn:aws:iam::838635938245:policy/service-role/AWSLambdaBasicExecutionRole-52db32c5-0793-4bd4-ab8b-449016e0b153', VersionId=version_id) 
#response['PolicyVersion']['Document']
print(attached_response)
 
