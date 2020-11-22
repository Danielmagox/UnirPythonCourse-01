#!/usr/bin/env python
# coding: utf-8

# ## Ejercicio 1
# 
# Completa la siguiente función para que dado un número de documento nacional de identidad (DNI), se devuelva una letra. Esta letra se obtiene calculando el resto del DNI entre 23 y a partir de ese valor asignarle una letra de la siguiente tabla:
# 
# ![Tabla letras de control DNI](img/letras.jpg)
# 
# El valor DNI será un número entero y la letra debe ser una cadena de carateres que contendrá una única letra en mayúsculas.

# In[9]:


DNIrest = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
def ejercicio_1(dni):
    return DNIrest[dni%23]


# ## Ejercicio 2
# 
# Completa la siguiente función para que dado el precio de un producto, se calcule y se devuelva el precio total que debe pagar el cliente, es decir, incluyenfo el IVA (21% sobre el precio del producto). El precio total deberá ser únicamente el valor del precio, es decir, no debe contener el símbolo de la moneda.
# 

# In[23]:


def ejercicio_2(precio):
    return round(precio * 1.21,2)


# ## Ejercicio 3
# 
# Completa la siguiente función para que dado el diámetro de una circunferencia, se calcule el área del círculo que contiene dicha circunferencia. Como valor de PI se usará $3.1415$.

# In[5]:


def ejercicio_3(diametro):
    return 3.1415 * (diametro/2) * (diametro/2)


# ## Ejercicio 4
# 
# Completar la función para que dado dos números entéros <n> y <m> dos números enteros, se calcula el cociente y el resto de hacer la división entera entre n y m.

# In[7]:


def ejercicio_4(n, m):
    return divmod(n,m)[0], divmod(n,m)[1]


# ## Ejercicio 5
# 
# Completar la función para que dado el número de unidades que ha comprado un usuario de 2 productos diferentes, devolver el peso total del paquete para enviar su compra por mensajería. El peso de cada unidad del producto1 es de 147 unidades y el peso de cada unidad del producto2 es de 2400 unidades. La función debe devolver únicamente el peso total.

# In[5]:


def ejercicio_5(producto1, producto2):
    return (147*producto1 + 2400*producto2)

