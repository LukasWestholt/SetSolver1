# German Examples

Credits for the examples goes to: https://gitlab.imn.htwk-leipzig.de/autotool/all0/

## Inhalt

### Mengen
- [Aufgabe 1.demo](#Aufgabe-1demo)
- [Aufgabe 1.1](#aufgabe-11)
- [Aufgabe 1.2](#aufgabe-12)
- [Aufgabe 1.3](#aufgabe-13)
- [Aufgabe 1.4](#aufgabe-14)
- [Aufgabe 1.5](#aufgabe-15)
- [Aufgabe 1.6](#aufgabe-16)


### Mengen mit Relationen
- [Aufgabe 2.demo](#aufgabe-2demo)
- [Aufgabe 2.1](#aufgabe-21)
- [Aufgabe 2.2](#aufgabe-22)
- [Aufgabe 2.3](#aufgabe-23)
- [Aufgabe 2.4](#aufgabe-24)


### MultiMengen
- [Aufgabe 3.demo](#aufgabe-3demo)
- [Aufgabe 3.1](#aufgabe-31)
- [Aufgabe 3.2](#aufgabe-32)


---
---

### [Aufgabe 1.demo](/examples/sets/exercice0.py)

Gesucht ist ein Ausdruck (Term) mit dieser Bedeutung:

    {{1, 2}, {2}}

Der Ausdruck soll höchstens die Größe _10_ haben.\
Sie dürfen diese Symbole benutzen

    Operator-Symbole:
    zweistellige : [ +, -, &]
    einstellige  : [ pow]
    nullstellige : [ ]
    Funktions-Symbole: [ ]

und diese vordefinierten Konstanten:

    A = {1, 2}
    B = {1}

Calculated result:

    (pow(A)-pow(B)) --> {{2}, {1, 2}}
    Calculation ended after 0.063 sec

* * *

### [Aufgabe 1.1](/examples/sets/exercice1.py)
Gesucht ist ein Ausdruck (Term) mit dieser Bedeutung:

    {{{{3}}}}

Der Ausdruck soll höchstens die Größe _30_ haben.\
Sie dürfen diese Symbole benutzen

    Operator-Symbole:
    zweistellige : [ +, -, &]
    einstellige  : [ pow]
    nullstellige : [ ]
    Funktions-Symbole: [ ]

und diese vordefinierten Konstanten:

    A = {{}, {2}, {3}}
    B = {{}, {{3}}}

Calculated result:

    (pow((B-A))-A) --> {{{{3}}}}
    Calculation ended after 0.001 sec

* * *

### [Aufgabe 1.2](/examples/sets/exercice2.py)
Gesucht ist ein Ausdruck (Term) mit dieser Bedeutung:

    {{}, {3}, {5}, {{}}}

Der Ausdruck soll höchstens die Größe _20_ haben.\
Sie dürfen diese Symbole benutzen

    Operator-Symbole:
    zweistellige : [ +, -, &]
    einstellige  : [ pow]
    nullstellige : [ ]
    Funktions-Symbole: [ ]

und diese vordefinierten Konstanten:

    A = {{2, {}}, {5}}
    B = {{}, {3}, {5}}

Calculated result:

    (pow(pow((A-A)))+B) --> {{3}, {{}}, {}, {5}}
    Calculation ended after 0.003 sec

* * *

### [Aufgabe 1.3](/examples/sets/exercice3.py)
Gesucht ist ein Ausdruck (Term) mit dieser Bedeutung:

    {6, {2}}

Der Ausdruck soll höchstens die Größe _30_ haben.\
Sie dürfen diese Symbole benutzen

    Operator-Symbole:
    zweistellige : [ +, -, &]
    einstellige  : [ pow]
    nullstellige : [ ]
    Funktions-Symbole: [ ]

und diese vordefinierten Konstanten:

    U = {3, 5, 6, {1}}
    V = {1, 2, 4, 6, {3}}
    W = {4, {2}}

Calculated result:

    ((V+W)-(V-U)) --> {{2}, 6}
    Calculation ended after 4.58 sec

* * *

### [Aufgabe 1.4](/examples/sets/exercice4.py)
Gesucht ist ein Ausdruck (Term) mit dieser Bedeutung:

    {{}, {1, 2, {3}}, {1, {3}}, {2, {3}}, {{3}}}

Der Ausdruck soll höchstens die Größe _30_ haben.\
Sie dürfen diese Symbole benutzen

    Operator-Symbole:
    zweistellige : [ +, -, &]
    einstellige  : [ pow]
    nullstellige : [ ]
    Funktions-Symbole: [ ]

und diese vordefinierten Konstanten:

    A = {1, 2}
    B = {{3}}

Calculated result:

    (pow(B)+(pow((A+B))-pow(A))) --> {{{3}, 1}, {{3}, 1, 2}, {}, {{3}, 2}, {{3}}}
    Calculation ended after 0.29 sec

* * *

### [Aufgabe 1.5](/examples/sets/exercice5.py)

Gesucht ist ein Ausdruck (Term) mit dieser Bedeutung:

    {{}, {5, {}}, {{5, {}}}}

Der Ausdruck soll höchstens die Größe _30_ haben.\
Sie dürfen diese Symbole benutzen

    Operator-Symbole:
    zweistellige : [ +, -, &]
    einstellige  : [ pow]
    nullstellige : [ ]
    Funktions-Symbole: [ ]

und diese vordefinierten Konstanten:

    A = {{2, {5, {1}}}}
    B = {{}, {5, {}}}

Calculated result:

    (pow((B-pow(A)))+B) --> {{}, {{}, 5}, {{{}, 5}}}
    Calculation ended after 0.002 sec

* * *

### [Aufgabe 1.6](/examples/sets/exercice6.py)

Gesucht ist ein Ausdruck (Term) mit dieser Bedeutung:

    {{}, {5}, {{}}}

Der Ausdruck soll höchstens die Größe _20_ haben.\
Sie dürfen diese Symbole benutzen

    Operator-Symbole:
    zweistellige : [ +, -, &]
    einstellige  : [ pow]
    nullstellige : [ ]
    Funktions-Symbole: [ ]

und diese vordefinierten Konstanten:

    A = {4, {4}, {5}}
    B = {5, {}, {{}}}

Calculated result:

    ((A+B)&pow(B)) --> {{}, {{}}, {5}}
    Calculation ended after 0.994 sec

---
---

### [Aufgabe 2.demo](/examples/sets-relations/exercice0.py)

Die folgende Aufgabe bezieht sich auf Relationen
über dem Grundbereich mkSet

    [ 1, 2, 3]

Gesucht ist ein Ausdruck (Term) mit dieser Bedeutung:

    {(3 , 3)}

Der Ausdruck soll höchstens die Größe _7_ haben.\
Sie dürfen diese Symbole benutzen

    Operator-Symbole:
    zweistellige : [ +, -, &, .]
    einstellige  : [ inverse, reflexive_cl, transitive_cl]
    nullstellige : [ ]
    Funktions-Symbole: [ ]

und diese vordefinierten Konstanten:

    R = {(1 , 2) , (3 , 2)}
    S = {(1 , 1) , (2 , 3) , (3 , 1)}

Calculated result:

    ((inverse(S)&R).S) --> {(3, 3)}
    Calculation ended after 0.004 sec

* * *

### [Aufgabe 2.1](/examples/sets-relations/exercice1.py)

Die folgende Aufgabe bezieht sich auf Relationen
über dem Grundbereich mkSet

    [ 1, 2, 3]

Gesucht ist ein Ausdruck (Term) mit dieser Bedeutung:

    {(1 , 1) , (1 , 2) , (1 , 3), (2 , 1) , (2 , 2)}

Der Ausdruck soll höchstens die Größe _20_ haben.\
Sie dürfen diese Symbole benutzen

    Operator-Symbole:
    zweistellige : [ +, -, &, .]
    einstellige  : [ ]
    nullstellige : [ ]
    Funktions-Symbole: [ ]

und diese vordefinierten Konstanten:

    R = {(2 , 1) , (3 , 1) , (3 , 2)}
    S = {(1 , 2) , (1 , 3) , (2 , 1)}

Calculated result:

    (S.((S.(S+R))+R)) --> {(1, 2), (2, 1), (2, 2), (1, 1), (1, 3)}
    Calculation ended after 0.007 sec

* * *

### [Aufgabe 2.2](/examples/sets-relations/exercice2.py)

Die folgende Aufgabe bezieht sich auf Relationen
über dem Grundbereich mkSet

    [ 1, 2, 3, 4]

Gesucht ist ein Ausdruck (Term) mit dieser Bedeutung:

    {(1 , 3) , (3 , 1) , (3 , 2) , (3 , 4) , (4 , 3)}

Der Ausdruck soll höchstens die Größe _30_ haben.\
Sie dürfen diese Symbole benutzen

    Operator-Symbole:
    zweistellige : [ +, -, &, .]
    einstellige  : [ inverse]
    nullstellige : [ ]
    Funktions-Symbole: [ ]

und diese vordefinierten Konstanten:

    R = {(1 , 1) , (1 , 4) , (3 , 3) , (4 , 4)}
    S = {(2 , 3) , (3 , 1) , (3 , 2) , (3 , 4)}

Calculated result:

    (R.(inverse(S)+S)) --> {(3, 4), (4, 3), (3, 1), (3, 2), (1, 3)}
    Calculation ended after 0.003 sec

* * *

### [Aufgabe 2.3](/examples/sets-relations/exercice3.py)

Die folgende Aufgabe bezieht sich auf Relationen
über dem Grundbereich mkSet

    [ 1, 2, 3, 4]

Gesucht ist ein Ausdruck (Term) mit dieser Bedeutung:

    {(3 , 2) , (3 , 3) , (4 , 1) , (4 , 3) , (4 , 4)}

Der Ausdruck soll höchstens die Größe _20_ haben.\
Sie dürfen diese Symbole benutzen

    Operator-Symbole:
    zweistellige : [ +, -, &, .]
    einstellige  : [ inverse, transitive_cl, reflexive_cl]
    nullstellige : [ ]
    Funktions-Symbole: [ ]

und diese vordefinierten Konstanten:

    R = {(1 , 3) , (2 , 1) , (3 , 1) , (4 , 3)}
    S = {(3 , 2) , (3 , 3) , (4 , 3) , (4 , 4)}

Calculated result:

    (((S&R).R)+S) --> {(4, 4), (3, 3), (4, 3), (3, 2), (4, 1)}
    Calculation ended after 0.009 sec

* * *

### [Aufgabe 2.4](/examples/sets-relations/exercice4.py)

Die folgende Aufgabe bezieht sich auf Relationen
über dem Grundbereich mkSet

    [ 1, 2, 3, 4]

Gesucht ist ein Ausdruck (Term) mit dieser Bedeutung:

    {(3 , 1)}

Der Ausdruck soll höchstens die Größe _50_ haben.\
Sie dürfen diese Symbole benutzen

    Operator-Symbole:
    zweistellige : [ +, -, &, .]
    einstellige  : [ inverse, transitive_cl, reflexive_cl]
    nullstellige : [ ]
    Funktions-Symbole: [ ]

und diese vordefinierten Konstanten:

    R = {(1 , 2) , (4 , 3)}
    S = {(1 , 3) , (2 , 4)}

Calculated result:

    inverse(((R.S).R)) --> {(3, 1)}
    Calculation ended after 0.003 sec

---
---

### [Aufgabe 3.demo](/examples/multisets/exercice0.py)

Gesucht ist ein Ausdruck (Term) mit dieser Bedeutung:

    {q:1}

Der Ausdruck soll höchstens die Größe _30_ haben.\
Sie dürfen diese Symbole benutzen

    Operator-Symbole:
    zweistellige : [ +, -, &]
    einstellige  : [ ]
    nullstellige : [ ]
    Funktions-Symbole: [ ]

und diese vordefinierten Konstanten:

    A = {p:1, q:3}
    B = {q:2, r:3}
    C = {q:1, r:1}

Calculated result:

    (C&A) --> {'q': 1}
    Calculation ended after 0.0 sec

* * *

### [Aufgabe 3.1](/examples/multisets/exercice1.py)

Gesucht ist ein Ausdruck (Term) mit dieser Bedeutung:

    {p:3, q:7, s:5}

Der Ausdruck soll höchstens die Größe _25_ haben.\
Sie dürfen diese Symbole benutzen

    Operator-Symbole:
    zweistellige : [ +, -, &]
    einstellige  : [ ]
    nullstellige : [ ]
    Funktions-Symbole: [ ]

und diese vordefinierten Konstanten:

    A = {p:2, q:1, r:2, t:2, u:4}
    B = {p:1, q:5, s:5}

Calculated result:

    ((A&B)+((A&B)+B)) --> {'p': 3, 'q': 7, 's': 5}
    Calculation ended after 0.305 sec

* * *

### [Aufgabe 3.2](/examples/multisets/exercice2.py)

Gesucht ist ein Ausdruck (Term) mit dieser Bedeutung:

    {p:4, r:11, t:5, u:8}

Der Ausdruck soll höchstens die Größe _30_ haben.\
Sie dürfen diese Symbole benutzen

    Operator-Symbole:
    zweistellige : [ +, -, &]
    einstellige  : [ ]
    nullstellige : [ ]
    Funktions-Symbole: [ ]

und diese vordefinierten Konstanten:

    A = {p:2, r:5, t:3, u:2}
    B = {q:5, s:2, t:1}
    C = {r:1, u:4}

Calculated result:

    (((A+C)+A)-B) --> {'p': 4, 'r': 11, 't': 5, 'u': 8}
    Calculation ended after 0.004 sec
