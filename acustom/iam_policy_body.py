def get_rolename_from_arn(arn):
    return arn.split('/')[-1]


print(get_rolename_from_arn('arn:aws:iam::838635938245:role/service-role/ria-crop-image-role-wxpkpwcs'))