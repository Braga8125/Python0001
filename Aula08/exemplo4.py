#Soma de n valores
def soma_coxinha(*args):
    return sum(args)
def media_valores(*args):
    return sum(args)/len(args)
if __name__ == '__main__':
    
    print(soma_coxinha(6,10)) 
    print(soma_coxinha(6,10,20))  
    print(soma_coxinha(6,10,20,58,9,4))  
    print("==== média de n valores ====") 
    print(media_valores(10,8,6))
    print(media_valores(10,10,10,10,10))
    print(media_valores(10,2,2))