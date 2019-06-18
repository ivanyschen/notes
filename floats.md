## Floats

* **key: tradeoff between magnitude and precision**

* floating point numbers in memory:
  

  — ——— ——————— (sign, exponent, fraction)

* doubles have 15 significant digits

* Precision is lost when **adding** or **subtracting** numbers with different magnitude. (multiplication and division are fine)

  ```python
  In [1]: 12345 + 1e15                                                                                                  
  Out[1]: 1000000000012345.0
  
  In [2]: 12345 + 1e16                                                                                                  
  Out[2]: 1.0000000000012344e+16
    
  In [3]: 12345 + 1e17                                                                                                  
  Out[3]: 1.0000000000001235e+17
  ```

* use a library to sum floats (check out `accupy` library)

  ```python
  In [4]: sum([-1e20, 1, 1e20])                                                                                         
  Out[4]: 0.0    # precision lost
    
  In [5]: math.fsum([-1e20, 1, 1e20])                                                                                   
  Out[5]: 1.0    # longer computation time
    
  In [6]: np.sum([-1e20, 1, 1e20])                                                                                     
  Out[6]: 0.0    # precision lost
  ```

* Not all real numbers can be represented in floating numbers ($\pi$, $e$, 0.1, ...)
  


    ,…,……,…………,…………………,…………………,………………...

  0  ^                        0.5                     1.0

     0.1 (need to use the nearest `,` to represent it which is 0.1000000005)


  The difference between a real number and the nearest number is called *relative error*

  ```python
  In [12]: "%0.20f" % (0.1, )                                                                                           
  Out[12]: '0.10000000000000000555'
    
  In [16]: "%0.20f" % (0.2, )                                                                                           
  Out[16]: '0.20000000000000001110'
    
  In [17]: "%0.20f" % (0.1 + 0.2, )                                                                                     
  Out[17]: '0.30000000000000004441'
    
  In [18]: "%0.20f" % (0.3, )                                                                                           
  Out[18]: '0.29999999999999998890'
    
  In [19]: sum([0.1] * 10)                                                                                              
  Out[19]: 0.9999999999999999
  ```

* Every operation introduces some error and nothing can we do about it.

* Be careful when **comparing floats**. Use `np.isclose()`

  ```python
  In [20]: np.isclose(0.1 + 0.2 - 0.3, 0.0)                                                                             
  Out[20]: True
  
  In [21]: 0.1 + 0.2 - 0.3 == 0.0                                                                                       
  Out[21]: False
  ```

* Round floats to the precision before displaying.

  ```python
  In [22]: "%0.2f" % (0.1, )                                                                                            
  Out[22]: '0.10'
  
  In [23]: "%0.2f" % (0.1 + 0.2, )                                                                                      
  Out[23]: '0.30'
  
  In [24]: "%0.2f" % (sum([0.2 * 10]), )                                                                                
  Out[24]: '2.00'
  
  In [25]: "%0.2f" % (sum([0.1 * 10]), )                                                                                
  Out[25]: '1.00'
  ```

## nan

* Not a number

* Reesult of mathematically undefined operations

  ```python
  In [26]: float('inf') / float('inf')                                                                                  
  Out[26]: nan
  ```

* It breaks everything

  ```python
  In [28]: nan = float('nan')                                                                                           
  
  In [29]: nan == nan                                                                                                   
  Out[29]: False
  
  In [30]: 1 > nan                                                                                                      
  Out[30]: False
  
  In [31]: 1 < nan                                                                                                      
  Out[31]: False
  
  In [32]: 1 + nan                                                                                                      
  Out[32]: nan
  ```

* Useful if you want to ignore invalid values

  ```python
  In [33]: a = np.array([1.0, 0.0, 3.0])                                                                                
  
  In [34]: b = np.array([5.0, 0.0, 7.0])                                                                                
  
  In [35]: np.nanmean(a / b)                                                                                            
  RuntimeWarning: invalid value encountered in true_divide
  Out[35]: 0.3142857142857143
  
  In [36]: a / b                                                                                                        
  RuntimeWarning: invalid value encountered in true_divide
  Out[36]: array([0.2 , nan, 0.42857143])
  ```

## `decimal`

* *The `decimal` module provides support for decimal floating point arithmetic.*

* Exact representations of decimal numbers

* the "nearest number" rounding will still happen but it'l be more sensible

* precision still needs to be specified

* Examples:

  ```python
  In [37]: from decimal import Decimal                                                                                  
  
  In [38]: d = Decimal('0.1')                                                                                           
  
  In [39]: sum([d] * 10)                                                                                                
  Out[39]: Decimal('1.0')
  
  In [40]: pi = Decimal(math.pi)                                                                                        
  
  In [41]: pi                                                                                                           
  Out[41]: Decimal('3.141592653589793115997963468544185161590576171875')
  ```

  

Note: Most of the note are by David Wolever. Originl talk: https://www.youtube.com/watch?v=zguLmgYWhM0