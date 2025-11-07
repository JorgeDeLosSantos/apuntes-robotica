$$
\renewcommand{\vec}[1]{\boldsymbol{\mathbf{#1}}}
\newcommand{\framei}[1]{ \{#1\} }
% Paréntesis y llaves
\newcommand{\rbr}[1]{ \left( #1 \right) }
\newcommand{\sbr}[1]{ \left[ #1 \right] }
\newcommand{\cbr}[1]{ \left\{ #1 \right\} }
\newcommand{\W}{\boldsymbol{\omega}}
% transformaciones
\newcommand{\Tij}[2]{T_{#1}^{#2}}
\newcommand{\Rij}[2]{R_{#1}^{#2}}
\renewcommand{\veci}[2]{\boldsymbol{\mathbf{r}}_{#1}^{#2}}
$$

# Introducción

```{warning}
Actualmente estos apuntes están en desarrollo, tome sus precauciones con respecto al contenido que podría estar incompleto e inconexo. **Fecha de última actualización: 07/11/2025**
```

Estos apuntes se han elaborado con la finalidad de servir como una referencia rápida para los alumnos de los cursos de Cinemática de Robots y Dinámica de Robots de la Universidad Politécnica de Guanajuato, para sumar a su formación conocimientos sólidos en materia del análisis de manipuladores seriales.

La idea de este texto es proporcionar contenido que sea *digerible* para el alumno, incluyendo ejemplos, ejercicios, ejercicios para resolver con la computadora, videos, animaciones, entre otros recursos, que le ayuden a asimilar los temas correspondientes de una mejor manera. 

## Sobre la notación

A continuación se listan y describen una serie de convenciones y notación a utilizar en el desarrollo del texto:

* Las cantidades vectoriales son representadas mediante letras en negritas, por ejemplo: $\vec{u}$, $\vec{v}$, $ \vec{A} $ y $\vec{B}$. 

* Se utilizan paréntesis para numerar las juntas o articulaciones, corchetes para los eslabones y llaves para los sistemas de referencia. Ejemplo: {\it El sistema de referencia $\{3\}$ está adherido al eslabón $ \sbr{3} $ y su eje $z$ apunta en la dirección de accionamiento de la junta $\rbr{4}$ .}

* $\Rij{n}{m} $ denota una matriz de rotación que describe la orientación del sistema $\{n\}$ con respecto a $\{m\}$.

* $ \Tij{n}{m} $ denota una matriz de transformación homogénea que describe la posición y orientación del sistema $\{n\}$ con respecto a $\{m\}$.

* $ \veci{p}{i} $ representa el vector $\vec{p}$ descrito en el sistema de referencia $ \{i\} $.

* $ J $ denota el jacobiano geométrico de un manipulador.

* $ J_a $ denota el jacobiano analítico de un manipulador.

* $ \W_{m,n}^l $ denota la velocidad angular del sistema $\{n\}$ con respecto al sistema $\{m\}$ medida desde el sistema $\{l\}$.

La siguiente lista describe algunas abreviaturas y notaciones reducidas, sobre todo para funciones trigonométricas que aparecerán de forma muy frecuente en los análisis de cinemática de manipuladores:

* $ c_m = \cos \theta_m = \cos q_m $, sí $m$ es un valor numérico, en caso contrario: $ c_m = \cos m $
* $ s_m = \sin \theta_m = \sin q_m $, sí $m$ es un valor numérico, en caso contrario: $ s_m = \sin m $
* $ c\theta_m = \cos\theta_m $ 
* $ cq_m = \cos q_m $
* $ c(\theta_m + \theta_n) = \cos\left( \theta_m + \theta_n \right) $
* $ c(q_m + q_n) = \cos\left( q_m + q_n\right) $
* $ c_{mn} = \cos(\theta_m + \theta_n) = \cos(q_m + q_n) $, sí $m$ y $n$ son valores numéricos, en caso contrario: $ c_{mn} = \cos(m + n) $

* $ s\theta_m = \sin\theta_m $ 
* $ sq_m = \sin q_m $
* $ s(\theta_m + \theta_n) = \sin\left( \theta_m + \theta_n \right) $
* $ s(q_m + q_n) = \sin\left( q_m + q_n\right) $
* $ s_{mn} = \sin(\theta_m + \theta_n) = \sin(q_m + q_n) $, sí $m$ y $n$ son valores numéricos, en caso contrario: $ c_{mn} = \sin(m + n) $

*Pedro Jorge De Los Santos*