import re
def fun(s):
    # return True if s is a valid email, else return False
    if(re.search('^[a-z0-9_-]+@[a-z0-9]+\.[a-z]{1,3}$', s)):
        username = s[:s.find('@')]
        websitename = s[s.find('@')+1:s.find('.')]
        ex = s[s.find('.')+1:]
        if (not username.replace('-', '').replace('_', '').isalnum()):
            return False
        if (not websitename.isalnum()):
            return False
        if len(ex) > 3:
            return False       
        return True
         
    else:
        return False

    
    
    

