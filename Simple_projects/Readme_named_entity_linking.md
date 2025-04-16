# Named Entity Linking (NEL) using spaCy

# Description:
Perform Named Entity Linking using spaCy to map entities in text to real-world entities (from a knowledge base).

# Example Text in script:
"Barack Obama was the 44th President of the United States.Apple expanded to the U.K. with a $1 billion investment."

# Sample Output:

Entity: Barack Obama
Label: PERSON
No linked entity.
----
Entity: 44th
Label: ORDINAL
No linked entity.
----
Entity: the United States
Label: GPE
No linked entity.
----
Entity: Apple
Label: ORG
No linked entity.
----
Entity: U.K.
Label: GPE
No linked entity.
----
Entity: $1 billion
Label: MONEY
No linked entity.
----

# Note:
 Named Entity Linking requires a knowledge base (like Wikidata).
 spaCy's built-in models like 'en_core_web_trf' can support linking, 
 but not all entities will be linked unless customized.

