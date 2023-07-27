
import pickle


my_dict = {'numbers': [42, 4.1415, (7 + 3j)], 
           'functions': (sum, max), 
           'others': {False, True, 'Hello world!'}
           }
res = pickle.dumps(my_dict)
with open('HW8_Serialization/LEC/pickle/quest.pickle', 'wb') as f:
    pickle.dump(f'{res = }', f)