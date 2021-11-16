# German Examples

## Inhalt

- [Aufgabe (demo)](#aufgabe-demo)
- [Aufgabe 1](#aufgabe-1)
- [Aufgabe 2](#aufgabe-2)
- [Aufgabe 3](#aufgabe-3)
- [Aufgabe 4](#aufgabe-4)
- [Aufgabe 5](#aufgabe-5)
- [Aufgabe 6](#aufgabe-6)

---

### [Aufgabe (demo)](/examples/aufgabe0.py)

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

Calculated result(s):

    (pow(A)-pow(B)) --> {{2}, {1, 2}}
    Calculation ended after 0.56 sec

* * *

### [Aufgabe 1](/examples/aufgabe1.py)
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

Calculated result(s):

    (pow((B-A))-A) --> {{{{3}}}}
    Calculation ended after 0.005 sec

* * *

### [Aufgabe 2](/examples/aufgabe2.py)
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

Calculated result(s):

    (pow(pow((A-A)))+B) --> {{3}, {{}}, {}, {5}}
    Calculation ended after 0.013 sec

* * *

### [Aufgabe 3](/examples/aufgabe3.py)
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

Calculated result(s):

    (((W-V)+U)-(U-V)) --> {{2}, 6}
    Calculation ended after 320.397 sec

* * *

### [Aufgabe 4](/examples/aufgabe4.py)
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

Calculated result(s):

    (pow(B)+(pow((A+B))-pow(A))) --> {{{3}, 1}, {{3}, 1, 2}, {}, {{3}, 2}, {{3}}}
    Calculation ended after 2.889 sec

* * *

### [Aufgabe 5](/examples/aufgabe5.py)

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

Calculated result(s):

    (pow((B-pow(A)))+B) --> {{}, {{}, 5}, {{{}, 5}}}
    Calculation ended after 0.008 sec

* * *

### [Aufgabe 6](/examples/aufgabe6.py)

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

Calculated result(s):

    ((A+B)&pow(B)) --> {{}, {{}}, {5}}
    Calculation ended after 32.459 sec
