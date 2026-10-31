I’ve programmed an automated resolution theorem prover that works with definite clause knowledge bases. The spec is stored in .json files. It has a knowledge base “kb” which contains a list of clauses in conjunctive normal form. Clauses with one atom are positive. In clauses with more than one atom, the first atom is assumed to be positive while the others are negative. The goal clause (“goal”) is assumed to be a disjunction of negative literals.

Here are some examples of the .json format below:

{
    "kb" : [
        [
            ["GRANDPARENT", "?x","?y"],
                ["PARENT", "?x", "?z"], ["PARENT", "?z", "?y"]
        ],
        [["PARENT", "BRIAN", "DOUG"]],
        [["PARENT", "DOUG", "MARY"]],
        [["PARENT", "MARY", "SUE"]]
    ],

    "goal": [["GRANDPARENT", "?x", "?y"]]
}

{
    "kb": [
        [["SIMPLE_SENTENCE", "?x", "?y", "?z", "?u", "?v"], ["NOUN_PHRASE", "?x", "?y"], ["VERB_PHRASE", "?z", "?u", "?v"]],
        [["NOUN_PHRASE",     "?x", "?y"],                   ["ARTICLE",     "?x"],        ["NOUN",        "?y"]],
        [["VERB_PHRASE",     "?x", "?y", "?z"],              ["VERB",        "?x"],        ["NOUN_PHRASE", "?y", "?z"]],
        [["ARTICLE", "A"]],
        [["ARTICLE", "THE"]],
        [["NOUN",    "MAN"]],
        [["NOUN",    "DOG"]],
        [["VERB",    "LIKES"]],
        [["VERB",    "BITES"]]
    ],
    "goal": [["SIMPLE_SENTENCE", "?a", "?b", "?c", "?d", "?e"]]
}

Now, formulate the following problem and constraints to this specification above and create a .json file:
[YOUR TEXT HERE]
