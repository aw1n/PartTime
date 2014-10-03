'''
Created on 2 oct. 2014

@author: Sylvain
'''

def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None
    
def exists(model, **kwargs):
    try:
        model.objects.get(**kwargs)
        return True
    except model.DoesNotExist:
        return False