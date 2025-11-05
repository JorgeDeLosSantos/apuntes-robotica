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
Actualmente estos apuntes están en desarrollo, tome sus precauciones con respecto al contenido que podría estar incompleto e inconexo. **Fecha de última actualización: 24/10/2025**
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

*Guanajuato, México.*

$$
\renewcommand{\vec}[1]{\boldsymbol{\mathbf{#1}}}
\renewcommand{\vecg}[1]{\boldsymbol{#1}}
\newcommand{\atantwo}[2]{\text{arctan2} \left( #1,\, #2 \right) }
\newcommand{\arctantwo}[2]{\text{arctan2} \left( #1,\, #2 \right) }
\newcommand{\vecuni}[1]{  \hat{\boldsymbol{\mathbf{#1}}} }
\newcommand{\framei}[1]{ \{#1\} }
\newcommand{\ejt}[1]{e^{j\theta_{#1}}}
\newcommand{\rp}[1]{\dot{r}_{#1}}
\newcommand{\rpp}[1]{\ddot{r}_{#1}}
\newcommand{\w}[1]{\omega_{#1}}
\newcommand{\sint}[4]{\int_{#1}^{#2} #3 \, #4}
\newcommand{\sintp}[4]{\int_{#1}^{#2} \left( #3 \right) \, #4}
\newcommand{\dint}[7]{\int_{#1}^{#2} \int_{#3}^{#4} #5 \, #6 \, #7 }
\newcommand{\dintp}[7]{\int_{#1}^{#2} \int_{#3}^{#4} \left(#5\right) \, #6 \, #7 }
\newcommand{\sumin}{ \mathlarger{\sum}_{i=1}^n }
\newcommand{\rbr}[1]{ \left( #1 \right) }
\newcommand{\sbr}[1]{ \left[ #1 \right] }
\newcommand{\cbr}[1]{ \left\{ #1 \right\} }
\newcommand{\abr}[1]{ \langle #1 \rangle }
\newcommand{\frbr}[2]{ \left( \frac{#1}{#2} \right) }
\newcommand{\fsbr}[2]{ \left[ \frac{#1}{#2} \right] }
\newcommand{\fcbr}[2]{ \left\{ \frac{#1}{#2} \right\} }
\newcommand{\fabr}[2]{ \langle \frac{#1}{#2} \rangle }
\newcommand{\ffrac}[4]{ \frac{ \frac{#1}{#2} }{ \frac{#3}{#4} } }
\newcommand{\La}{\mathcal{L}} 
\newcommand{\Ki}{\mathcal{K}} 
\newcommand{\Po}{\mathcal{P}} 
\newcommand{\LaEq}[1]{
\frac{d}{dt}\left( \frac{\partial\mathcal{L}}{\partial \dot{q}_{#1}} \right) - \frac{\partial\mathcal{L}}{\partial q_{#1}} = \tau_{#1}
}
\newcommand{\LaEqA}[1]{\frac{d}{dt}\left( \frac{\partial\mathcal{L}}{\partial \dot{q}_{#1}} \right)}
\newcommand{\LaEqB}[1]{\frac{\partial\mathcal{L}}{\partial q_{#1}}}
\newcommand{\tauvec}{ \bm{\tau} } 
\newcommand{\KiEq}[1]{ \frac{1}{2} m_{#1} \vec{v}_{G_{#1}}^T \vec{v}_{G_{#1}} +
\frac{1}{2} \bm{\omega}_{#1}^T I_{#1} \bm{\omega}_{#1} } 
\newcommand{\KiTraEq}[1]{ \frac{1}{2} m_{#1} \vec{v}_{G_{#1}}^T \vec{v}_{G_{#1}} } 
\newcommand{\KiRotEq}[1]{ \frac{1}{2} \bm{\omega}_{#1}^T I_{#1} \bm{\omega}_{#1} } 
\newcommand{\PoEq}[1]{ - m_{#1} \vec{g}^T \vec{r}_{G_#1} } 
\newcommand{\Icm}[1]{ I_{#1}^{{#1}'} } 
\newcommand{\Isym}[1]{ 
\begin{bmatrix} 
I_{x_{#1}x_{#1}} & 0 & 0 \\
0 & I_{y_{#1}y_{#1}} & 0 \\
0 & 0 & I_{z_{#1}z_{#1}} \\
\end{bmatrix} 
} 
\newcommand{\rG}[1]{ \vec{r}_{G_{#1}} } 
\newcommand{\vG}[1]{ \vec{v}_{G_{#1}} }
\newcommand{\lc}[1]{ l_{c_{#1}} }
\newcommand{\qp}[1]{\dot{q}_{#1}}
\newcommand{\qpp}[1]{\ddot{q}_{#1}} 
\newcommand{\cijk}[3]{
\frac{1}{2} \left( 
\frac{\partial m_{#1#2}}{\partial q_{#3}} + 
\frac{\partial m_{#1#3}}{\partial q_{#2}} -
\frac{\partial m_{#2#3}}{\partial q_{#1}}
\right)
} 
\newcommand{\wijk}[3]{ \boldsymbol{\omega}_{#2,#3}^{#1}}
\newcommand{\W}{\boldsymbol{\omega}}
\renewcommand{\aa}[1]{\alpha_{#1}} % Aceleración angular
\newcommand{\cdt}[1]{c\theta_{#1}}
\newcommand{\sdt}[1]{s\theta_{#1}}
\newcommand{\tdt}[1]{t\theta_{#1}}
\newcommand{\cdq}[1]{cq_{#1}}
\newcommand{\sdq}[1]{sq_{#1}}
\newcommand{\tdq}[1]{tq_{#1}}
\newcommand{\symlist}{\bullet}
\newcommand{\cda}[1]{c\alpha_{#1}}
\newcommand{\sda}[1]{s\alpha_{#1}}
\newcommand{\cdtt}[2]{c\left(\theta_{#1} + \theta_{#2} \right)}
\newcommand{\sdtt}[2]{s\left(\theta_{#1} + \theta_{#2} \right)}
\newcommand{\colvec}[3]{\begin{bmatrix}#1\\#2\\#3\end{bmatrix}}
\newcommand{\rowvec}[3]{\begin{bmatrix}#1&#2&#3\end{bmatrix}}
\newcommand{\colvech}[4]{\begin{bmatrix}#1\\#2\\#3 \\ #4\end{bmatrix}}
\newcommand{\Tij}[2]{T_{#1}^{#2}}
\newcommand{\Rij}[2]{R_{#1}^{#2}}
\renewcommand{\veci}[2]{\boldsymbol{\mathbf{r}}_{#1}^{#2}}
\DeclareMathOperator{\arctantwo}{arctan2}
\DeclareMathOperator{\sen}{sen}
$$