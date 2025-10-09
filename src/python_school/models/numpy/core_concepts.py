import numpy as np

class CoreConcepts:
    two_dim_arr = np.array([[1, 2, 3], [4, 5, 6]])
    def __init__(self):
        print("Init Core Concepts")

    def create_one_dim_array(self):
        arr = np.array([1, 2, 3])
        print(arr)

    def create_two_dim_array(self):
        arr = np.array([[1, 2, 3], [4, 5, 6]])
        print(arr)
    
    def length_of_array(self):
        print(self.two_dim_arr.size)

    def matrix_mult(self):
        arr_a = np.array([[1, 2, 3], [4, 5, 6]])
        arr_b = np.array([[10, 11], [20, 21], [30, 31]])
        arr_c = np.dot(arr_a, arr_b)
        print(arr_c)

    def stat_fun(self):
        sales = np.array([123, 234, 345, 456 ,567 ,678 ,789])
        print("Total Sales: ", sales.sum())
        print("Min Sales: ", sales.min())
        print("Max Sales: ", sales.max())
        print("Mean Sales: ", sales.mean())
        print("Standard Deviation Sales: ", sales.std())

    def broad_casting(self):
        lst=[10, 20, 30]
        print(lst*3)

        arr=np.array(lst)
        print(arr*3)
    
    def reshape_arr(self):
        print(self.two_dim_arr.shape)
        arr_new = self.two_dim_arr.reshape(3, 2)
        print(arr_new)

    def transpose_arr(self):
        print(self.two_dim_arr.transpose())
        print("Another short form: ", self.two_dim_arr.T)

if __name__=="__main__":
    print("Mian Class of Core Concepts")
    coreConcepts = CoreConcepts()
    coreConcepts.create_one_dim_array()
    coreConcepts.create_two_dim_array()
    coreConcepts.length_of_array()
    coreConcepts.matrix_mult()
    coreConcepts.stat_fun()
    coreConcepts.broad_casting()
    coreConcepts.reshape_arr()
    coreConcepts.transpose_arr()
    
