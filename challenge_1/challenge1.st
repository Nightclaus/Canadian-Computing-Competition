"Note: Run on Pharo"
| maxInputs radius array results i |

"Read number of inputs"
maxInputs := (Transcript show: 'Enter number of inputs: '; flush).
maxInputs := (FileStream stdin nextLine) asNumber.

radius := maxInputs // 2.
array := OrderedCollection new.

"Read input strings"
1 to: maxInputs do: [:index |
    Transcript show: 'Enter string ', index printString, ': '; flush.
    array add: (FileStream stdin nextLine).
].

results := 0.
1 to: radius do: [:i |
    (array at: i) = (array at: (i + radius))
        ifTrue: [results := results + 2].
].

Transcript show: 'Result: ', results printString; cr.